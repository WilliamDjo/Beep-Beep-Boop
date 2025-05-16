import sys
import tty
import termios

tty.setcbreak(0)
old_settings = termios.tcgetattr(0)

try:
    while True:
        ch = sys.stdin.read(1)
        if "1" <= ch <= "9":
            for _ in range(int(ch)):
                sys.stdout.buffer.write(b"\x07")
        sys.stdout.buffer.flush()
finally:
    termios.tcsetattr(0, termios.TCSADRAIN, old_settings)
