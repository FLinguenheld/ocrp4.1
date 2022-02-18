from copy import deepcopy
from typing import (Any,
                    Optional,
                    List,
                    Tuple)
from dataclasses import dataclass
from .view import View


@dataclass
class Field_form:

    f_name: str
    f_desc: str
    f_type: Any
    f_choices: Optional[List[Any]]=None  # Impossible de mettre une liste vide ?
    f_value: Optional[Any]=None

    def __str__(self):
        if self.f_value is None:
            return self.f_desc
        else:
            return f"{self.f_desc} : {self.f_value}"

    def question_text(self):
        if self.f_choices is None:
            return f"{self.f_desc} ({self.f_type})"
        else:
            # return f"{self.f_desc} ({self.f_choices})"
            return f"{self.f_desc} ({'/'.join(t for t in self.f_choices)})"


class Form(View):
    def __init__(self, header: str, fields: List[Field_form], bodies: List[str]=[]):

        self.fields = fields
        self.bodies = bodies

        super().__init__(header=header, bodies=bodies)


    def _update_show(self):
        new_bodies = deepcopy(list(self.bodies))
        new_bodies += ["\n".join(str(f) for f in self.fields)]
        self.bodies = new_bodies
        super().show(ended=False)


    def show(self):

        for field in self.fields:


            while True:

                self._update_show()

                try :
                    field.f_value = field.f_type(self._ask_question(field.question_text()))
                    break

                except KeyboardInterrupt:
                    break
                except ValueError:
                    continue


