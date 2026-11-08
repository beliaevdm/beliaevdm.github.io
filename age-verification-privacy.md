---
layout: privacy
title: "Privacy Policy — Age Check: Age Verification"
app: "Age Check: Age Verification"
updated: 8 November 2026
changes:
  - "8 November 2026 — first version."
---
## 3. Information the app processes

**Settings chosen by the site owner:** whether the gate is on, the minimum age, how visitors answer (Yes/No buttons,
date of birth or year of birth), every text of the gate and its translations, what happens to someone too young (a
message or an address to send them to), how many days an answer is remembered, the colours and design, the logo and
background image chosen from the site's media, and the page rules (page addresses). They are stored in the parameters
of the app's script in the site's Wix settings. The app reads the site's address and plan from Wix to show the "Check
my live site" link and to know which features are included.

**Visitors:** the app collects **no personal data from visitors**. A date or year of birth that a visitor types is
checked inside the visitor's browser against the minimum age and is **never stored or sent anywhere**; the app keeps
only the outcome described in section 4. Nothing about the visitor is sent to us or anyone else.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it stores only the visitor's own answer, so the gate is
not shown again on every page:

- `localStorage` key `agv` (or `sessionStorage` key `agv-s` when the owner chose to ask again in every new browser
  session) — that the minimum age was confirmed, which age that was, when, and whether it was typed or clicked. It
  holds no date of birth. The browser keeps it for the number of days the site owner chose; after that it is ignored
  and replaced at the next answer. The owner's "Ask everyone again" button makes every stored answer invalid.
- `sessionStorage` key `agv-no` — that the visitor answered "No" in this browser tab, so the under-age message stays
  until the tab is closed.

On a shared free-site address the keys start with the site's folder name. In the site owner's dashboard,
`localStorage` remembers whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. The only files the gate loads are the logo
and background image the site owner picked from the site's own media, served by Wix. If the site owner sets an address
for visitors who are too young, those visitors are sent to that address, which is chosen by the owner and not
controlled by us.

## 6. How long data is kept, and how to delete it

Settings stay until the site owner changes them. Turning the gate off removes the app's script from the site and keeps
the settings; uninstalling the app removes the script and its settings. A visitor can delete their stored answer at
any time by clearing the site's data in their browser.
