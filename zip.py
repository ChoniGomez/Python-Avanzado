nombres = ["Paco", "Emilio", "Javier", "Ana"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

#unir dos listas 
#1er elemento de la lista unida con zip es ("Paco", "botero")
nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)

#deshacer los elementos unidos por zip 
#pero "Ana" se perdio al unir con zip
nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

#iterar la lista con zip
for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)
