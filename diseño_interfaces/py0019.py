num = input('Introduce un número entero: ')
try:
    num = int(num)
    while num%2 == 0:
        num = input('Introduce un número entero: ')
        num = int(num)
except ValueError:
    print('Valor no valido')