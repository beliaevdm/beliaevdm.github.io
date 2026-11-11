---
layout: privacy
title: "Privacy Policy — Crumb: Cookie Consent & CCPA"
app: "Crumb: Cookie Consent & CCPA"
updated: 11 November 2026
changes:
  - "11 November 2026 — first version."
---
## 3. Information the app processes

**Settings chosen by the site owner:** whether the banner is on, its layout and position, colours, fonts and other
design choices, every text and its translations, the privacy and cookie policy links, which buttons and categories
visitors see, the cookie button, and (on the paid plan) region rules, pages without the banner and the renewal period.
They are stored in the parameters of the app's script in the site's Wix settings. When the banner is switched on or
off, the app also sets the site's default consent policy in Wix (whether optional tools wait for consent). The app
reads the site's address and plan from Wix to show the "Check my live site" link and to know which features are
included.

**Visitors:** the app collects **no personal data from visitors** and sends nothing about them to us. When a visitor
makes a choice on the banner, the app hands that choice (which cookie categories are allowed) to Wix's own consent
system on the site; Wix stores it and decides which of the site's tools may run. To pick the right banner, the
visitor's browser reads the page language, the device's time zone (only for region rules) and the browser's Global
Privacy Control signal; these are used inside the browser and are not stored or sent by the app.

## 4. Cookies and browser storage

The app **does not set any cookies** of its own. The visitor's consent choice is stored by Wix in Wix's own consent
cookie, under Wix's privacy policy. In the visitor's browser the app keeps only two small markers in `localStorage`:

- `crb-implied` — the time when the banner recorded a choice on the visitor's behalf (on the paid plan, a visitor
  outside the owner's chosen regions), so it is not recorded again on every page;
- `crb-gpc-ok` — that the visitor switched advertising or data sharing on themselves while their browser sent a Global
  Privacy Control signal, so the signal is not applied over their own choice.

On a shared free-site address the keys start with the site's folder name. Neither holds personal data. In the site
owner's dashboard, `localStorage` remembers whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own and loads no outside files on the site.
When the site owner leaves "Consent Mode" on, the app writes consent signals (granted or denied for analytics and
advertising) into the page's standard tag data layer, where the site's own analytics and advertising tags, if any,
read them; those tags are chosen by the site owner and are not controlled by us.

## 6. How long data is kept, and how to delete it

Settings stay until the site owner changes them. Turning the banner off removes the app's script from the site and
keeps the settings; uninstalling the app removes the script and its settings. A visitor's consent choice is kept by
Wix for as long as Wix keeps it, or until the visitor changes it with the cookie button, or until the banner asks
again (the owner's "Ask everyone again", or the paid plan's renewal after 6 or 12 months). A visitor can delete the
markers in section 4 and Wix's consent cookie at any time by clearing the site's data in their browser.
