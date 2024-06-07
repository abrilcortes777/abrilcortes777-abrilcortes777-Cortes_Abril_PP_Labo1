"""
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
"""
from punto_1 import *
def asignar_totales(datos):
    for servicio in datos:
        servicio['totalServicio'] = lambda servico_ind: float(servico_ind['cantidad']) * \
        float(servico_ind['precioUnitario'])
    return datos
"""lista = cargar_archivo('data.json')
datos_con_totales = asignar_totales(lista)
print(datos_con_totales)"""