from punto_1 import *
from punto_2 import*
from punto_3 import *
from punto_4 import *
from punto_5 import*
from punto_6 import*
while True:
    print("1 Cargar archivo"
            "\n2 Imprimir lista"    
            "\n3 Asignar totales"   
            "\n4 Filtrar por tipo"
            "\n5 Mostrar servicios:"
            "\n6 Guardar servicios"
            "\n7 Salir")
    opcion = input("Opcion: ")
    if opcion == '1':
        contenido = cargar_archivo('data.json')
    if opcion == '2':
        lista = cargar_archivo('data.json')
        imprimir_pot_col(lista)
    if opcion == '3':
        lista = cargar_archivo('data.json')
        datos_con_totales = asignar_totales(lista)
        print(datos_con_totales)
    if opcion == '4':
        servicios = cargar_archivo('data.json')
        tipo_seleccionado = input("ingrese un tipo: ")
        servicios_filtrados = filtrar_por_tipo(servicios, tipo_seleccionado)
        guardar_en_archivo(servicios_filtrados, f'servicios_tipo_{tipo_seleccionado}.json')
    if opcion == '5':
        servicios = cargar_archivo('data.json')
        lista_ordenada = ordenar_asc_desc(servicios,"asc")
        for servicio in servicios:
            print(servicio['descripcion'])
    if opcion == '6':
        servicios = cargar_archivo('data.json')
        servicios_ordenados = ordenar_asc_desc(servicios, "asc")
        guardar_archivo('servicios_ordenados.json', servicios_ordenados)
    if opcion == '7':
        break