"""
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
servicios.
"""
from punto_1 import *
def imprimir_pot_col(datos:list):
    """
    la funicon tomara una lista con los datos que se quieran formatear a tabla.
    se obtendran el  nombre de las columnas con las keys.
    se printeara una tabla con losa datos de la lista.
    """
    contenido = cargar_archivo('data.json')
    columnas = contenido[0].keys()
    tabla = [columnas]
    print(" / ".join(columnas))
    for dato in datos:
        fila = []
        for columna in columnas:
            fila.append(dato.get(columna))
        tabla.append(fila)
        print(" / ".join(fila))
#lista = cargar_archivo('data.json')
#imprimir_pot_col(lista)