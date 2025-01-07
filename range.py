"""
range(inicio, fin, paso)
"""
#con un solo elemento va a hacer una lista de 0 a 4
serie_1 = range(5)
print(list(serie_1))

#con dos elementos va a hacer una lista de 5 a 9
serie_2 = range(5,10)
print(list(serie_2))

#con tres elementos va a hacer una lista de 3 al 9 
#con pasos de 2 en 2
serie_3 = range(3,10,2)
print(list(serie_3))

#iterar los elementos con un for
for elemento in serie_3:
    print(elemento)
