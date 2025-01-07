def calcular_perimetro(*args):
    #imprimir los valores que recibe
    print(args)
    perimetro = 0
    #recorre todos los valores que recibe para calcular el perimetro
    for lado in args:
        perimetro += lado
    return perimetro


perimetro = calcular_perimetro(1,2,3,4)
print(perimetro)

triangulo = calcular_perimetro(1,2,3)
print(triangulo)
