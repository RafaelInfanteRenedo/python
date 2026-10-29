abuelo, abuela, primo, tio = 3, 7, 8, 20
def nicoteta(tio, /, abuelo, abuela, *, primo):
    return "Valor abuelo: ", abuelo, " / valor abuela: ", abuela, " Tu primo y tio: ", primo, tio

print(nicoteta(tio, abuelo, abuela, primo=40))
