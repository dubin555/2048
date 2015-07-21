import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

class keypress(object):
    def get(self):
        inkey = _Getch()
        k=inkey()
        if k=='\x1b[A':
            return "up"
        elif k=='\x1b[B':
            return "down"
        elif k=='\x1b[C':
            return "right"
        elif k=='\x1b[D':
            return "left"
        elif k== "X":
            sys.exit()
        else:
            return "not an arrow key!"

    def main(self):
        for i in range(0,20):
            self.get()

if __name__=='__main__':
    keyboard = keypress()
    keyboard.main()
