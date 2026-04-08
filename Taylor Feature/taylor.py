import os
import sys
import time
import math
import shutil
import ctypes

#!/usr/bin/env python3
# File: /C:/Users/rainb/GitChallenge2/DevAscDemo/Taylor Feature/taylor.py
# GitHub Copilot


# Enable ANSI on Windows
if os.name == "nt":
    kernel32 = ctypes.windll.kernel32
    h = kernel32.GetStdHandle(-11)
    mode = ctypes.c_uint32()
    if kernel32.GetConsoleMode(h, ctypes.byref(mode)):
        kernel32.SetConsoleMode(h, mode.value | 0x0004)

NAME = "TAYLOR"
SP = "  "  # space between letters

FONT = {
    "T": [
        "TTTTTTT",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   ",
    ],
    "A": [
        "   A   ",
        "  A A  ",
        " A   A ",
        " AAAAA ",
        " A   A ",
        " A   A ",
        " A   A ",
    ],
    "Y": [
        "Y     Y",
        " Y   Y ",
        "  Y Y  ",
        "   Y   ",
        "   Y   ",
        "   Y   ",
        "   Y   ",
    ],
    "L": [
        " L     ",
        " L     ",
        " L     ",
        " L     ",
        " L     ",
        " L     ",
        " LLLLL ",
    ],
    "O": [
        "  OOO  ",
        " O   O ",
        " O   O ",
        " O   O ",
        " O   O ",
        " O   O ",
        "  OOO  ",
    ],
    "R": [
        " RRRR  ",
        " R   R ",
        " R   R ",
        " RRRR  ",
        " R R   ",
        " R  R  ",
        " R   R ",
    ],
}

def hsv_to_rgb(h, s, v):
    h = h % 1.0
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)

def color_text(text, r, g, b):
    return f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m"

def build_lines(name):
    rows = len(next(iter(FONT.values())))
    out = [""] * rows
    for ch in name:
        chf = FONT.get(ch.upper(), [" " * 7] * rows)
        for i in range(rows):
            out[i] += chf[i] + SP
    return out

def center_pad(line):
    cols = shutil.get_terminal_size((80, 20)).columns
    pad = max(0, (cols - len(line)) // 2)
    return " " * pad + line

def render_frame(lines, hue_offset):
    colored = []
    # color each character column by column for a flowing rainbow
    total_cols = sum(len(line) for line in lines)  # rough
    # But we'll color per-letter-block instead
    parts = []
    # split into blocks (letters + spaces) by fixed width
    block_width = 7 + len(SP)
    blocks = len(NAME)
    for bi in range(blocks):
        h = (hue_offset + bi / max(1, blocks)) % 1.0
        r, g, b = hsv_to_rgb(h, 0.9, 0.95)
        parts.append((r, g, b))
    for row in lines:
        line = ""
        for bi in range(blocks):
            start = bi * block_width
            chunk = row[start:start + 7]
            # preserve spaces (don't color them strongly)
            colored_chunk = "".join(
                (color_text(c, *parts[bi]) if c != " " else c) for c in chunk
            )
            line += colored_chunk + " " * (len(SP))
        colored.append(center_pad(line))
    return "\n".join(colored)

def main(frames=40, delay=0.08):
    base = build_lines(NAME)
    try:
        for f in range(frames):
            hue = f / 20.0
            frame = render_frame(base, hue)
            sys.stdout.write("\x1b[2J\x1b[H")  # clear
            sys.stdout.write(frame + "\n")
            sys.stdout.flush()
            time.sleep(delay)
    except KeyboardInterrupt:
        pass
    finally:
        # final static display
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.write(render_frame(base, 0.0) + "\n")

if __name__ == "__main__":
    main()