lista = [10, 15 , 100, 40, 35, 353, 400, 40, 500, 420, 340, 115]
print("De menor a mayor")
print(sorted(lista, reverse=True))
print("No se mostrará el valor 40")
print([numero for numero in lista if numero != 40])
print("No se mostrarán valores mayores a 339")
print([numero for numero in lista if numero < 339])