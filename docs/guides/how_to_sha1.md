---
title: How To SHA1
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Verify with <span class="gradient-title">SHA1</span></h1>
  <p class="mofa-page-sub">Check that an installer you downloaded is exactly the one Microsoft published.</p>
</div>

<p class="mofa-lead">A SHA1 checksum is a fingerprint of a file. Change one byte and the fingerprint changes completely. MOFA publishes the SHA1 for every installer it tracks, so you can download a package, hash it, and compare. A match means the file arrived untouched.</p>

<div class="mofa-stats">
  <div><b>shasum</b><span>built into every Mac, nothing to install</span></div>
  <div><b>40 hex characters</b><span>the length of a SHA1 checksum</span></div>
  <div><b>Exact match</b><span>anything else means re-download</span></div>
</div>

## Check a file you already have {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12 15h5"/></svg></i><div><b>1. Open Terminal</b><span>Press <kbd>Cmd</kbd> <kbd>Space</kbd>, type Terminal and press Return. It lives in Applications, Utilities.</span></div></div>
  <div class="mofa-row"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg></i><div><b>2. Run shasum</b><span>Type the command below, then drag the file from Finder into the Terminal window to fill in its path, and press Return.</span></div></div>
  <div class="mofa-row"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>3. Compare</b><span>Put the output next to the checksum on the MOFA page. Every character has to match. Case does not matter.</span></div></div>
</div>

```bash
shasum -a 1 ~/Downloads/Microsoft_Word_16.114.pkg
```

The output is the checksum followed by the file name:

```
da39a3ee5e6b4b0d3255bfef95601890afd80709  Microsoft_Word_16.114.pkg
```

## Download and verify in one go {.mofa-h2}

<p class="mofa-lead">If you are scripting it, let shasum do the comparison. Paste the published checksum, two spaces, then the file name, and shasum reports OK or FAILED.</p>

```bash
curl -L -o Microsoft_Word_16.114.pkg "https://go.microsoft.com/fwlink/?linkid=525134"
echo "da39a3ee5e6b4b0d3255bfef95601890afd80709  Microsoft_Word_16.114.pkg" | shasum -a 1 -c
```

```
Microsoft_Word_16.114.pkg: OK
```

<p class="mofa-note">Swap in the checksum from the MOFA page for the file you downloaded. The one above is only an example. The two spaces between the checksum and the file name are required. That is the format shasum writes and the format it reads back with <code>-c</code>. The exit code is 0 on a match and 1 on a mismatch, so it slots straight into a deployment script.</p>

## Where to find the checksums {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="/standalone_apps/standalone_sha1_hashes_en"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>Current versions</b><span>SHA1 for every production installer, updated with each release.</span></div></a>
  <a class="mofa-row" href="/standalone_apps/standalone_preview_sha1_hashes_en"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b>Preview versions</b><span>SHA1 for the Preview channel builds.</span></div></a>
  <a class="mofa-row" href="/standalone_apps/standalone_beta_sha1_hashes_en"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Beta versions</b><span>SHA1 for the Beta channel builds.</span></div></a>
</div>

<p class="mofa-note">SHA1 is older and no longer considered collision resistant. It is fine for spotting a corrupted download, but when a SHA256 is also published, check that one too. MOFA publishes both, and the <a href="/guides/how_to_sha256">SHA256 guide</a> works the same way with <code>-a 256</code>.</p>

## Further reading {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://support.apple.com/guide/terminal/welcome/mac" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12 15h5"/></svg></i><div><b>Terminal User Guide</b><span>Apple's own introduction to Terminal, for anyone new to the command line.</span></div></a>
  <a class="mofa-row" href="https://en.wikipedia.org/wiki/SHA-1" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg></i><div><b>SHA1 on Wikipedia</b><span>How the algorithm works and where it stands today.</span></div></a>
  <a class="mofa-row" href="/standalone_apps/standalone_current_version_en"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>Current versions</b><span>Download links for every installer, straight from Microsoft's CDN.</span></div></a>
</div>

<p class="mofa-foot">Checksum does not match? Download the file again first. A partial or interrupted download is by far the most common cause.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/standalone_apps/standalone_sha1_hashes_en">SHA1 hashes</a>
  <a class="mofa-btn alt" href="/standalone_apps/standalone_current_version_en">Current versions</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/guides/how_to_sha256">How To SHA256</a><a class="mofa-chip outline" href="/guides/how_to_plist">How To Plist</a><a class="mofa-chip outline" href="/about_support/feedback">Feedback</a></div>

</div>
