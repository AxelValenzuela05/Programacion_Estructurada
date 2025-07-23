"""
list (array)
son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

Nota: sus valores si son modificables 

la lista es una coleccion ordenada y modificable. permite miembros duplicados

"""

import os 
os.system('cls')

#Funciones mas comunes en las listas 

paises=["mexico","brasil","españa","canada"]

numeros=[23,12,100,34]

varios=["Hola",True,33,3.12]

#Como ordenar las listas

print(numeros)
print(paises)
print(varios)

numeros.sort()
print(numeros)
paises.sort()
print(paises)

#agregar o insertar o añadir un elemento a la lista
#1er forma
print(paises)
paises.append("honduras")
print(paises)

#2da forma
paises.insert(1,"honduras")
print(paises)

#eliminar o borrar o suprimir un elemento a la lista
#1er forma
paises.sort()
print(paises)
paises.pop(4)
print(paises)

#2da forma
paises.remove("honduras")
print(paises)


#Buscar un eleemento dentro de una lista

print("brasil" in paises)

#Contar el numero veces que un elemento esta dentro de una lista


print(numeros)
print(numeros.count(12))
numeros.insert(1,12)
print(numeros)
print(numeros.count(101))

#Dar la vuelta a los elementos de una lista
print(paises)
print(numeros)
print(paises.reverse())
print(numeros.reverse())
print(numeros)
print(paises)

#conocer el indice o la posicion de un valor de la lista
posiscion=paises.index("españa")

#Unir el contenido de 2 o mas listas en una sola
numeros2=[300,500,100]


print(numeros)
print(numeros2)
numeros.extend(numeros2)
print(numeros)

paises.extend(numeros2)
print(paises)

