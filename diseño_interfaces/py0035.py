def suma_n_numeros(*args):
    suma=0
    if len(args) > 0:
        for i in args:
            suma+=i
    else:
        suma=0
    return suma
print(suma_n_numeros(2,2,2,2,2,2,2,2,2,2,40))

def suma_n_enteros(*args):
    suma=0
    if len(args) > 0:
        for i in args:
            if isinstance(i, int):
                suma+=i
            else:
                print(f"{i} no es un numero entero y no se suma")
    return suma
print(suma_n_enteros(2,2,2,2,2.8,2,"Buenas tardes",2,2,2,40))

def suma_dos_o_mas_numeros(num1, num2, *args):
    suma=0
    suma = num1+num2
    for i in args:
        try:
            suma+=int(i)
        except:
            print(f"{i} no es entero y no se ha sumado, modificalo para que lo sea")
    return suma
print(suma_dos_o_mas_numeros(2,2,2,2,2.8,2,"Buenas tardes",2,2,2,40))