"""
enumerate(iterable, start=0)

si no se pasa el parametro start, comienza la cuenta en 0
"""

nombres = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = enumerate(nombres, start=5)
print(list(nombres_enumerados))

#recorrer un zip con un ciclo for
for indice, elemento in enumerate(nombres):
    print(indice, elemento)
