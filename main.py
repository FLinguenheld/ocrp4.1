from .views.view import View

from .views.menu import (Menu, Field_menu)
# from views.form2 import (Form, Field_form)
from .views.form4 import (Form, Field_form, Field_form_List)

# itursiet



header = "Mon momument"


# my_menu = Menu(header=header,
#                choices=[Field_menu(f_text="Avancer",    f_value="A"),
#                         Field_menu(f_text="Reculer",    f_value="R"),
#                         Field_menu(),
#                         Field_menu(f_text="Manger",     f_value="1"),
#                         Field_menu(f_text="Dormir",     f_value="2"),
#                         Field_menu(),
#                         Field_menu(f_text="Quitter",    f_value="Q")],

#                bodies=["Choisissez\nune valeur !"])

# val = my_menu.show()

# my_simple_view = View(header=header, bodies=[f"Vous avez choisi : {val}"])
# my_simple_view.show()

# −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−



# Bonjour à tous saperlipopette


my_askings=[Field_form(f_name="Prenom",     f_type=str),
            Field_form(f_name="Nom",        f_type=str),
            Field_form(f_name="Age",        f_desc="(Nombre)", f_type=int),
            Field_form_List(f_name="Genre", f_desc="(Texte)",  f_type=str,   f_choices=["Masculin", "Féminin"]),
            Field_form_List(f_name="Nb de dents",              f_type=int,   f_choices=[5, 7, 9, 11, 13, 22])]

my_form = Form(header="Test formulaire",
               fields=my_askings,
               bodies=["Rentrez ces valeurs !"]
               )

my_form.show()


my_simple_view = View(header="Retour formulaire", bodies=["Vous avez rentré : ",
                                                          "\n".join(str(text) for text in my_askings)])
my_simple_view.show()


for i in range(10):
    print(i)

