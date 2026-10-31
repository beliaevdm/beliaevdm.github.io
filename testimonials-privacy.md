---
layout: privacy
title: "Privacy Policy — Testimonials Wall & Slider"
app: "Testimonials Wall & Slider"
updated: 31 October 2026
changes:
  - "31 October 2026 — the spam-limit hash is now made with a server-side secret key; before, it was an unkeyed hash of the network address, the wall and the date, which could be matched by trying every possible address."
  - "31 October 2026 — rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Testimonials added by the site owner:** customer name, role, company, text, rating, date, source and link, photo
link and tags, typed in or imported by the site owner. The site owner is responsible for having each customer's
permission to publish them.

**Wall settings:** layout, theme, colours, filters, texts and collect-form options.

**Testimonials sent by visitors (only if the site owner turns on the collect form):** the name, the text and, if the
site owner asks for them, a star rating, a role or company and an email address. A submission is shown on the site
only after the site owner approves it. The **email address is never shown on the site**; only the site owner sees it
in the dashboard. The site owner is notified of new submissions through Wix notifications.

**Spam protection:** to limit how many testimonials one network can send per day, the app stores a keyed one-way hash
of the sender's network address, the wall and the date, made with a secret key that exists only on the app's
server. The address itself is not stored; the hash cannot be recomputed without the key or linked across days or
walls. Submissions made before 31 October 2026 carry the earlier unkeyed hash.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it uses `sessionStorage` to keep a copy of the wall's published testimonials for
faster loading; it is cleared when the tab is closed. In the site owner's dashboard, `localStorage` remembers whether the sample content was already added and whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. From visitors' browsers it loads only the photos the site owner chose (normally from Wix media); a
review link opens only when a visitor clicks it.

## 6. How long data is kept, and how to delete it

Testimonials, submissions and walls stay in the site's Wix collections until the site owner deletes them in the app
dashboard or in the site's CMS. Removing a wall or the widget does not delete testimonials.
