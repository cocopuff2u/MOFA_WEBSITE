#!/bin/zsh

# Column/output settings
DELIM=" | "          # Text placed between columns (e.g., " | ")

# Show/hide columns (1=show, 0=hide)
SHOW_PATH=1          # Full .app path column
SHOW_NAME=1          # App name column
SHOW_VERSION=1       # App version (CFBundleShortVersionString)
SHOW_BUILD=0         # App build (CFBundleVersion)
SHOW_BUNDLE_ID=1     # Bundle identifier column

# What to scan (1=enable, 0=disable)
SCAN_ALL_USERS=1     # Scan every user's ~/Applications in /Users/* in addition to the current user
INCLUDE_NESTED_APPS=0 # Search inside subfolders and helper apps within bundles (goes deeper)
FOLLOW_SYMLINKS=1    # Follow symlinks (find -L) when scanning
SCAN_HIDDEN_DIRS=1   # Include hidden folders (names starting with .) under scan roots
SKIP_DOT_APPS=0      # Skip .app bundles whose directory name starts with a dot (e.g., /.test/My.app)

# Search depth
MAX_DEPTH=2          # Depth when INCLUDE_NESTED_APPS=0 (top-level + one subfolder)
NESTED_MAX_DEPTH=8   # Depth when INCLUDE_NESTED_APPS=1 (increase to scan deeper trees)

# Output order: reorder these keys to change column order
# Allowed keys: path, name, version_build, bundle_id
# Example: OUTPUT_ORDER=(path name bundle_id version_build)
OUTPUT_ORDER=(name path version_build bundle_id)

# Jamf Extension Attribute output (1=wrap results in <result>...</result> and output full formatted lines;
# SHOW_* and OUTPUT_ORDER still control which columns and order)
JAMF_EA_OUTPUT=1

# Office app detection
# Allowlist: Office-family bundle IDs that should be reported
OFFICE_BUNDLE_IDS=(
  com.microsoft.Word
  com.microsoft.Excel
  com.microsoft.Powerpoint
  com.microsoft.PowerPoint
  com.microsoft.Outlook
  com.microsoft.onenote.mac
  com.microsoft.OneDrive
  com.microsoft.teams
  com.microsoft.teams2
)
# Exclusions: known Microsoft apps that are not Office and should be ignored
EXCLUDE_BUNDLE_IDS=(
  com.microsoft.wdav.shim     # Microsoft Defender Shim
  com.microsoft.VSCode        # Visual Studio Code
  com.microsoft.rdc.macos     # Windows App (Remote Desktop)
)

# Collect Jamf EA values here (full formatted lines)
typeset -a VALID

# Scan /Applications and ~/Applications for Office apps by reading Info.plist
# Output order is configurable via OUTPUT_ORDER; visibility via SHOW_* toggles.

is_office_app() {
	local name="$1"
	local bundle_id="$2"
	local path="$3"

	# Exclude known non-Office Microsoft apps
	if [[ " ${EXCLUDE_BUNDLE_IDS[@]} " == *" $bundle_id "* ]]; then
		return 1
	fi

	# Allowlist: Office bundle IDs
	if [[ " ${OFFICE_BUNDLE_IDS[@]} " == *" $bundle_id "* ]]; then
		return 0
	fi

	# Fallback by product name (case-insensitive) for Office family only
	local target="${(L)name}${(L)path}"
	if [[ "$target" == *word* || "$target" == *excel* || "$target" == *powerpoint* || \
	      "$target" == *outlook* || "$target" == *onenote* || "$target" == *onedrive* || \
	      "$target" == *teams* ]]; then
		return 0
	fi

	return 1
}

get_plist_val() {
	# Usage: get_plist_val <plist_path> <key>
	local plist="$1" key="$2" val=""
	if command -v /usr/libexec/PlistBuddy >/dev/null 2>&1; then
		val="$(/usr/libexec/PlistBuddy -c "Print :$key" "$plist" 2>/dev/null || true)"
	else
		# defaults reads file domains better without the .plist suffix
		local domain="${plist%.plist}"
		val="$(/usr/bin/defaults read "$domain" "$key" 2>/dev/null || true)"
	fi
	printf '%s' "$val"
}

# Join helper to honor a variable delimiter without zsh ${(j:...:)} pitfalls
join_fields() {
	local delim="$1"; shift
	local out="" first=1 f
	for f in "$@"; do
		if (( first )); then
			out="$f"; first=0
		else
			out+="$delim$f"
		fi
	done
	print -r -- "$out"
}

