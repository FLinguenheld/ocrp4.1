import os
from frame import(
        Justification,
        Frame)

class View:

    def __init__(self, header: str, body: list):
        self.frame = Frame()
        self.title = header.upper()
        self.body = body

    def show(self, ended: bool=True):

        # Clear screen
        os.system("cls" if os.__name__ == "nt" else "clear")

        # Header
        self.frame.print_top()
        self.frame.print_text(self.title, Justification.CENTER)
        self.frame.print_line()
        self.frame.print_blank_line()

        # Body
        for b in self.body:
            self.frame.print_text(b, Justification.LEFT)
            self.frame.print_blank_line()

        if ended:
            self.frame.print_bottom()
