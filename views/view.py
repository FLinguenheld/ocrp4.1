import os
from .frame import(
        Justification,
        Frame)

class View:

    def __init__(self, header: str, bodies: list[str]):
        self.frame = Frame()
        self.title = header.upper()
        self.bodies = bodies

    def show(self, ended: bool=True):
        """ Clear the terminal, print header and all bodies. Close the frame if ended=True """

        # Clear screen
        os.system("cls" if os.__name__ == "nt" else "clear")

        # Header
        self.frame.print_top()
        self.frame.print_text(self.title, Justification.CENTER)
        self.frame.print_line()
        self.frame.print_blank_line()

        # Bodies
        for b in self.bodies:
            self.frame.print_text(b, Justification.LEFT)
            self.frame.print_blank_line()

        if ended:
            self.frame.print_bottom()

    def _ask_question(self, text: str):
        """ Finish the frame with a prompt. Return user's value without any check """

        self.frame.print_line()
        self.frame.print_text(text, Justification.LEFT)
        self.frame.print_bottom()

        # Print input then replace the cursor
        return input(f"\u001B[2A\u001B[{len(text) + self.frame.tab + 2}C> ")

    def _ask_confirmation(self, text: str="Confirmer ? (O/N)"):
        """ Finish the frame with a confirmation, return a bool """
        
        while True:
            match self._ask_question(text).upper():
                case "O":
                    return True
                case "N":
                    return False

# suit
