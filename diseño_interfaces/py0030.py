inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}
copia_inventario = inventario_inicial.copy()
avisos = []
for venta in ventas:
    if venta in inventario_inicial:
        copia_inventario[venta]-=1
    else:
        copia_inventario.setdefault(venta, 0)
        copia_inventario[venta]-=1
        avisos.append("Venta añadida, código: " + venta)

for repo in reposiciones:
    if repo in copia_inventario:
        copia_inventario[repo]+=reposiciones[repo]

print("------ INFORME ------")
print("Numero de referencias: ", len(copia_inventario))
print("Unidades totales en stock: ", sum(inventario_inicial.values()))

stock0 = []
for ud in copia_inventario:
    if copia_inventario[ud] < 1:
        stock0.append(ud)

for st in stock0:
    copia_inventario.pop(st)
consulta = input("Introduce un código ")
correct = consulta in copia_inventario
if correct:
    print("Unidades en stock: ", copia_inventario[consulta])
else:
    print("No exixte")

print("Inventario original: ", inventario_inicial)
print("Inventario original: ", copia_inventario)

inventario_ordenado = sorted(copia_inventario.items(), key=lambda item: item[1])
dos = inventario_ordenado[:2]
print("Los elementos con más stock son: ", dos)