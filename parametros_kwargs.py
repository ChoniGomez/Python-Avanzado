def funcion_kwargs(**kwargs):
    #imprimir los parametros que recibe (diccionario)
    print(kwargs)
    #recorrer el diccionario que recibe
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")
    print(kwargs["nombre"], kwargs["apellido"])


funcion_kwargs(nombre="choni", apellido="jeje")
