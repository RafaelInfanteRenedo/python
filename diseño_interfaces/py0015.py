matriz = [
   [1, 1, 1, 3],
   [2, 2, 2, 7],
   [3, 3, 3, 9],
   [4, 4, 4, 13] ]

for list in matriz:
    if list[0] + list[1] + list[2] == list[3]:
        print(str(list) + "se cumple la condicion")
    else:
        list[3] = sum(list[0:3])
print(matriz)