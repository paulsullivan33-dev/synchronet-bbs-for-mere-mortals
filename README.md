# Synchronet BBS for Mere Mortals

Before the web, people dialed into bulletin
board systems — one computer, in someone's
house, that answered the phone and offered
message boards, files, games and chat to
whoever called. **Synchronet** is that
idea kept alive and rebuilt for the
internet age. It is a complete bulletin
board system (a **BBS**) that runs on your
own machine: callers connect over **telnet**
or SSH, create an account, read and post
messages in local boards, send each other
mail, and browse menus — all in text, all
hosted by you. You are the **sysop**, the
system operator, and the board is exactly
as public or as private as you make it.

This guide explains what a modern BBS is,
how Synchronet's parts fit together, how
to install it on Linux the way its project
documents, and how to take a fresh install
to a working board: given a name, bound to
your machine only, with a sysop account, a
first ordinary caller, and a real message
posted and read back in a local message
base. Nothing here needs a network of
other BBSs, a web server, or anyone else's
computer.

The lab that wrote this guide ran the real
thing: **Synchronet 3.21e**, built from the
project's own Git sources by its documented
installer on a small Linux machine — an
eighteen-minute compile — then configured
to listen only on the lab machine itself,
on port 18083. It registered a sysop and a
caller, both invented people on an invented
board, read the board's bulletins, posted
a message in the local General board, and
read that message back in a later login.
Every step is kept as a transcript in the
lab folder.

What the lab deliberately did not switch
on, it did not fake. A stock Synchronet
also contains a mail server, an FTP server,
a web server and more; this guide turns
all of those off and opens only the
terminal server a caller needs, and says
so wherever the others are described.
Joining BBS networks such as DOVE-Net or
FidoNet, running door games, and offering
the board to the public internet are
taught from the documentation and labelled
as such. `criteria.md` keeps the full
ledger of what was run and what was only
read.

One thing belongs up front, because a BBS
makes it true from the first account: **a
sysop can read everything on the board** —
every message, every piece of mail between
callers. Running a board, even a tiny
private one, means holding other people's
words. Chapter 1 states that line early,
and the configuration chapters are built
so you learn the system on a board nobody
else can reach until you decide otherwise.

## What this guide covers

- [**What Synchronet is**](what-synchronet-is.md) —
  the mental model: one program, several
  servers, callers at terminals, and the
  sysop who answers for all of it
- [**The moving parts**](the-moving-parts.md) —
  the terminal, mail, FTP and web servers
  inside one program, the control files
  that configure them, and the directories
  that hold your board's data
- [**Installing Synchronet**](installing-synchronet.md) —
  the documented Linux route: the
  prerequisites, the project's installer
  makefile, the long sequential build, and
  the version check that proves it worked
- [**Configuring the board**](configuring-the-board.md) —
  giving the board a name, choosing which
  servers run, and binding the board to
  your own machine while you learn it
- [**First login and the sysop**](first-login-and-the-sysop.md) —
  the first connection, the system
  password, and creating the sysop account
  that owns the board
- [**Users and passwords**](users-and-passwords.md) —
  how a new caller registers, the questions
  they answer, and the passwords — theirs,
  yours, and the system's
- [**Menus and bulletins**](menus-and-bulletins.md) —
  what a caller sees at logon: bulletins,
  board statistics, the main menu and its
  one-key commands
- [**Message bases**](message-bases.md) —
  groups and sub-boards, who may post
  where, writing a message in the line
  editor, and reading it back
- [**E-mail, files and chat**](email-files-and-chat.md) —
  the welcome mail every new caller gets,
  and an honest map of the file, chat and
  games sections this lab did not open
- [**Running the board**](running-the-board.md) —
  console mode and services, timed events,
  updates, and the backups that matter
- [**Recipes**](recipes.md) — a private
  board for a household, a board for a
  club, reopening a board you shut down,
  and checking a board is healthy
- [**The neighbours**](the-neighbours.md) —
  Mystic BBS, WWIV, ENiGMA½ and the forums
  and chat servers that took the BBS's
  place: what each does differently
- [**Limits**](limits.md) — a long source
  build, plaintext telnet, one program
  holding every server, stock events that
  reach for the network, and a 1990s
  interface that makes no apologies
- [**Troubleshooting**](troubleshooting.md) —
  the name the board refuses, the password
  prompts that surprise you, menus that
  seem to answer themselves, and the
  running-as-root warning
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Opening the board to the public internet —
ports, routers, and the moderation duty
that arrives with strangers — is pointed
at, not taught; learn on loopback first.
Joining message networks (DOVE-Net, QWK,
FidoNet) is described from the project's
documentation only. The web and mail
servers inside Synchronet are real and
documented by the project, but this guide
keeps them off, so running a Synchronet
board as your mail or web server is out
of scope.

## How to use this guide

Read chapter 1 for the model and chapter 2
before installing anything — knowing which
part holds what turns later confusion into
a named problem. Chapters 3 and 4 build
and tame the board; chapter 5 makes you
its sysop. Chapters 6 to 9 are the
caller's life: registering, menus,
messages and mail. The lab's transcripts
live in `synchronet-bbs-lab/transcripts/`;
the scripted terminal driver that produced
the session transcripts is
`synchronet-bbs-lab/session.py`, and the
keystroke scripts it followed are beside
it.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Usenet for Mere Mortals](https://paulsullivan33-dev.github.io/usenet-for-mere-mortals/)
- [DOSBox for Mere Mortals](https://paulsullivan33-dev.github.io/dosbox-for-mere-mortals/)
- [SSH for Mere Mortals](https://paulsullivan33-dev.github.io/ssh-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/synchronet-bbs-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/synchronet-bbs-for-mere-mortals/blob/main/LICENSE-CODE).
