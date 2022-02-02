
from view import View


class Menu(View):

    def __init__(self, title, choices):
        body = "\n".join(f"{val} : {key}" for key, val in choices.items())
        super().__init__(title=title, body=body)


    def show(self):
        super().show()

        choice = input("Selection ?")



