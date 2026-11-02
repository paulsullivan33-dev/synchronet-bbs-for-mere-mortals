# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's board, sysop and caller are invented, and so is
   its town.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 13 names what the tool
   cannot do: an eighteen-minute source build with no parallel
   option, plaintext telnet, one program holding every server,
   stock timed events that reach for the network on first run,
   software that runs as root if you let it, an interface from
   another era, small scale by design, moderation that is the
   sysop alone, and backups that are two directories and your
   own habit.
8. **The ethics rule is in the text, early.** Chapter 1 states
   the operator's line before any procedure depends on it: a
   sysop can read everything on the board — every message,
   every piece of mail — so callers must be told, their words
   treated as theirs, and the learning board kept reachable
   only from the operator's own machine. The guide's own lab
   held itself to the same rule: invented people, a loopback
   binding, and the system password never printed in any
   transcript.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU Ubuntu 24.04.5 LTS sandbox (GCC
13.3.0, GNU Make 4.3). Synchronet **3.21e** was installed by the
project's documented Git route: the prerequisite packages from
the project's own list, the installer makefile
(`install-sbbs.mk`) fetched from the project's Git repository,
and `make -f install-sbbs.mk SYMLINK=1 NOCAP=1 TAG=sbbs321e`,
which cloned the sources and built them sequentially in about
eighteen minutes (build exit 0; the installer log and the
build's own log are summarised in transcript t02, and the full
build log is kept in the lab folder as `build.log`). `NOCAP=1` was needed
because the sandbox could not set file capabilities; the guide
text says when a reader needs it. The board was configured by
editing `ctrl/sbbs.ini`, `ctrl/main.ini` and `ctrl/msgs.ini`
directly (SCFG, the project's configuration program, was not
used), bound to 127.0.0.1, with the terminal server on telnet
port **18083** and the mail, FTP, web and services servers, the
PETSCII ports, and the rlogin and SSH logon options all off.

The sandbox user is root, so the board ran as root and its
console warning about that is quoted in the text rather than
hidden; on a real machine the board should run as the dedicated
unprivileged account the project's install guide arranges, and
chapters 4, 10 and 13 all say so.

All transcripts live in `synchronet-bbs-lab/transcripts/`. The
terminal session transcripts (t06–t12) were produced by a
scripted telnet driver (`synchronet-bbs-lab/session.py`, its
keystroke scripts beside it) because the lab has no interactive
terminal; the captures were rendered the way a terminal renders
them (backspaces applied, control bytes dropped) and are
otherwise unedited. The system password was passed to the
driver through an environment variable and appears in no
transcript. Passwords shown in transcripts are the invented
lab accounts' own.

Run for real, with transcripts as evidence:

- The environment and the documented prerequisite install,
  including an apt lock collision with another process on the
  shared machine and the successful retry (t00).
- Fetching the installer makefile from the project's Git
  repository (t01) and the full sequential build of the 3.21e
  tag, exit 0 (t02).
- The installed tree and the version checks: "Synchronet
  Console for Linux-x64 Version 3.21e", servers reporting the
  sbbs321e tag (t03).
- Configuration: board name, QWK ID and location set; interface
  bound to 127.0.0.1; telnet port 18083; PETSCII ports off;
  rlogin/SSH options removed; mail, FTP, web and services
  AutoStart off; per-sub-board posting rules read from
  msgs.ini (t04).
- First start: the terminal server listening on 127.0.0.1 port
  18083, four nodes, the `data/` tree created by timed events,
  the running-as-root warning, and one stock timed event's
  outbound FTP attempt failing under the sandbox's network
  policy (t05, and the server log it quotes).
- Sysop registration end to end: the SY system-password
  prompt, the reserved name "Sysop" refused, the generated
  password offered and replaced, the User Settings screen for
  user #1 (t06).
- A sysop logon, including the extra SY prompt ordinary
  callers never see (t07).
- A caller's registration: the full questionnaire, the
  duplicate-name search, the command-shell choice, the User
  Settings screen for user #3, and the referral question
  (t08).
- The welcome e-mail the board sends a new caller, offered at
  logon and read (t09).
- Bulletins read (Statistics: Users 3, Logons counted live),
  the main menu and its prompt, the sub-board list, and
  posting in Local General through the built-in line editor,
  saved and confirmed (t10).
- The posted message read back in a later login: listed with
  L, viewed with V, header and body as posted (t11).
- Logoff with its confirmation prompt and the goodbye screen
  (t12), and the server stopped with the port verified closed
  (t13).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The mail (SMTP/POP3), FTP and web servers and the extra
  services: installed, deliberately left off, and described
  only at that level.
- SSH and rlogin logons (present, switched off), and the
  PETSCII ports for Commodore callers.
- SCFG, the menu-driven configuration program; this guide
  configured by editing the files it edits.
- Message networking: DOVE-Net, QWK exchanges between boards,
  and FidoNet. The board in this guide talked to its callers
  only.
- Door games and external programs, file transfers (including
  ZMODEM, whose tools were installed as prerequisites), chat
  between nodes, and the text-file section — menu-mapped in
  chapter 9, not entered.
- Running Synchronet as a systemd service; the lab ran console
  mode only.
- The neighbour packages of chapter 12 (Mystic BBS, WWIV,
  ENiGMA½) and the web heirs — characterised, not run.
- Opening the board beyond the local machine: LAN bindings are
  described in the recipes as a configuration change, but the
  lab's board never left loopback, and public-internet
  operation is out of scope entirely.

Fixtures are this guide's own and deliberately generic: a
board named The Reading Room in Example Town, a sysop named
Sam Operator, a caller named Alex Rivers, and one short
message about proving the board works. No real person,
address, organisation or event appears anywhere in the lab.
