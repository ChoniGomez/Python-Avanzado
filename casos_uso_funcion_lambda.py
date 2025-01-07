lista_numeros = [1,2,3,4,5,6,7,8]

#en filter paso como argumento una funcion lambda
lista_pares = list(filter(lambda numero: numero % 2 == 0, lista_numeros))
print(lista_pares)

#map recorre toda la lista
nueva_lista = list(map(lambda numero: numero * 10, lista_numeros))
print(nueva_lista)
