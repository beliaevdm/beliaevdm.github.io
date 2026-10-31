---
layout: privacy
title: "Privacy Policy — Launch Countdown Timer"
app: "Launch Countdown Timer"
updated: 31 October 2026
changes:
  - "31 October 2026 — rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Countdowns (entered by the site owner):** names, launch dates and times, time zones, texts, button labels and
links, theme and colours, and an optional background image link. Stored in the site's Wix collections.

**Visitors:** the app **collects no personal data from visitors**. The browser reads the countdown from the app's
server and calculates the remaining time itself; the server's clock time is sent along so a wrong device clock can
be corrected. Nothing about the visitor is stored.

**Add to calendar:** if a visitor chooses it, the app either opens Google Calendar with the event's title and time
filled in (the visitor decides whether to save it) or creates a standard `.ics` file on the visitor's device.
Nothing is sent to us.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it uses `sessionStorage` to keep a copy of the countdown for faster loading
(cleared when the tab is closed). For "personal" (evergreen) timers only, it keeps one number in `localStorage`: the
time the visitor first saw that countdown, so reloading the page does not restart it; it never leaves the browser.
In the site owner's dashboard, `localStorage` remembers whether the sample content was already added and whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. From visitors' browsers it loads only the background image the site owner chose (normally from Wix
media); Google Calendar opens only when a visitor clicks that option.

## 6. How long data is kept, and how to delete it

Countdowns stay in the site's Wix collections until the site owner deletes them in the app dashboard or in the site's CMS.
