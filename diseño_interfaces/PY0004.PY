menu = ['Ensalada', 'Sopa', 'Pasta']
menuHoy = menu.copy()
menuHoy.extend(['Pescado', 'Postre'])
menuHoy.pop()
if "sopa" in menuHoy:
    menuHoy.remove("sopa")
menuHoy.reverse()
print("Lista 1 :")
print(menu)
print("Lista 2 :")
print(menuHoy)