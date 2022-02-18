from copy import deepcopy
from typing import (Any,
                    Optional,
                    List,
                    Tuple)
from dataclasses import dataclass
from .view import View


@dataclass
class Field_form():
    f_name: str
    f_desc: str
    f_type: Any
    f_value: Any  # Usine à gaz pour passer en optional, autre solution ?

    def __str__(self):
        if self.f_value is None:
            return self.f_desc
        else:
            return f"{self.f_desc} : {self.f_value}"

    def question_text(self):
        return f"{self.f_desc} ({self.f_type})"

    def convert(self, value):
        return self.f_type(value)


@dataclass
class Field_form_List(Field_form):
    f_choices: List[Any]

    def question_text(self):
        return f"{self.f_desc} ({'/'.join(t for t in self.f_choices)})"

    def convert(self, value):
        val = super().convert(value)

        if val in self.f_choices:
            return val
        else:
            raise ValueError



class Form(View):
    def __init__(self, header: str, fields: List[Field_form], bodies: List[str]=[]):
        self.fields = fields
        self.bodies_base = bodies

        super().__init__(header=header, bodies=bodies)

    def _update_bodies(self):
        new_bodies = deepcopy(list(self.bodies_base))
        new_bodies += ["\n".join(str(f) for f in self.fields)]
        self.bodies = new_bodies

        super().show(ended=False)

    def show(self):

        while True:

            for field in self.fields:

                while True:

                    # Update bodies with new informations and show
                    self._update_bodies()

                    try :
                        field.f_value = field.convert(self._ask_question(field.question_text()))
                        break

                    except KeyboardInterrupt:
                        break
                    except ValueError:
                        continue

            self._update_bodies()
            if self._ask_confirmation():
                break

