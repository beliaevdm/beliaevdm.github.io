---
layout: privacy
title: "Privacy Policy — Launch Countdown & Coming Soon"
app: "Launch Countdown & Coming Soon"
updated: 11 November 2026
changes:
  - "11 November 2026 — the optional waitlist (“Notify me”) form: what it stores, who sees it and how it is deleted (sections 3, 4 and 6). The form is off unless the site owner turns it on."
  - "31 October 2026 — rewritten in the common format used for all our apps (roles, legal bases, rights, retention and how changes are announced)."
---
## 3. Information the app processes

**Countdowns (entered by the site owner):** names, launch dates and times, time zones, texts, button labels and
links, theme and colours, and an optional background image link. Stored in the site's Wix collections.

**Visitors:** the browser reads the countdown from the app's server and calculates the remaining time itself; the
server's clock time is sent along so a wrong device clock can be corrected. Apart from the waitlist below, nothing
about the visitor is stored.

**Waitlist ("Notify me", optional):** only when the site owner turns the form on for a countdown. A visitor who
types an email and presses the button sends that email to the app's server, which stores it in the site's own Wix
collection together with the date, the countdown's name and id, and the countdown's language. The same email is
stored once per countdown. The list is visible only to the site owner and the site's collaborators (in the app's
dashboard and the site's CMS), who can export it as a CSV file to contact the visitors about the launch. We, the app
developer, do not use these emails, do not send messages to them and do not pass them to anyone; we act as a processor
for the site owner. The form shows the owner's own note on what visitors sign up for. An invisible "leave empty" field
in the form is used to stop automated sign-ups; it is not stored.

**Add to calendar:** if a visitor chooses it, the app either opens Google Calendar with the event's title and time
filled in (the visitor decides whether to save it) or creates a standard `.ics` file on the visitor's device.
Nothing is sent to us.

## 4. Cookies and browser storage

The app **does not set any cookies**. In the visitor's browser it uses `sessionStorage` to keep a copy of the countdown for faster loading
(cleared when the tab is closed), and, only when the site owner opens the site with `?skip-countdown`, a flag that
shows a full-screen countdown as a normal block for the rest of that tab. For "personal" (evergreen) timers only, it keeps one number in `localStorage`: the
time the visitor first saw that countdown, so reloading the page does not restart it; it never leaves the browser.
In the site owner's dashboard, `localStorage` remembers whether the sample content was already added and whether a short review request was already shown.

## 5. Third-party services

The app uses **no analytics, tracking or advertising services** of its own. From visitors' browsers it loads only the background image the site owner chose (normally from Wix
media); Google Calendar opens only when a visitor clicks that option.

## 6. How long data is kept, and how to delete it

Countdowns stay in the site's Wix collections until the site owner deletes them in the app dashboard or in the site's CMS.
Waitlist emails stay until the site owner deletes them (one by one, all of one countdown, or all at once in the
app's Waitlist tab, or in the site's CMS); deleting a countdown keeps its sign-ups so they can still be exported. A
visitor who wants their email removed asks the site owner, who controls the list.
