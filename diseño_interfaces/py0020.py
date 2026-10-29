def sumar(num1, num2):
    sum = num1 + num2
    return sum
    
def restar(num1, num2):
    resta = num1 - num2
    return resta
    
def multiplicar(num1, num2):
    multi = num1*num2
    return multi
    
def division(num1, num2):
    try:
        return num / num2
    except ZeroDivisionError:
        print(f"No se puede dividir entre 0")
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
                print(sumar(num, num2))
            case "2":
                print(restar(num, num2))
            case "3":
                print(multiplicar(num, num2))
            case "4":
                print(division(num, num2))
            case _:
                print('Opcion no valida')

    except ValueError:
        print('Valor no valido')