from datetime import date
def agregar(desc, registro=None, usuario="Sistema"):
    if (registro is None):
        registro = []

    tarea = {"descipcion":desc, "fecha": date.today(), "usuario":usuario}
    registro.append(tarea)
    return registro

registrado = agregar("Lavar los platos", usuario="Nacho")
agregar("Poner la mesa", registrado, usuario="Monica")
agregar("Sacar la basura", registrado, usuario="Petunia")
agregar("Hacer la cama", registrado, usuario="Alejandro")
print(registrado)

if __name__ == "__main__":
    registro_jorge = agregar("añado envio sms", usuario="jorge")
    registro_jorge = agregar("corrijo envio sms", registro_jorge, usuario="jorge")

    registro_ana = agregar("corrijo bug1", usuario="Ana")
    registro_ana = agregar("corrijo bug2", registro_ana, usuario="Ana")

    print(registro_jorge)
    print(registro_ana)