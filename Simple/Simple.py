from operator import itemgetter
import random

def crear_lista_diccionario():
    lista = []
    nuevo = {}
    for i in range(1, 11):
        nuevo = {'id': i, 'edad':random.randint(0,100)}
        lista.append(nuevo)
    return lista

edades = crear_lista_diccionario()
print(edades)

def ordenar_lista(listado):
    listado = sorted(listado, key =itemgetter('edad'))
    print("El id de la persona mas joven es", listado[0]["id"])
    print("El id de la persona mas vieja es", listado[9]["id"])
    return listado

edades = ordenar_lista(edades)
print(edades)