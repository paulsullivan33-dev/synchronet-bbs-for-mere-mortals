# Troubleshooting

**Outcome: the surprises this guide's lab
actually met — and the standard ones the
configuration predicts — each with the
check that settles it.**

## "You can't use that name"

Registration refuses some names with
"(duplicate or invalid)". Two causes: the
name is taken, or it is **reserved** —
*Sysop* is the one everyone tries first.
The board keeps its role-words for itself.
Pick your real name or another handle;
the powers follow the account number (#1),
not the word. (Transcript t06.)

## The board asks for a password twice — SY:

Sysop-level logons ask for the account
password *and* the system password, at the
bare prompt `SY:`. It is not a loop and
nothing is wrong. Ordinary callers never
see it. If the system password is refused,
check `password=` in `ctrl/main.ini` —
that file, on the server, is the only
place the answer lives. (Transcripts t06
and t07.)

## Menus that seem to answer themselves

BBS prompts — "[Hit a key]", the yes/no
questions marked `[+]`, the settings
menus — are **hotkeys**: one keypress, no
Enter. If your terminal or your habits
send Enter afterwards, that Enter lands as
the *next* prompt's answer, and screens
appear to choose themselves — the lab's
scripted driver derailed two registrations
exactly this way before the rule was
learned. Answer one prompt, wait for the
next, and if a screen vanishes before you
read it, suspect a stray keystroke before
you suspect the board. In the settings
screens, remember the answers are only
saved when the flow completes — closing
the connection mid-registration leaves no
account behind, which is the safe failure
mode, but a confusing one.

## My caller pressed P and could not post

Posting rights are **per sub-board**
(chapter 8): Sysop Notices allows only the
sysop to post, by configuration
(`post_ars=SYSOP` in `ctrl/msgs.ini`). The
caller is not broken and neither is the
board. Send them to General, or change
the board's rule if it is wrong for your
community.

## "No user account specified, running as root!"

A warning, not an error: the board is
running as the root user. A sandbox or a
first experiment can live with it; a
board that stays up should run as the
dedicated unprivileged account the
project's install guide arranges. The fix
is who runs the program, not a setting
inside it.

## The build stops with a missing library

The compile names what it cannot find.
Match it against the prerequisite list in
chapter 3 (`libarchive-dev`, `libnspr4-dev`,
`libcap-dev`, `libmosquitto-dev`,
`libsystemd-dev` are the usual suspects),
install the missing `-dev` package, and
re-run the installer command — it resumes
from the cloned sources. And if `apt`
itself refuses because another package
process holds the lock, wait for it and
retry; two builders sharing one machine
meet this on any project.

## Something already uses my port

If the console reports the terminal server
cannot bind, another program holds the
port, or a previous `sbbs` is still
running. Find it with `ss -tlnp | grep
18083`, stop it, and start again. To prove
a stopped board is really stopped, the
same command should answer with nothing —
transcript t13 is the lab doing exactly
that check on itself.

## The art looks like line noise

Your terminal and the board disagree about
the character set. The registration
questions ("Use CP437 terminal graphics?")
exist for this: answer so the test art
renders as boxes and lines rather than
stray letters, or switch the board side
later in the caller's User Settings
(terminal type and character set are
per-user settings). A plain ASCII choice
always works and loses only the
decoration.
