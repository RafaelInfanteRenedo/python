def muestra_info(dni, /, *, nombre, apellido, edad):
    print("Persona con dni: ", dni, ", nombre: ", nombre, ", apellido: ", apellido, " y ", edad, " años");

muestra_info("48277048z", nombre="Manolo", apellido="Alberto", edad="20");