"""
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
"""
import json
from punto_1 import *
def filtrar_por_tipo(servicios, tipo_seleccionado)->list:
    """
    filtra los servicios por el tipo seleccionado y devuelve una lista con los servicios filtrados.
    """
    servicios_filtrados = []
    for servicio in servicios:
        if servicio.get('tipo') == tipo_seleccionado:
            servicios_filtrados.append(servicio)
    return servicios_filtrados

def guardar_en_archivo(servicios:list, nombre_archivo:str):
    """
    guarda los servicios en un nuevo archivo JSON.
    """
    with open(nombre_archivo, 'w') as archivo:
        json.dump(servicios, archivo, indent=4, ensure_ascii=False)


servicios = cargar_archivo('data.json')
tipo_seleccionado = input("ingrese un tipo: ")
servicios_filtrados = filtrar_por_tipo(servicios, tipo_seleccionado)
guardar_en_archivo(servicios_filtrados, f'servicios_tipo_{tipo_seleccionado}.json')