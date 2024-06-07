"""
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
"""
from punto_1 import *
from copy import deepcopy
def ordenar_asc_desc(lista:list,orden:str)->list:
    """
    la funcion toma una lista y un parametro que 
    indica el orden (ascendente o descendente) y retorna una la lista ordenada.
    """
    lista_a_ordenar = deepcopy(lista)
    for i in range(len(lista_a_ordenar) - 1):
        for i in range(len(lista_a_ordenar) - 1):
            for j in range(i + 1, len(lista_a_ordenar)):
                if orden == "asc":
                    if lista_a_ordenar[i]["descripcion"] > lista_a_ordenar[j]["descripcion"]:
                        lista_a_ordenar[i], lista_a_ordenar[j] = lista_a_ordenar[j], lista_a_ordenar[i]
                elif orden == "desc":
                    if lista_a_ordenar[i]["descripcion"] < lista_a_ordenar[j]["descripcion"]:
                        lista_a_ordenar[i], lista_a_ordenar[j] = lista_a_ordenar[j], lista_a_ordenar[i]
    return lista_a_ordenar
servicios = cargar_archivo('data.json')
lista_ordenada = ordenar_asc_desc(servicios,"asc")
for servicio in servicios:
     print(servicio['descripcion'])
