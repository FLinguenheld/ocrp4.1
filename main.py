from menu import Menu

# my_view = View(title="mon momument", body="la tour Eiffel\nMontparnasse\nMont St Michel")
# my_view.show()


my_menu = Menu(title="Mon momument !!!", choices={"La tour Eiffel":0, "Montparnasse":1, "Mont St Michel": 2})
val = my_menu.show()

print(val)

