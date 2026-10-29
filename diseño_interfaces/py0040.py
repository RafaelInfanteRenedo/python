import math
radio = float(input("Introduce el radio"))
def area(num):
    r_cuadrado = lambda num:num**2
    area = math.pi*r_cuadrado(num)
    return area
print(f"El area es: {area(radio):.2f}")