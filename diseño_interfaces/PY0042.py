lista1 = [1, 4, 5, 7, 9, 22, 45, 2845, 7, 10]
lista2 = [4, 6, 7, 8, 10, 45, 1233]
def listas(lista1, lista2):
    lista_def = list(filter(lambda x: x in lista1, lista2))
    return set(lista_def)
print("Elementos comunes: ", listas(lista1, lista2))