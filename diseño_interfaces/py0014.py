try:
    num1 = float(input('Introduce un número: '))
    num2 = float(input('Introduce otro número: '))
    num3 = float(input('Introduce otro número: '))
    sum = float(num1*0.15 + num2*0.35 + num3*0.5)
    print('La suma ponderada es:', sum)
except ValueError:
    print('Valor no valido')