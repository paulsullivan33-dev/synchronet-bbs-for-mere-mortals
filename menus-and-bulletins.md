# Menus and bulletins

**Outcome: you can walk a caller from the
logon banner to the main menu, read the
board's bulletins on the way, and name the
prompt that tells a caller where they are.**

Check: from transcript t10 — the bulletins
menu offers three stock bulletins, the
first is the board's statistics, and the
main menu's prompt reads
`* Main * 3:59:52 [1] Local [2] General:`,
naming the menu, the time left, and the
current message area in one line.

## The logon sequence

A caller's arrival has a fixed shape
(transcripts t09 to t12):

1. The **banner**: the board's name,
   version, node number ("NODE: 1 (of
   4)"), and the logon prompt.
2. Name and password, then "Logging on to
   The Reading Room as Alex Rivers ...",
   while the board loads the caller's
   **message pointers** — its memory of
   what each caller has already read, so
   boards can offer only what is new.
3. A **logon screen** of ANSI art, paused
   at **[Hit a key]**. Most prompts like
   this on a BBS are *hotkeys*: they read
   a single keypress and move on. Pressing
   Enter afterwards too sends a stray
   keystroke into the *next* prompt — the
   troubleshooting chapter has the full
   story, because it catches everyone.
4. Any **unread mail** is offered
   immediately: "Read your unread mail
   now?" A first-time caller has one piece
   waiting, the welcome mail of chapter 9.

## Bulletins

Then the **BullsEye!** bulletins menu
appears — the board's notice board, a
numbered list of text files. Stock, it
holds three: the board's **Statistics**,
**New user instructions**, and **About
this version of Synchronet**. Press a
number to read one, `Q` to move on.

The statistics bulletin is worth reading
as a sysop, because it is the board's
whole diary in one screen (transcript
t10): where the board is, how long it has
been up, and the totals — Users, Logons,
Messages, E-mail, Files. It is also the
check this guide used twice: after the
first registration it counted the new
users, and after chapter 8's post it is
where a Messages total of 1 will appear.

After the bulletins come the last few
callers list and a one-screen summary of
*your* session — logons today, time used,
mail waiting, whether the sysop is
available — and one question:

```text
[+] Search all groups for new messages? [Yes]
```

Say yes and the board scans every board
for messages newer than your pointers;
say no and you go straight to the menu.
Either way, you arrive at the board's
centre.

## The main menu

The **main menu** is a single screen of
one-key commands in groups (transcript
t10 shows it in full): Read/Post messages,
Message Area Selection, Electronic Mail,
Message Search, Go to (files, text files,
chat, external programs), and Other
commands. It redraws after each command,
under the prompt that keeps a caller
oriented:

```text
* Main * 3:59:52 [1] Local [2] General:
```

Menu name, time remaining today, current
message **group** and **sub-board** — the
four facts a caller needs, always on
screen. A few keys deserve learning first:
`N` scans for new messages, `R` reads, `L`
lists the current board's messages, `P`
posts, `E` is e-mail, `I` is information
about the board, `O` logs off — the board
asks "Log off? [No]" first, because a
stray keypress should not end a call.
Chapter 8 stays inside the message keys;
chapter 9 maps the rest.
