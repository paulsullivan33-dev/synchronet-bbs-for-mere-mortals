# Limits

**Outcome: you can state plainly what
Synchronet will not do, what it does
awkwardly, and what running it costs —
before any of it surprises you or your
callers.**

- **The install is a source build.** There
  is no one-line package install on the
  documented route: prerequisites, a clone,
  and a compile that took the lab's small
  machine about eighteen minutes, with no
  supported way to parallelise it. Updates
  repeat the compile. This is the price of
  a project that ships source first.
- **Telnet is plaintext.** The protocol
  this guide uses sends everything —
  passwords included — unencrypted. On
  loopback and a home LAN that is a
  contained risk; on the public internet
  it is not. Synchronet offers SSH logons
  (this guide switched them off to keep
  one door), and a public board should use
  them. Do not let nostalgia talk you out
  of encryption.
- **One program holds every server.** The
  terminal, mail, FTP, web and services
  servers are one binary with one
  configuration. Convenience and risk in
  the same shape: a stock install starts
  more doors than a new sysop realises,
  which is why chapter 4 exists. Turn off
  what you do not run, every time.
- **A stock board reaches outward.** Timed
  events on a fresh install try to talk to
  the project's network the moment the
  board first runs. Nothing in the lab was
  harmed by it — the sandbox blocked the
  attempt — but a private board should
  have its events trimmed before it is
  left running, not after.
- **It runs as root if you let it.** The
  console warns you, and then obeys you.
  The discipline — a dedicated,
  unprivileged account — is yours to
  apply; the software will not apply it
  for you.
- **The interface is from another era, on
  purpose.** Eighty columns, hotkeys that
  fire without Enter, line editors with
  rulers, art drawn from a 1980s character
  set. Callers raised on feeds will bounce
  off some of it; callers it suits will
  feel at home instantly. There is no
  mobile app, no push notification, no
  infinite scroll, and there is not going
  to be.
- **Scale is small by design.** Four nodes
  in a stock configuration, files on a
  disk, one machine. Synchronet serves a
  community, not a crowd; a board that
  outgrows it has succeeded at something
  BBSs were never for.
- **The sysop is the moderation team.**
  There is no trust-and-safety department,
  no report queue staffed by a platform —
  there is you, your configuration, and
  your judgment, with total visibility
  (chapter 1) and total responsibility.
  On a private board that is light work.
  On a public one it is the whole job.
- **Backups are files, and your problem.**
  No built-in replication, no hosted
  dashboard: `data/` and `ctrl/`, copied
  by you, on your schedule (chapter 10).
  The board's history is exactly as safe
  as your last copy of two directories.
