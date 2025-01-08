def cacular_area_cuadrado(lado):
    """Calcula el área de un cuadrado al recibir la longitud del lado"""
    area = lado*lado
    return area


lado_cuadrados = [1, 3, 4]
area_cuadrados = []
for lado in lado_cuadrados:
    area = cacular_area_cuadrado(lado)
    area_cuadrados.append(area)

# ejecutar en consola de python
# python -m pdb area_cuadrado.py
# con la letra l lista la lineas de codigo
# con break 8 detiene la ejecucion del codigo en la linea 8 del codigo
# con continue, ejecuta el codigo hasta el siguiente breakpoint
# con next ejecuta la siguiente linea de codigo sin necesidad de definir un breakpoint
# con la letra q finaliza el modo debugging
# inspeccionar variable con el debugging
# display nombre_variable
# dejar de ver el contenido de la variable con el debugging
# undisplay nombre_variable
# restart reinicia el debugging