lista_inicial = [6, 1, 8, 7, 3, 2, 4, 9, 5]
def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares = sorted(pares)
    impares=sorted(impares)
    return pares, impares
lista_pares = []
lista_impares=[]
lista_pares, lista_impares = separar(lista_inicial)
print(lista_pares)
print(lista_impares)