from .view import View
# from frame import Justification

class Menu(View):

    def __init__(self, header, choices):
        body = ["\n".join(f"{val} : {key}" for key, val in choices.items())]
        super().__init__(header=header, body=body)

        self.choices = choices

    def show(self):

        while True:
            try:
                super().show(False)

                choice = int(self.frame.print_question("Selection"))
                if choice in self.choices.values():
                    return choice

            except KeyboardInterrupt:
               raise KeyboardInterrupt 
            except:
                continue
