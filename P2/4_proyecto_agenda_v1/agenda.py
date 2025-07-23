

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
   print(".:: Sistema de agenda ::.. \n1.-  ➕Agregar  \n2.-  💥Mostrar \n3.-➗Cálcular Promedios \n4.- 💥SALIR ")
   opcion=input("Elige una opción (1-4): ") 
   return opcion   