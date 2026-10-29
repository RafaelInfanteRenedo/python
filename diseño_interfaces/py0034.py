def menu_pizza():
    pizzas = {"Margarita" : 8, "Cuatro quesos": 12.5, "Pepperoni" : 10}
    while True:
        ind = 1
        
        opcion = input("¿Le gustaria añadir alguna pizza? si/no: ").lower()
        
        if opcion == "si":
            
            nombre_pizza = input("Introduzca el nombre de la pizza: ").title()
            
            try:
                precio_pizza = float(input("Introduzca el precio de la pizza: "))
                pizzas.update({nombre_pizza:precio_pizza})
            except ValueError:
                print("El precio introducido no es valido")        
        else:
            break
        pizzas_ordenadas = sorted(pizzas.items(), key=lambda item: (item[1], item[0]))

        for ind, (nombre, precio) in enumerate(pizzas_ordenadas, start=1):
            print(ind, ".", nombre, "-", precio)
    return pizzas
print(menu_pizza())