from copy import deepcopy

from .view import View
from enum import Enum


class Format(Enum):
    STR = 0
    INT = 1
    UINT = 2
    LIST = 3

def test():

    for i in range(10):
        print(i)


class Field:

    def __init__(self, text: str, format: Format, possibilities: list[str]=[]):

     self.text = text
     self.format = format
     self.possibilities = possibilities
     self.value = ""                     # Easier than None to print

    def __str__(self):
        return f"{self.text} : {self.value}"


class Form(View):

    def __init__(self, header: str, bodies: list[str], fields : list[Field]):

        super().__init__(header=header, bodies=bodies)
        self.fields = fields
        self.base_bodies = bodies

    def show(self):
        """ Build bodies with fields and ask to user to fill.
            Ask a confirmation and leave """

        while True :

            self._fill_form()

            # Confirm ?
            self._rebuild_bodies()
            if self._ask_confirmation():
                break
            else:
                self._reset_values()



    def _fill_form(self):
        """ Loop in fields to fill one by one according to formats """

        for my_field in self.fields:

            while True:
                try:

                    # Update screen
                    self._rebuild_bodies()



                    # Ask
                    if my_field.format == Format.LIST:
                        question = f"{my_field.text} ({' / '.join(my_field.possibilities)}) ?"
                    else:
                        question = f"{my_field.text} ?"

                    user_value = (self._ask_question(question))
                    self._checkValue(user_value, my_field)

                    # Set
                    my_field.value = user_value
                    break

                except KeyboardInterrupt:
                    raise KeyboardInterrupt
                except:
                    continue


            # TreeSitter trouve sale de ne pas utiliser un set :|
            # Il n'aime pas non plus le "any"

            # Utiliser le try de cette manière -> accadémique ?
            # Idem pour le while True ?


    def _rebuild_bodies(self):
        """ Copy bodies, add fields underneath, then show() """

        new_bodies = deepcopy(self.base_bodies)
        new_bodies += ["\n".join(f"{field.text} : {field.value}" for field in self.fields)]
        self.bodies = new_bodies
        super().show(False)

    def _reset_values(self):
        """ Loop in self.fields to erase value """

        for f in self.fields:
            f.value = ""

    def _checkValue(self, value: any, field: Field):
        """ Try to cast value according to its format, raise an error if needed """

        match field.format:

            case Format.STR:                # Check with regex ?
                if not value:
                    raise ValueError
                else:
                    return value

            case Format.INT:
                return int(value)

            case Format.UINT:
                val = int(value)

                if val < 0:
                    raise ValueError
                else:
                    return val

            case _:
                if (value in field.possibilities):
                    return value
                else:
                    raise ValueError

