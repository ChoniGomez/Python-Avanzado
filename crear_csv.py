import csv
import os

ruta = "csv_vacio.csv"
#ruta tomada desde la consola de python
ruta_absoluta = "C:\\Users\\MiEquipo\\Documents\\Python avanzado\\csv_vacio.csv"
#misma ruta pero con la libreria OS
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)

archivo_abierto = open(ruta_absoluta_os, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()
