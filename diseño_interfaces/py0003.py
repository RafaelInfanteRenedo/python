cadena = []
while True:
    nombre = input("Introduce un nombre o 'fin' para terminar: ")
    if nombre.lower()=="fin":
        break
    else:
        cadena.append(nombre)
nombreusuario = input("Introduce un nombre ")
numveces = cadena.count(nombreusuario)
print("El nombre " + nombreusuario + " se repite " + str(numveces) + " veces")
print("El nombre " + nombreusuario + " se encuentra en la posicion " + str(cadena.index(nombreusuario)))
cadena.remove(cadena[cadena.index(nombreusuario)])
print("El nombre " + nombreusuario + " se ha eliminado de la lista")
vip = input("Introduce un nombre VIP ")
cadena.insert(0, vip)
print("Se ha interdado el nombre VIP " + vip + " en la primera posicion de la lista")
print("Los nombres introducidos son: " + str(cadena))