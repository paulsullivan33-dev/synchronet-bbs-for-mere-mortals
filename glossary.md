# Glossary

**BBS (bulletin board system)** — a computer
that hosts a small text community directly:
callers connect to it, log on, and use its
message boards, mail, files and chat. The
host is one machine, run by one operator.

**Sysop** — the system operator: the person
who runs the board, holds its master
password, and can read and moderate
everything on it. Account number 1.

**Caller / user** — anyone with an account
who logs on. The two words are used
interchangeably in BBS culture.

**System password** — the board's own
master password, kept in `ctrl/main.ini`
and asked for at the `SY:` prompt: before
the sysop account is created, and at every
sysop-level logon. Not an account password.

**Node** — one caller slot. A stock board
runs four nodes, so four callers can be on
at once; the banner reports which node you
took.

**Terminal server** — the part of
Synchronet that accepts telnet, SSH and
rlogin connections and runs caller
sessions. The front door.

**Command shell** — the script that draws a
caller's menus and interprets their keys.
Synchronet Classic is the traditional one
this guide uses; shells are JavaScript.

**Message base** — the filing system for
public messages, organised as groups of
sub-boards; also, loosely, one sub-board's
messages.

**Group / sub-board** — the two levels of
message area: a group (Local) holds
sub-boards (General, Debate, Sysop
Notices), each with its own read and post
rules.

**Message pointers** — the board's per-user
memory of what has been read, so scans can
offer only what is new.

**Bulletin** — a text file the board shows
from its BullsEye! menu at logon:
statistics, instructions, announcements.

**BullsEye!** — Synchronet's bulletin menu
program, met at every logon.

**Line editor** — the built-in message
writer: type line by line, command it with
slash lines (`/?` for its menu, `/S` to
save), mind the ruler.

**Door** — an external program the board
runs for a caller, historically games;
Synchronet's plugin mechanism of thirty
years' standing.

**CP437** — the original IBM PC character
set, whose box-drawing characters BBS art
is made of. Terminals that cannot show it
can fall back to plain ASCII.

**ANSI art** — screens drawn with ANSI
escape codes and CP437 characters: the
logon screens and menus' decoration.

**PETSCII** — the Commodore character set;
Synchronet's optional PETSCII ports serve
Commodore callers. Off in this guide.

**SCFG** — Synchronet's menu-driven
configuration program, the screen-based
way to edit what this guide edits as text
files in `ctrl/`.

**SBBSCTRL** — the environment variable
that tells the `sbbs` program where its
control directory lives.

**Timed event** — a scheduled job the
board runs for itself: maintenance on the
bases, or exchanging mail with networks.

**QWK** — an offline message packet format
from the dial-up era, and by extension the
networking built on exchanging packets;
a board's `qwk_id` is its network name.

**DOVE-Net** — Synchronet's own message
network, linking boards that choose to
join it. Described in this guide, not
joined.

**FidoNet** — the oldest store-and-forward
BBS network, still running; Synchronet can
speak its protocols.
