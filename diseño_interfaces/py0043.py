cadena = input('Introduce una frase: ')

cadena2 = cadena.lower().replace(" ", "")
cadena3 = []
for char in cadena2:
    if char not in cadena3:
        numero = cadena2.count(char)
        print("El caracter " + char +  " se repite " + str(numero) + " veces")
        cadena3.append(char)