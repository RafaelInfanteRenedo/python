lista = []
lista = [n*n for n in range(1, 20)]
print("Lista con los cuadrados de los números del 1 al 20")
print(lista)
lista = [n for n in lista if n % 2 != 0]
print("Lista anterior solo con números impares")
print(lista)