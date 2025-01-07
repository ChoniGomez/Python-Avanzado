def separar_par_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

#convertir esta funcion a lambda
def calcular_area_cuadrado(lado):
    return lado ** 2

#funcion lambda asignada a una variable
calcular_cuadrado = lambda lado: lado ** 2
print(calcular_cuadrado(2))
