from typing import (Optional,
                    List)

from dataclasses import dataclass
from .view import View

@dataclass
class Field_menu:

    f_text: Optional[str]=""
    f_value: Optional[str]=None

    def __str__(self):
        if self.f_value is not None:
            return f"{self.f_value} : {self.f_text}"
        else:
            return f"{self.f_text}"


class Menu(View):

    def __init__(self, header: str, choices: List[Field_menu], bodies: List[str]=[]):

        self.choices = choices
        new_bodies = list(bodies)
        new_bodies += ["\n".join(str(t) for t in choices)]

        super().__init__(header=header, bodies=new_bodies)

    def show(self):

        while True:
            try:
                # Show without closing the frame
                super().show(ended=False)

                # Ask question and check choice
                choice = self._ask_question("Selection")

                for elem in self.choices:
                    if elem.f_value == choice:
                        return choice

            except KeyboardInterrupt:
               break
