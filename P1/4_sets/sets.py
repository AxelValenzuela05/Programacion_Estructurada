"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")
#crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

emails=[]
while True:
    email = input("Ingrese el mail del alumno (o 'salir' para terminar): ")
    if email.lower( ) == 'salir':
        break
    if email not in emails:
        emails.append(email)
    else:
        print("El email ya esta en la lista. ")





  



