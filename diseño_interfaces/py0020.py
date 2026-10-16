while True:
    try:
        num = int(input('Introduce un numero entero: '))
        num2 = int(input('Introduce un numero entero: '))
        print('Menu')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('Introduce salir para salir')
        opcion = input('Introduce una opcion: ').strip().lower()

        if opcion == 'salir':
            break

        match opcion:
            case "1":
                sum = num + num2
                print(f"La suma es: {sum:.2f}")
            case "2":
                sum = num - num2
                print(f"La resta es: {sum:.2f}")
            case "3":
                sum = num * num2
                print(f"La multiplicacion es: {sum:.2f}")
            case "4":
                try:
                    sum = num / num2
                    print(f"La division es: {sum:.2f}")
                except ZeroDivisionError:
                    print(f"No se puede dividir entre 0")
            case _:
                print('Opcion no valida')
    except ValueError:
        print('Valor no valido')
        