# Installing Synchronet

**Outcome: Synchronet 3.21e is built from
the project's own sources, in a folder of
your choosing, and the program itself
reports its version.**

Check: `exec/sbbs --version` prints
"Synchronet Console for Linux-x64 Version
3.21e" (transcript t03). Until it does,
nothing after this chapter can work.

Synchronet's project documents two Linux
routes: building from the Git repository
with the project's installer makefile, and
older package routes. This guide follows
the Git route — it is the one the project
steers new installs to, and it is the one
the lab ran, word for word. It has three
stages: install the prerequisite packages,
fetch the installer, and let the installer
clone and build everything. The build is
the long part. On the lab's small machine
it took about eighteen minutes; the
project's makefiles do not support
building in parallel, so do not add `-j`
flags hoping to hurry it — pour coffee
instead.

## Stage 1: the prerequisites

Synchronet is written in C and C++ and
links against a handful of libraries. On
Ubuntu 24.04, the lab installed the
project's documented non-graphical set
(transcript t00):

```bash
sudo apt-get update
sudo apt-get install -y git build-essential \
  libarchive-dev libnspr4-dev libcap-dev \
  libmosquitto-dev libsystemd-dev gdb lrzsz
```

`build-essential` brings the compiler and
`make`. The libraries are Synchronet's own
dependencies: `libarchive` for archive
files, `libnspr4` for the portable runtime
its JavaScript engine uses, `libcap` for
file capabilities, `libmosquitto` for its
MQTT support, and `libsystemd` so it can
run properly as a service. `lrzsz` provides
the classic X/Y/ZMODEM file-transfer tools
BBS callers expect. The project's full
prerequisite list also names graphical
libraries for its optional X11 utilities;
a headless board does not need them, and
the lab left them out.

## Stage 2: fetch the installer

Make the folder the board will live in,
and download the project's installer
makefile into it — a single file, straight
from the project's Git repository
(transcript t01):

```bash
mkdir -p ~/sbbs
cd ~/sbbs
wget https://gitlab.synchro.net/sbbs/sbbs/-/raw/master/install/install-sbbs.mk
```

## Stage 3: build

One command does the rest — it clones the
sources into `repo/`, compiles the
JavaScript engine and the bundled crypto
library, then Synchronet itself, and lays
out the board's directory tree
(transcript t02):

```bash
make -f install-sbbs.mk SYMLINK=1 TAG=sbbs321e
```

Two of those choices matter:

- `SYMLINK=1` links the board's working
  directories (`exec`, `text`, `web`,
  `docs`, `xtrn`) into the source tree
  instead of copying them. The project's
  install guide recommends this for Git
  installs, and it makes updating the
  board a matter of updating the sources
  and rebuilding (chapter 10).
- `TAG=sbbs321e` pins the build to the
  current stable release, version 3.21e,
  rather than the moving development tip.
  The tag name is the release with "sbbs"
  in front of it; if a newer release
  exists by the time you read this, its
  tag follows the same pattern.

If your account cannot set the file
capability that lets a program bind to
low ports, add `NOCAP=1` to the command;
the lab's sandbox needed it. This guide
uses a high port (18083) anyway, so the
capability is a formality here.

When the build finishes, the tree holds
real `ctrl/` and `node1`–`node4`
directories beside the symlinks, and the
claim of this chapter can be checked:

```bash
~/sbbs/exec/sbbs --version
```

The lab's answer (transcript t03):
"Synchronet Console for Linux-x64 Version
3.21e", and the terminal server reports
itself compiled from the 3.21e tag. The
board is installed. It is also, so far,
nobody's board: it has the stock name, the
stock settings, and every server switched
on. Chapter 4 fixes all three before it
runs.
