# First login and the sysop

**Outcome: you have connected to your own
board over telnet, passed its system
password, and created the sysop account —
user number 1 — that owns everything else
in this guide.**

Check: the registration ends at a screen
headed "User Settings for *your name* #1"
(transcript t06). The "#1" is the proof:
the board knows its operator.

## Connecting

Any telnet client reaches the board. The
lab drove it with a small script (kept in
the lab folder) because it has no terminal
of its own; on your machine, use the
telnet client of your choice, pointed at
your own computer:

```bash
telnet 127.0.0.1 18083
```

The board answers with its name and
version, a feature list, and — because no
sysop exists yet — it does not offer the
usual logon. Instead (transcript t06):

```text
Creating sysop account... System password required.
SY:
```

## The system password

The `SY:` prompt is the board asking for
the **system password**: the master
password in `ctrl/main.ini`, set when the
software was installed. It is not your
account password — it is the board's own
lock, and it exists so that the power to
create the sysop account (and, later, to
perform the most sensitive operations)
needs more than an account. Type it and
press Enter. The lab's transcripts never
print it; yours should not either. When
the board is yours and settled, change it
in `main.ini` to something of your own and
keep it with the same care as any master
password — chapter 6 returns to this.

## Registering as sysop

With the system password accepted, the
board walks you through the same
registration every caller gets (chapter 6
details each question), with sysop stakes:

- It detects your terminal, asks you to
  press Backspace so it learns your delete
  key, and asks about **CP437** graphics —
  the classic PC character set BBS art is
  drawn in. Answer yes if your terminal
  shows the art correctly.
- It asks for your **name** — and here is
  the first lesson: the obvious name is
  refused. The lab tried to register as
  "Sysop" and got "You can't use that name
  (duplicate or invalid)". *Sysop* is a
  reserved word on the board, like a
  username a service keeps for itself.
  Use your own name; the board grants the
  powers to the account, not the name.
- It asks for a handle (the lab's sysop is
  *Sam Operator*, handle *SamO*), a
  location, and the rest of the standard
  questionnaire.
- Then the password: the board **generates
  a random password** for the account and
  shows it to you, offering "Enter a
  different password?" Either keep the
  generated one — write it down before you
  press anything — or replace it with your
  own and type it twice. Losing the sysop
  password on a board only you can reach
  is recoverable with effort; on a public
  board it is a small disaster. The lab
  chose its own.

Registration ends in the **User Settings**
screen for your new account, listing the
choices you just made: terminal type,
command shell, editor, and a page of
yes/no defaults, ending at "#1" in the
heading. Press `Q` to leave the settings,
and the board logs you on as its sysop.

Remember the shape of what just happened,
because chapter 6 builds on it: three
different secrets now exist — the system
password, your account password, and (from
the next chapter) each caller's password —
and the board asks for them at different
doors for different reasons.

## A sysop's logon is different

Log off, then log on again as yourself to
see it (transcript t07). Name, account
password — and then the board asks once
more:

```text
SY:
```

A sysop-level logon requires the system
password *as well as* the account
password. Ordinary callers never see this
prompt. It is the board insisting that
whoever holds the keys proves it twice,
and it will surprise you exactly once —
the troubleshooting chapter keeps the
explanation for the day it surprises a
future you.
