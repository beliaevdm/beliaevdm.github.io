---
layout: privacy
title: "Privacy Policy — Instant Quote Calculator"
app: "Instant Quote Calculator"
updated: 31 October 2026
changes:
  - "31 October 2026 — added the events the calculator passes to the site's own Google Tag Manager, Google Analytics or Meta Pixel, which the previous text did not describe. Rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Calculators (entered by the site owner):** fields, options, prices, formulas, texts, appearance settings and,
optionally, a webhook address. Stored in the site's Wix collections.

**Quote requests (sent by visitors):** the name, email address, phone number and message the visitor typed (only the
fields the site owner asks for), the answers they chose and the price breakdown, which the app's server calculates
from the site owner's settings.

**Contacts:** the app adds the visitor's name, email address and phone number to the site owner's Wix Contacts so the
request appears with the owner's other customers.

**Copy of the estimate (only if the site owner turns it on):** the visitor's email address, name and estimate are
passed to Wix's email service to send the visitor one copy of their own estimate; replies go to the site owner.

**Notifications and webhooks:** a notification with the visitor's name, the total and the calculator's name is sent
to the site owner's Wix dashboard and Wix Owner app. If the site owner enters a webhook address, each request is
also sent to that address; the site owner chooses that service and is responsible for it.

**Usage counts:** anonymous counters per calculator and day (views, starts, prices shown, requests sent and the sum
of quoted totals). They contain no personal data.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it uses `sessionStorage` to keep a copy of the calculator for faster loading and
to count a visit only once per session; it is cleared when the tab is closed. In the site owner's dashboard, `localStorage` remembers whether the sample content was already added and whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. If the site itself already uses Google Tag Manager, Google Analytics or a Meta Pixel, the calculator
passes them events about its own use (started, price shown, request sent) inside the visitor's browser; it loads
none of these services itself, and the site owner's settings for them apply. The optional webhook (section 3) sends
data to the service the site owner chose.

## 6. How long data is kept, and how to delete it

Calculators, requests and counters stay in the site's Wix collections until the site owner deletes them. Requests
can be deleted in the Requests tab of the app dashboard or in the site's CMS; deleting a calculator does not delete the
requests it collected. Contacts added to Wix Contacts are managed there by the site owner.
