---
title: Raw feeds
---
<div class="mofa-feed-head">
  <img class="mofa-feed-icon" src="/images/App_Store_logo.webp" alt="" />
  <div class="mofa-feed-text">
    <h1>Raw feeds</h1>
    <p>The dataset behind the Mac App Store page, as XML, YAML and JSON.</p>
  </div>
</div>
<div class="mofa-feed-meta">
  <span class="mofa-feed-updated"><i></i>Rebuilt every 2 hours from Microsoft</span>
  <span class="mofa-feed-raw"><a class="mofa-chip outline" href="https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files" target="_blank" rel="noopener">All files on GitHub</a></span>
</div>


## Mac App Store dataset {.mofa-h2-left}

<table class="mofa-feeds">
<thead><tr><th>Feed</th><th>What it contains</th><th>Formats</th><th>Page</th></tr></thead>
<tbody>
<tr><td><b>Mac App Store latest</b></td><td>Current version, release date, min macOS, bundle ID and App Store link for every Microsoft app on the Mac App Store.</td><td class="fmts"><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.xml" target="_blank" rel="noopener">XML</a><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.yaml" target="_blank" rel="noopener">YAML</a><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.json" target="_blank" rel="noopener">JSON</a></td><td><a href="/macos_appstore/macos_appstore_current_version">View →</a></td></tr>
</tbody></table>

Looking for the standalone installers, Office history or RSS feeds? They are on the <a href="/standalone_apps/standalone_raw_feeds_en">standalone raw feeds</a> page.

## Using the feeds {.mofa-h2-left}

For scripts, use the raw file URL rather than the GitHub page, for example:

```
https://raw.githubusercontent.com/cocopuff2u/MOFA/main/latest_raw_files/macos_standalone_latest.json
```

Every file is regenerated on a schedule by the [MOFA repository](https://github.com/cocopuff2u/MOFA)’s GitHub Actions, so a URL you save today keeps returning the latest data. XML, YAML and JSON carry the same fields; pick whichever your tooling reads most easily.
