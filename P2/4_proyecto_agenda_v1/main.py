#proyecto 3 
# Crear un proyecto que permita Gestionar (Administrar) calificaciones, colocar un menu de opciones para agregar, mostrar, calcular promedio calificaciones de un estudiante. 

#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo (modulos)
# 2.- Utilizar list (bidimensional) para almacenar el nombre del alumno, asi como sus tres calificaciones
#  

import agenda

def main():
    datos = []  

    opcion=True
    while opcion:
     agenda.borrarPantalla()
     opcion=agenda.menu_principal()

     match opcion:
        case "1":  
            agenda.agregar_calificaciones(datos)
            agenda.esperarTecla()
        case "2":
            agenda.mostrar_calificaciones(datos)
            agenda.esperarTecla() 
        case "3":
            agenda.calcular_promedios(datos)
            agenda.esperarTecla()   
        case "4":
            opcion=False    
            agenda.borrarPantalla()
            print(" Terminaste la ejecucion del SW")
        case _:
            opcion=True 
            print("Opción invalida vuelva a intentarlo") 
            agenda.esperarTecla()

if __name__ == "__main__":
    main()