import os
from enum import Enum

class View:

    def __init__(self, title: str, body: str):
        self.frame = Frame()
        self.title = title.upper()
        self.body = body

    def show(self):

        # Clear screen
        os.system("cls" if os.__name__ == "nt" else "clear")

        self.frame.print_top()
        self.frame.print_text(self.title, Justification.CENTER)
        
        self.frame.print_middle()
        self.frame.print_empty()
        self.frame.print_text(self.body, Justification.LEFT)

        self.frame.print_empty()
        self.frame.print_bottom()


class Justification(Enum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2

class Frame:

    def __init__(self, width: int=100, tab: int=5):
        self.width = width - 2
        self.tab = tab

    def print_top(self):
        print("┌" + "─" * self.width + "┐")

    def print_middle(self):
        print("├" + "─" * self.width + "┤")

    def print_bottom(self):
        print("└" + "─" * self.width + "┘")

    def print_empty(self):
        print("│" + " " * self.width + "│")

    def print_text(self, text: str, justif: Justification=Justification.CENTER):

        for line in text.split("\n"):

            match justif:
                case Justification.LEFT:
                    print("│" + " " * self.tab + line + " " * (self.width - len(line) - self.tab) + "│")
                case Justification.RIGHT:
                    print("│" + " " * (self.width - len(line) - self.tab) + line + " " *  + self.tab + "│")
                case _:
                    print("│" + line.center(self.width) + "│")




# https://www.compart.com/fr/unicode/block/U+2500
# ┌───────────┬───────────┐
# │           │           │
# ├───────────┼───────────┤
# │           │           │
# │           │           │
# │           │           │
# └───────────┴───────────┘

# ┏━━━━━━━━━━━┯━━━━━━━━━━━┓
# ┃           │           ┃
# ┠───────────┼───────────┨
# ┃           │           ┃
# ┃           │           ┃
# ┃           │           ┃
# ┗━━━━━━━━━━━┷━━━━━━━━━━━┛


