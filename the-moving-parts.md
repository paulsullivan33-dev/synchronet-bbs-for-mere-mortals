# The moving parts

**Outcome: you can name the servers inside
Synchronet, the files that configure them,
and the directories that hold a board's
life — so that later chapters' instructions
land on a map you already have.**

Check: given a symptom — "callers can't
connect" versus "the board forgot my
message" — you can say which part, and
which directory, you would look at first.

## One program, several servers

Synchronet is a single program, `sbbs`,
that contains several servers side by side:

- the **terminal server**, the front door:
  it accepts telnet, SSH and rlogin
  connections, runs the logon, and drives
  each caller's session. This guide's lab
  runs only this one.
- the **mail server**, which sends and
  receives internet e-mail (SMTP and POP3)
  and carries the board's internal mail.
- the **FTP server**, for file transfers.
- the **web server**, which serves the
  board's web interface.
- a set of smaller **services** (finger,
  gopher, IRC and others) that can each be
  switched on if wanted.

Each server has its own switch and its own
port in the configuration, and each can be
off. A new install turns most of them on;
chapter 4 turns all but the terminal
server off, on purpose: every listening
server is a door, and you only need one
while you learn.

Inside the terminal server, each caller
occupies a **node** — a numbered slot. A
stock configuration provides four nodes,
so four callers can be on at once; the
connection banner reports "NODE: 1 (of 4)".
What a caller sees and types is driven by
a **command shell**, a script that draws
the menus and interprets the one-key
commands. A fresh board offers callers a
choice at registration between shells,
including **Synchronet Classic**, the
traditional menu this guide uses. The
shell is JavaScript, which is why a BBS
from the modem era can be restyled like a
modern program — and why "the menu did
something odd" and "the server is down"
are different problems in different parts.

## The files that run the board

An install is a tree of directories with
plain names (transcript t03 lists the
lab's):

- `ctrl/` — the **control directory**:
  every configuration file, all of them
  readable text. `sbbs.ini` holds the
  servers' switches, ports and the address
  they bind to. `main.ini` holds the
  board's name and identity and the system
  password. `msgs.ini` holds the message
  boards' settings. A menu-driven
  configuration program, **SCFG**, edits
  these files for you; this guide edits
  them directly so you can see exactly
  what changed.
- `exec/` — the programs: the `sbbs`
  binary itself, its utilities, and the
  JavaScript the shells and services run.
- `data/` — the board's living memory,
  created the first time the server runs:
  the user database, message bases, mail.
  This is the directory a backup exists
  for. If `ctrl/` is the board's mind and
  `exec/` its body, `data/` is its diary.
- `text/` — the screens and menus callers
  see: logon artwork, bulletin files, the
  menu text.
- `node1` to `node4` — one small working
  directory per node.
- `web/` and `webv4/` — the web server's
  roots, unused while the web server is
  off.

Two environment facts hold this together.
The variable **SBBSCTRL** tells the
program where its `ctrl/` directory is,
and the installer offers a choice between
copying the support files into place or
**symlinking** them to the source tree —
the Git install this guide uses symlinks
`exec`, `text`, `web` and friends, so the
source checkout and the running board are
the same files. Chapter 3 uses that
option, and chapter 10's update
instructions depend on it.

## Where messages live

A **message base** is the board's filing
system for public messages. Message areas
are organised two levels deep: a **group**
(such as *Local*) contains **sub-boards**
(such as *General*). Each sub-board has
its own settings — who may read, who may
post — kept in `msgs.ini`, and its
messages in `data/`. A stock board starts
with one small group, which chapter 8
explores live. Beyond the board itself,
Synchronet can exchange messages with
other BBSs through **networks** — DOVE-Net
is Synchronet's own, and QWK packets and
FidoNet are supported too. Networking is
real, documented, and switched off in this
guide: a first board talks to its callers,
not to other boards.
