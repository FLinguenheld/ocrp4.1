from enum import Enum

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

    def print_line(self):
        print("├" + "─" * self.width + "┤")

    def print_blank_line(self):
        print("│" + " " * self.width + "│")

    def print_bottom(self):
        print("└" + "─" * self.width + "┘")

    def print_text(self, text: str, justif: Justification=Justification.CENTER):
        for line in text.split("\n"):
           print(self._build_text(line=line, justif=justif))

    def _build_text(self, line: str, justif: Justification):
        match justif:
                case Justification.LEFT:
                    return str("│" + " " * self.tab + line + " " * (self.width - len(line) - self.tab) + "│" )
                case Justification.RIGHT:
                    return str("│" + " " * (self.width - len(line) - self.tab) + line + " " *  + self.tab + "│" )
                case _:
                    return str("│" + line.center(self.width) + "│" )


    def print_question(self, text: str):

        self.print_line()
        self.print_text(text, Justification.LEFT)
        self.print_bottom()

        # choice = input("\u001B[3A\u001B[50C")
        return input(f"\u001B[2A\u001B[{len(text) + self.tab + 2}C> ")





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


