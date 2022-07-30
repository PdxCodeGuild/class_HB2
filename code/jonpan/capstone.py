from random import randint
from asciimatics.screen import Screen

def demo(screen):
    while True:
        screen.print_at(text,
                        randint(0, screen.width), randint(0, screen.height),
                        colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()

text = input("Enter a string:  ")

Screen.wrapper(demo)
