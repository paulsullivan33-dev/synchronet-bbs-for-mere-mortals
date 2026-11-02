# Recipes

**Outcome: four boards assembled from the
chapters before this one — no new
machinery, just the parts combined on
purpose.**

Each recipe assumes chapters 3 to 5 are
done: a built board, privately bound, with
a sysop. Each says what to change, and
what to check.

## Recipe 1: a household board

*For: a family's own message wall — notes,
jokes, a shared diary nobody else can
read.*

Keep chapter 4's configuration exactly as
it stands: loopback only, terminal server
only, telnet on your chosen port. Register
one account per person (chapter 6), and
let General be the family's wall. Add a
second sub-board in `ctrl/msgs.ini` beside
General for the ongoing thread — plans,
shopping, the saga of the boiler — so the
wall stays scannable. Check: the
statistics bulletin counts your household,
and the board is unreachable from any
other machine (`Interface = 127.0.0.1`
sees to that).

## Recipe 2: a club board on the LAN

*For: a club whose members visit from
their own machines on the same network —
a ham club, a retro-computing circle.*

Change one line: bind the board to the
machine's LAN address instead of loopback
(`Interface` in `ctrl/sbbs.ini`), keeping
every other server off. Members telnet to
that address and your port. Register the
officers as callers; rename a sub-board
for club business next to General, and
keep Sysop Notices as the announcement
channel it already is — officers ask, the
sysop posts. Check: a second machine on
the LAN can log on, and the board is
still invisible from the internet because
nothing forwards its port. The step from
here to a public board is a router change
and a moderation commitment, not a
software change — chapter 13 weighs it.

## Recipe 3: reopen a board you shut down

*For: the board from a previous season,
its data directory kept.*

Rebuild or keep the software (chapter 3),
restore `ctrl/` and `data/` from your
backup (chapter 10), start the board, and
log on as the sysop: the SY prompt and
your old accounts are exactly where you
left them, because they were files, not a
service's state. Post in Sysop Notices
that the board is back. Check: the
statistics bulletin shows the old totals,
and an old account's message pointers
still know what it had read.

## Recipe 4: the five-minute health check

*For: any board, weekly.*

1. Log on and read the **Statistics**
   bulletin: users, logons, messages — a
   sudden flat line or a sudden flood is
   the news, either way.
2. Read the **last few callers** list:
   names you know, at hours you expect.
3. Watch the console log for a minute:
   connection attempts from addresses that
   should not know the board exists mean
   a binding or a router changed somewhere.
4. Confirm the backup of `data/` and
   `ctrl/` is newer than the last message
   you would grieve.

A board that passes those four is a board
that is fine. Most weeks, that is the
whole job of being a sysop — which is
rather the point of one.
