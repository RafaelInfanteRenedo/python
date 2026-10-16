cadena = [1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4]
for i in range(len(cadena)):
    if i%2 == 0:
        if cadena[i] > 0:
            print("Indice: " + str(i) + ", precio antes: " + str(cadena[i]) + ", precio despues: " + str(cadena[i]*0.9))
    else:
        if cadena[i] > 0:
                    print("Indice: " + str(i) + ", precio antes: " + str(cadena[i]) + ", precio despues: " + str(cadena[i]*0.8))