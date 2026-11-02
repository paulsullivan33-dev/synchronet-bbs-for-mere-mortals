#!/usr/bin/env python3
"""Interactive-ish Synchronet telnet session driver (stdin-driven).

Reads commands from stdin, one per line:
  expect <regex>     wait for pattern in output (30s)
  send <text>        send text + CR
  sendenv <VAR>      send value of env var + CR (for secrets; never logged)
  sleep <seconds>
  dump               print cleaned transcript so far
Everything received is accumulated; final transcript goes to argv[1].
"""
import os, re, socket, sys, time

HOST, PORT = "127.0.0.1", 18083

def clean(b: bytes) -> str:
    s = b.decode("cp437", errors="replace")
    s = re.sub(r"\xff[\xfb-\xfe].", "", s)
    s = s.replace("\xff", "")
    s = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", s)
    s = re.sub(r"\x1b[()][0-9A-B]", "", s)
    s = s.replace("\x1b", "")
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s

def main():
    out_path = sys.argv[1]
    sock = socket.create_connection((HOST, PORT), timeout=10)
    sock.settimeout(0.4)
    raw = bytearray()

    def pump(seconds):
        end = time.time() + seconds
        while time.time() < end:
            try:
                data = sock.recv(65536)
                if not data:
                    return
                raw.extend(data)
            except socket.timeout:
                pass
            except OSError:
                return

    state = {"pos": 0}

    def expect(pattern, timeout=30):
        rx = re.compile(pattern, re.S)
        end = time.time() + timeout
        while time.time() < end:
            try:
                data = sock.recv(65536)
                if not data:
                    break
                raw.extend(data)
            except socket.timeout:
                pass
            text = clean(bytes(raw))
            m = rx.search(text, state["pos"])
            if m:
                state["pos"] = m.end()
                return True
        print(f"EXPECT-TIMEOUT: {pattern}", file=sys.stderr)
        return False

    for line in sys.stdin:
        line = line.rstrip("\n")
        if not line:
            continue
        cmd, _, arg = line.partition(" ")
        if cmd == "expect":
            expect(arg)
        elif cmd == "send":
            sock.sendall(arg.encode() + b"\r")
            pump(1.2)
        elif cmd == "key":
            sock.sendall(arg.encode())
            pump(1.2)
        elif cmd == "keyhex":
            sock.sendall(bytes.fromhex(arg))
            pump(1.2)
        elif cmd == "sendenv":
            sock.sendall(os.environ[arg].encode() + b"\r")
            pump(1.2)
        elif cmd == "sleep":
            pump(float(arg))
        elif cmd == "dump":
            print(clean(bytes(raw)))
            sys.stdout.flush()
    pump(1.5)
    with open(out_path, "w") as f:
        f.write(clean(bytes(raw)))
    try:
        sock.close()
    except OSError:
        pass

if __name__ == "__main__":
    main()
