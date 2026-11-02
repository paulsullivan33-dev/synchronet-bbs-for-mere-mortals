# Configuring the board

**Outcome: the board has your name for it,
only its terminal server will start, and
that server listens on your machine only,
on port 18083 — so the first run is
private by construction.**

Check: the edited lines are visible in
`ctrl/sbbs.ini` and `ctrl/main.ini`
(transcript t04 shows the lab's before
and after), and no other server is set to
start.

A Synchronet board is configured by text
files in `ctrl/`. The project ships a
menu-driven configuration program, SCFG,
that edits them through screens; this
guide edits the files directly, because
seeing the exact lines change teaches you
where things live. Every edit below is a
line in a file you can re-open and check.

## Give the board its identity

In `ctrl/main.ini`, three lines near the
top name the board (the lab's invented
values are shown; choose your own):

```ini
name=The Reading Room
location=Example Town
qwk_id=READROOM
```

`name` is what callers see in the banner
and the bulletins. `location` appears in
the same places and in the user list.
`qwk_id` is the board's short network
identifier — eight characters, no spaces —
used if the board ever joins a message
network; a private board still needs one,
so give it the board's initials. The same
file holds `password=`, the **system
password** — leave it exactly as installed
for now; chapter 5 explains what it is
for and when to change it. Further down,
in `ctrl/msgs.ini`, one line sets the
tagline appended to messages the board
sends to networks:

```ini
default_tagline=The Reading Room
```

## Choose which servers run

In `ctrl/sbbs.ini`, each server has a
section, and each section has switches.
Three edits shape the whole guide:

```ini
[Global]
Interface = 127.0.0.1
```

This binds every server to the loopback
address — the board can be reached only
from this machine. It is the single most
important line in this chapter. A board
you are still learning should not be
findable by anyone else, and this line is
what makes that true rather than hoped.

```ini
[BBS]
TelnetPort = 18083
Pet40Port = 0
Pet80Port = 0
Options = XTRN_MINIMIZED
```

The terminal server's telnet port moves
from the default 23 to **18083** (the lab's
assigned port — on your own machine any
free high port works, but pick one and use
it consistently). The two PETSCII ports —
for Commodore callers, a real and charming
feature — are set to 0, off, since the lab
has no Commodore callers. The `Options`
line, as installed, also enabled rlogin
and SSH logons; the lab removed both
flags, leaving telnet as the one way in.
SSH is the better door for a public board,
and chapter 13 says so plainly; for a
loopback-only board, one door is simpler
to reason about.

Then, in each of the other servers'
sections, one line:

```ini
[Mail]
AutoStart = false
[FTP]
AutoStart = false
[Web]
AutoStart = false
[Services]
AutoStart = false
```

The mail, FTP, web and services servers
now stay off when the board starts. They
are still installed, still configurable,
and still described honestly in later
chapters — they simply do not listen.

## Start it, briefly

With those edits saved, the first start
is one command, run from the board's
folder:

```bash
cd ~/sbbs
SBBSCTRL=$PWD/ctrl ./exec/sbbs
```

The console reports each server starting,
the terminal server "listening on socket
127.0.0.1 port 18083", and four nodes
ready (transcript t05). First starts also
create the `data/` directory and run the
board's **timed events** — small scheduled
jobs; on a stock board a few of them try
to reach the internet (the lab watched one
attempt an FTP fetch for a network image
list, and fail harmlessly in the sandbox).
That is normal, and chapter 10 covers
trimming events on a private board.

Two console lines deserve attention rather
than alarm. "No user account specified,
running as root!" appears when the board
runs as the root user, as the lab's
sandbox does; on a real machine, run the
board as a dedicated unprivileged user, as
the project's install guide arranges. And
the terminal server announcing itself is
your invitation: the board is up, private,
and waiting for its first caller — who is
also its sysop. Leave it running and go
to chapter 5.