# Build a single formatted result line according to OUTPUT_ORDER and SHOW_* toggles
format_app_info() {
	# Usage: format_app_info <name> <version> <build> <bundle_id> <path>
	local name="$1" ver="$2" build="$3" bundle_id="$4" path="$5"
	local -a fields=()

	for key in "${(@)OUTPUT_ORDER}"; do
		case "$key" in
			path)
				(( SHOW_PATH )) && fields+=("${path:-N/A}")
				;;
			name)
				(( SHOW_NAME )) && fields+=("${name:-N/A}")
				;;
			version_build)
				if (( SHOW_VERSION || SHOW_BUILD )); then
					local v="${ver:-N/A}" b="${build:-N/A}" vb=""
					if (( SHOW_VERSION && SHOW_BUILD )); then
						vb="$v ($b)"
					elif (( SHOW_VERSION )); then
						vb="$v"
					else
						vb="$b"
					fi
					fields+=("$vb")
				fi
				;;
			bundle_id)
				(( SHOW_BUNDLE_ID )) && fields+=("${bundle_id:-N/A}")
				;;
		esac
	done

	join_fields "$DELIM" "${fields[@]}"
}

print_app_info() {
	# Usage: print_app_info <name> <version> <build> <bundle_id> <path>
	local line
	line="$(format_app_info "$@")"
	print -r -- "$line"
}

process_app() {
	local app="$1"
	local plist="$app/Contents/Info.plist"
	[[ -f "$plist" ]] || return 0

	# Resolve to canonical absolute path (handles symlinks)
	local resolved_app="${app:A}"

	# Optionally skip dot-prefixed app bundles (e.g., /.test/*.app or /.Microsoft*.app)
	if (( SKIP_DOT_APPS )) && [[ "${resolved_app:t}" == .* ]]; then
		return 0
	fi

	local name display_name bundle_id ver build
	display_name="$(get_plist_val "$plist" 'CFBundleDisplayName')"
	name="$(get_plist_val "$plist" 'CFBundleName')"
	[[ -n "$display_name" ]] && name="$display_name"
	bundle_id="$(get_plist_val "$plist" 'CFBundleIdentifier')"
	ver="$(get_plist_val "$plist" 'CFBundleShortVersionString')"
	build="$(get_plist_val "$plist" 'CFBundleVersion')"

	if is_office_app "$name" "$bundle_id" "$resolved_app"; then
		if (( JAMF_EA_OUTPUT )); then
			# Collect the full formatted line for Jamf EA
			VALID+=("$(format_app_info "$name" "$ver" "$build" "$bundle_id" "$resolved_app")")
		else
			print_app_info "$name" "$ver" "$build" "$bundle_id" "$resolved_app"
		fi
	fi
}

scan_dir() {
	local dir="$1"
	[[ -d "$dir" ]] || return 0
	# choose depth based on INCLUDE_NESTED_APPS
	local depth="$MAX_DEPTH"
	(( INCLUDE_NESTED_APPS )) && depth="$NESTED_MAX_DEPTH"

	# build find command (optionally follow symlinks)
	local -a find_cmd=(find)
	(( FOLLOW_SYMLINKS )) && find_cmd=(find -L)

	if (( SCAN_HIDDEN_DIRS )); then
		# include hidden folders
		"${find_cmd[@]}" "$dir" -maxdepth "$depth" -type d -name "*.app" 2>/dev/null | while IFS= read -r app; do
			process_app "$app"
		done
	else
		# prune hidden folders
		"${find_cmd[@]}" "$dir" -maxdepth "$depth" \( -path '*/.*' -prune -o -type d -name "*.app" -print \) 2>/dev/null | while IFS= read -r app; do
			process_app "$app"
		done
	fi
}

# Build list of directories to scan based on SCAN_ALL_USERS
build_scan_targets() {
	SCAN_TARGETS=( "/Applications" "$HOME/Applications" )

	if (( SCAN_ALL_USERS )); then
		local home base
		for home in /Users/*; do
			[[ -d "$home" ]] || continue
			base="${home:t}"  # zsh basename
			[[ "$base" == "Shared" || "$base" == ".localized" ]] && continue
			[[ -d "$home/Applications" ]] && SCAN_TARGETS+=("$home/Applications")
		done
	fi
}

main() {
	build_scan_targets
	# Removed: EA-mode warning about SHOW_* columns (EA output now uses the same formatting)

	local dir
	for dir in "${SCAN_TARGETS[@]}"; do
		scan_dir "$dir"
	done

	if (( JAMF_EA_OUTPUT )); then
		echo "<result>"
		(( ${#VALID[@]} )) && printf "%s\n" "${VALID[@]}"
		echo "</result>"
		exit 0
	fi
}

main "$@"
