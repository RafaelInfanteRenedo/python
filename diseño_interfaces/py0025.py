linea = "######################################################################"
contador = 0
lista = ["España", "Argentina", "Perú", "Bolivia", "Chile"]
while True:
    try:
        print("MENÚ. Elija una de las siguientes opciones marcando su número:")
        print("1. Imprimir alfabéticamente en orden ascendente")
        print("2. Imprimir alfabéticamente en orden descendente")
        print("3. Añadir País")
        print("4. Eliminar Pais")
        print("5. Salir")
        contador+=1
        opcion = int(input("Introduce una opción; "))
        opcion = opcion
        if opcion > 0 and opcion < 6:
            match opcion:
                case 1:
                    print(sorted(lista))
                    print(linea)
                    print("\n\n")
                case 2:
                    print(sorted(lista, reverse=True))
                    print(linea)
                    print("\n\n")
                case 3:
                    pais = input("Introduce un pais para añadir: ")
                    lista.append(pais)
                    print("Pais añadido.")
                    print(linea)
                    print("\n\n")
                case 4:
                    pais = input("Introduce un pais para eliminar: ")
                    if pais in lista:
                        lista.remove(pais)
                        print("Pais eliminado.\n")
                        print(lista)
                        print("\n\n")
                    else:
                        print("Ese pais no esta en la lista")
                case 5:
                    break
        else:
            print("Número no válido")

    except ValueError:
        print("Valor no válido")
    print("El numero de veces que se ha mostrado el menu es: " + str(contador))