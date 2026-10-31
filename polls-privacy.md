---
layout: privacy
title: "Privacy Policy — Poll Maker: Voting & Ratings"
app: "Poll Maker: Voting & Ratings"
updated: 31 October 2026
changes:
  - "31 October 2026 — the vote hash is now made with a server-side secret key; before, it was an unkeyed hash of the network address and the poll's ID, which someone with access to the site's votes collection could match by trying every possible address."
  - "31 October 2026 — added members-only voting, webhooks and dashboard storage, which the previous text did not describe. Rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Polls (entered by the site owner):** questions, options, images, thank-you messages, redirect links, voting
settings, appearance settings, saved themes, custom styles and, optionally, a webhook address. Stored in the site's
Wix collections.

**Votes (sent by visitors):** the chosen option(s) or ranking, a random token created in the visitor's browser and a
**keyed one-way hash** of the visitor's network (IP) address and the poll's ID, made with a secret key that exists
only on the app's server. It is used only to stop the same person voting twice in the same poll; without the key it
cannot be recomputed or turned back into an address, and it cannot be matched across polls. **The network address
itself is never stored.** Votes cast before 31 October 2026 carry the earlier unkeyed hash of the address and the
poll's ID.

**Members-only polls (if the site owner chooses this):** the app asks Wix whether the visitor is logged in as a
site member and, if the site owner limits a poll to members with certain badges, which badges the member holds. To
allow one vote per member it stores a keyed one-way hash of the member's ID and the poll's ID; the ballot itself
contains no member information.

**Email addresses (only if the site owner turns on email collection):** a visitor may enter an email address with
their vote. It is stored in the site's Wix collection and shown only to the site owner, who can export it.

**Webhooks (only if the site owner enters a webhook address):** each vote (poll, question, chosen options and
current results) and each email address left with a vote is also sent to that address. The site owner chooses
that service and is responsible for it.

**Results:** vote totals and a count of votes over time, shown to the site owner and — as the owner chooses — to
visitors.

## 4. Cookies and browser storage

The app **does not set any cookies**. It keeps the random vote token in the visitor's `localStorage` so a visitor is not asked to vote again on
a device where they already voted; the token leaves the device only as part of a vote. In the site owner's dashboard, `localStorage` remembers whether the sample content was already added and whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. If the site owner picks a Google font for a poll, visitors' browsers load it from Google Fonts
(`fonts.googleapis.com`, `fonts.gstatic.com`), which receives the visitor's network address as with any web request
([Google Privacy Policy](https://policies.google.com/privacy)). Without a Google font, no request goes to Google.
The optional webhook (section 3) sends data to the service the site owner chose.

## 6. How long data is kept, and how to delete it

Polls, votes and email addresses stay in the site's Wix collections until the site owner deletes them. Deleting a
poll in the dashboard also deletes its votes and email addresses; the site owner can also delete rows in the site's
CMS.
