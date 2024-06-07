"""
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
"""
from punto_5 import *
def guardar_archivo(nombre:str,contenido:str):
    """
    la funcion intenta crear el archivo con el nombre ingresado como parametro
    y escribir el contenido(parametro) en él. 
    Si la operacion es exitosa, imprime un mensaje de que se ha creado el archivo y retorna True. 
    Si ocurre algun error durante el proceso, imprime un mensaje de error y retorna False.
    """
    try:
        with open(nombre, 'w') as archivo:
            json.dump(servicios, archivo, indent=4)
            print(f"Se creo el archivo: {nombre}")
            return True
    except Exception:
        print(f"Error al crear el archivo: {nombre}")
        return False
servicios = cargar_archivo('data.json')
servicios_ordenados = ordenar_asc_desc(servicios, "asc")
guardar_archivo('servicios_ordenados.json', servicios_ordenados)
