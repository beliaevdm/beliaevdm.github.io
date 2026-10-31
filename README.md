# beliaevdm.github.io — developer page, legal pages and public assets of the Wix apps by Dmytro Bieliaiev

GitHub Pages (Jekyll, theme minima), root of `main`. Since 2026-10-31 everything that used to live in
`beliaevdm/accessibility-widget-legal` is here; the old repo only redirects its pages to the new addresses.

| Path | What | Source of truth |
|---|---|---|
| `index.html`, `favicon.png`, `img/`, `_src/` | Developer page (Company Info → Website) | `docs/brand/developer-site/` in the wix-apps repo — published with the command in its README, which touches only these paths |
| `<app>-privacy.md`, `<app>-terms.md`, `privacy-policy.md`, `terms-of-service.md` (Accessibility Widget) | Privacy policy and terms of every app | this repo |
| `apps-privacy.md` | General policy, Company Info privacy link | this repo |
| `legal.md` → `/legal` | All apps with Privacy / Terms links | this repo |
| `_layouts/privacy.html`, `_includes/privacy/`, `_templates/app-privacy.md` | One privacy format: sections 1–2 (intro), the app's sections 3–6 (page content), 7–15 (common), change history (front matter) | this repo |
| `apps/<app>/` | SEO pages, listing images (`img/`), demo images loaded by app code (`demo/`) | this repo |
| `assets/` | Shared images (developer logo), Quote Calculator listing images | this repo |

Process and checklist: `docs/PRIVACY-POLICY.md` in the wix-apps repo.
