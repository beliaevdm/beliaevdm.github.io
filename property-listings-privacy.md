---
layout: privacy
title: "Privacy Policy — Property Listings & Search"
app: "Property Listings & Search"
updated: 31 October 2026
changes:
  - "31 October 2026 — the spam-limit hash is now made with a server-side secret key; before, it was an unkeyed hash of the network address, the board and the date, which could be matched by trying every possible address."
  - "31 October 2026 — rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Properties added by the site owner:** title, reference, status, type, price, address, location, rooms, areas,
features, description, photo links, video and tour links, tags and facts, typed in or imported by the site owner.

**Board settings:** layout, theme, colours, filters, texts, and the phone, WhatsApp number and email address the
site owner chooses to show.

**Enquiries sent by visitors (only if the site owner keeps the enquiry form on):** the visitor's name, email address,
message, the property it is about and, if the site owner asks for it, a phone number. Enquiries are **never shown on
the site**; only the site owner sees them in the dashboard. The site owner is notified of each new enquiry through
Wix notifications.

**Spam protection:** to limit how many enquiries one network can send per day, the app stores a keyed one-way hash
of the sender's network address, the board and the date, made with a secret key that exists only on the app's
server. The address itself is not stored; the hash cannot be recomputed without the key or linked across days or
boards. Submissions made before 31 October 2026 carry the earlier unkeyed hash.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it uses `sessionStorage` to keep a copy of the board's published properties for
faster loading; it is cleared when the tab is closed. In the site owner's dashboard, `localStorage` remembers whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. It embeds no maps or videos: from visitors' browsers it loads only the photos the site owner chose
(normally from Wix media). Google Maps, WhatsApp, video and virtual-tour pages open only when a visitor clicks the
matching link and are then governed by those services' own policies.

## 6. How long data is kept, and how to delete it

Properties, boards and enquiries stay in the site's Wix collections until the site owner deletes them in the app
dashboard or in the site's CMS. Removing a board or the widget does not delete properties or enquiries.
