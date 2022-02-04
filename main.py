from views.view import View
from views.menu import Menu


header = "Mon momument"


my_menu = Menu(header=header, choices={"La tour Eiffel":0, "Montparnasse":1, "Mont St Michel": 2})
val = my_menu.show()

# Pourquoi utiliser le dico à l'envers avec la valeur en clef ?
my_simple_view = View(header=header, body=[f"Vous avez choisi : {val}"])
my_simple_view.show()




