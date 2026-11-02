# Users and passwords

**Outcome: a second, ordinary account
exists on your board — created the way any
caller creates one — and you can describe
every question registration asks and every
password the board keeps.**

Check: the board's statistics bulletin
counts your new caller (Users: 3 on the
lab board — transcript t10), and the new
account's own settings screen shows its
number, #3 in the lab.

## How a caller registers

At the logon prompt — which now reads
"Enter User Name or 'New' or 'Guest'" — a
new caller types **New**. After terminal
detection (the same backspace test and
CP437 question as chapter 5), the board
checks whether anyone already uses the
name — "Searching for duplicate user
names..." — and asks, in order
(transcript t08):

- **Your name** — the caller's real name,
  or at least the name the board will know
  them by. Duplicates and reserved words
  are refused, as "Sysop" was.
- **Handle or call sign** — the short
  nickname shown in chat and lists; amateur
  radio operators traditionally use their
  call sign, which is why the question is
  worded that way.
- **Location** — free text, shown in the
  user list.
- **Gender** — a single keypress.
- **Birthday** — typed into an MM/DD/YYYY
  mask; the board uses it for age checks
  on restricted areas, if you ever set
  any.
- **Network mail address** — the caller's
  internet e-mail, so the board can reach
  them (and so a forgotten password has
  somewhere to go, on a board with mail
  switched on).
- Whether to **forward** their board mail
  to that address.

Then "Is the above information correct?"
— nothing is saved until the caller says
yes here, which is worth knowing before
you experiment: a half-finished
registration leaves no account behind.

Two things happen next that every caller
sees exactly once. The board offers a
choice of **command shell** — the lab
chose *Synchronet Classic*, the
traditional menus — and asks for a
**password**: it generates a random one,
shows it, and offers the chance to enter
a different one instead, twice for
verification. The registration closes with
the User Settings screen (press `Q`),
one last question — "Where did you hear
about this BBS?" — and the logon sequence
of chapter 7.

The lab's caller is *Alex Rivers* of
Example Town, invented for this guide, and
you should invent yours the same way:
registration is the sysop's only chance
to rehearse being a caller, and you will
understand every later complaint better
for having answered these questions
yourself.

## The three passwords, kept straight

- **Account passwords** belong to callers.
  Each caller picks (or is given) one at
  registration and can change it later.
  Treat the board's user database as
  sensitive material: it holds your
  callers' names, addresses and
  credentials, and chapter 10's backup
  advice exists partly to keep it that
  way — and to keep it at all.
- **Your account password** is a caller's
  password that happens to be yours. It
  opens your account, nothing more.
- **The system password** opens the
  board's deepest doors: creating the
  sysop, sysop-level logons, sensitive
  operations. It lives in `ctrl/main.ini`.
  Change the installed default once your
  board is settled, keep it out of
  transcripts and screenshots, and never
  use it as any account's password.

A caller's account also carries **access
levels** and flags the sysop controls —
who may post where, who is exempt from
time limits, who is locked out entirely.
The stock board's defaults are sensible
for a private board; the message chapter
shows the one place they bite immediately
(a board only the sysop may post to). The
full user editor is part of SCFG and the
project's documentation; this guide's lab
did not need it, and says so.
