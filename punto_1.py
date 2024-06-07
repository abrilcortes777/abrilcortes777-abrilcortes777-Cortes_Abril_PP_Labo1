"""
El programa contará con el siguiente menú:
1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
servicios.
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
7) Salir.
nota: el código deberá tener comentarios con la documentación de cada una de las funciones y
respetar las reglas de estilo de la cátedra.
nota bis: separar las funciones en distintas bibliotecas.
"""
import json
def cargar_archivo(extension:str)->list:
    """
    la funcion imprime el contenido del archivo y retorna una lista correspondiente al contenido.
    Si el archivo no existe, la funcion imprime un mensaje de error y devuelve False.
    """
    try:
        archivo = open(extension, 'r+')
        contenido = json.load(archivo)
        #if contenido:
                #print(contenido)
        return list(contenido)
    except FileNotFoundError:
        print("no existe ese archivo")
        return False
    
#contenido = cargar_archivo('data.json')
