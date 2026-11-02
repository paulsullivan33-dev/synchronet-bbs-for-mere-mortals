# Running the board

**Outcome: you know the ways the board can
be run day to day, what its scheduled
events do while you sleep, how it is
updated, and the one backup habit that
protects everything your callers wrote.**

Check: you can name the directory a backup
must contain (`data/`, with `ctrl/` beside
it) and the two facts the lab proved about
running it — the console start of chapter
4, and the clean stop in transcript t13.

## Console first, service later

This guide runs the board in **console
mode** — the `sbbs` command of chapter 4,
in a terminal, where its log scrolls past
and stopping it is stopping the program.
That is the right way to learn: every
logon, event and error is visible, and
the board's life is obviously tied to a
process you started.

For a board that must survive reboots and
logouts, the project documents running
Synchronet as a system service (a systemd
unit is the usual Linux route). The lab
did not install the service — its board
lived for an afternoon — so this guide
describes the option and points to the
project's install documentation rather
than teaching steps it did not run. The
rule from this series applies: console
until you trust it, service when it earns
it.

However it runs, run it as a **dedicated
unprivileged user** on a real machine.
The board's console warns you when it
runs as root ("No user account specified,
running as root!"), as it did throughout
this lab's sandbox. The project's install
guide arranges a proper account; do not
ship a board as root because the lab's
disposable sandbox did.

## Timed events

A board does housekeeping on a schedule:
**timed events** are small jobs the
terminal server runs at set times — some
maintain the message bases and user file,
and on a networked board they exchange
mail with other systems. Chapter 4 met
one reaching for the internet on its first
run (a stock event fetching a list from
the project's FTP site). On a private
board, open the event configuration and
retire the events that exist to talk to
networks you never joined; keep the
maintenance ones. The principle travels:
a fresh install is configured for the
board its author imagined — public and
networked — and part of configuring yours
is removing the parts of that imagination
you do not share.

## Updating

Because chapter 3 installed with
`SYMLINK=1`, the board's working files
*are* the source tree in `~/sbbs/repo/`.
Updating is the project's documented
routine: pull the new sources, check out
the new release tag, and re-run the
installer makefile to rebuild. Rebuilds
take the same patience as the first one.
Read the project's release notes before
updating a board with callers — a BBS is
stateful in a way a web app is not, and
its database files deserve a backup first
(which is the next section, arriving on
time).

## Backups

Everything your board *is* — as opposed to
the software, which you can rebuild —
lives in two directories:

- `data/` — the user database, the message
  bases, the mail. Lose this and the
  board's history and accounts are gone.
- `ctrl/` — your configuration: the
  board's name, its areas, its passwords.

Copy both, while the board is stopped or
quiet, to anywhere you trust. The lab's
own stop is transcript t13: server
stopped, port confirmed closed, nothing
left listening. A backup taken of a
stopped board is the one kind you never
have to wonder about.

And the operators' last word, callers
permitting: a board's value is its people
and their words. The software is a
download; `data/` is the board.
