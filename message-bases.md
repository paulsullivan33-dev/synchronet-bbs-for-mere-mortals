# Message bases

**Outcome: a message you wrote stands in
the Local group's General sub-board, and
in a later login you can list the board
and read the message back, header and
body, exactly as another caller would.**

Check: transcript t11's reading screen —
"Subj: First post on the new board / From:
Alex Rivers #3" — above the very text
transcript t10 saved with "Posted on
Local General".

## Groups and sub-boards

From the main menu, `*` lists the current
group's sub-boards (transcript t10). The
stock board has one group, **Local**, with
three sub-boards:

```text
Sub-boards of Local                          Msgs

   [1] Sysop Notices                            0
*  [2] General                                  0
   [3] Debate                                   0
```

The `*` marks where you stand. To move,
type the sub-board's **number** at the
main prompt — just the digit, no symbol
(the menu's "# Select sub-board" notation
means "a number", and typing a literal `#`
gets a polite scolding and the hint "Type
the actual number, not the symbol"). `/*`
lists groups the same way, and the prompt
always shows your current area, so you
can confirm the move landed.

The three stock boards teach the one idea
that matters about message areas: **each
sub-board has its own posting rule.** In
**Sysop Notices**, the configuration in
`ctrl/msgs.ini` restricts posting to the
sysop (`post_ars=SYSOP`), making it a
one-way announcement channel: everyone
reads, only the operator writes.
**General** carries no such restriction,
and the lab's caller posted there freely.
Same menu, same key, different rule per
board. When you design your own areas,
that per-board rule is the decision you
are making.

## Posting a message

In General, press `P`. The board answers
"Posting on Local General" and asks one
question before the editor:

```text
Subject: First post on the new board
```

Then the built-in **line editor** opens:

```text
Enter message now (200 lines max). Type /? on a new line for menu.
----+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---
```

Type your message a line at a time,
pressing Enter at each line's end. The
ruler is not decoration: a line longer
than the screen is wrapped mid-word by
the editor, exactly as callers have
endured since dial-up — write short lines.
Commands to the editor go on their own
line and start with a slash: `/?` lists
them, and `/S` saves. The lab's message —
two typed lines, saved as three after the
wrap — came back with the receipt that
ends the act:

```text
Saving ...
Saved 149 characters (3 lines).
Writing Index ...
Posted on Local General.
```

(transcript t10.) The message is now in
`data/`, indexed, and part of the board.

## Reading it back

Posting as its author proves little; the
board's promise is that the message
*persists* and can be read fresh. So the
lab logged off, logged on again, went to
General and pressed `L` — **List/View
messages** (transcript t11):

```text
Loading messages ... Local / General          [message 1 of 1]
# From                      Subject
1 Alex Rivers              <First post on the new board
```

At the lister's prompt, `V` **views** the
selected message (`R` here means *reply*,
a trap the lab found so you do not have
to). The reading screen shows the header —
subject, to, from with account number,
date — and the body, wrapped for the
screen, under a `* Reading *` prompt that
pages through long threads. `Q` returns
to the main menu.

That round trip — write, save, log off,
log on, list, read — is the whole BBS idea
in miniature, and it is the last thing
this guide proves live. Everything else a
board does is an extension of it: more
areas, more callers, other boards, other
networks.
