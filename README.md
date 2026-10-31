# Developer page — https://beliaevdm.github.io/

The page behind "App developer → website" on every App Market listing (Dev Center → Company Info → Website,
`COMPANY.website` in `tools/browser/lib/devcenter.mjs`). Set up 2026-10-31: the old link was an empty GitHub profile.

**Source of truth = this folder.** The repo `beliaevdm/beliaevdm.github.io` (GitHub Pages, root of `main`) is only
the published copy.

New app (/new-app Phase 9) or a renamed app / new icon / new demo URL:
1. `_src/apps.jsonl` — one line per app: `app`, `id`, `name`, `teaser` (as on the live listing), `icon` (listing URL).
2. Icon → `img/<app>.png` (192×192): `curl -sL -o img/<app>.png "<icon>/v1/fill/w_192,h_192,al_c,q_90/icon.png"`.
3. `_src/build.py` — demo URL in `demo`, the app in one of `groups` (the script fails if an app is missing).
4. `python3 _src/build.py`, then publish:
   ```bash
   T=$(mktemp -d) && git clone -q https://github.com/beliaevdm/beliaevdm.github.io.git $T \
     && rsync -a --delete --exclude .git docs/brand/developer-site/ $T/ \
     && git -C $T add -A && git -C $T commit -qm "<what changed>" && git -C $T push -q
   ```
Text changes go to `_src/template.html`, never to `index.html` (generated). Jekyll skips `_src/`.
