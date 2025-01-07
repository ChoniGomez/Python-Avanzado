lista_nombres = ["Paco", "Emilio", "Javier", "Ana"]

for nombre in lista_nombres:
    print(nombre)
    if nombre == "Javier":
        break #aca se rompe el ciclo for y else no se ejecuta
else:
    print("Ciclo terminado")
