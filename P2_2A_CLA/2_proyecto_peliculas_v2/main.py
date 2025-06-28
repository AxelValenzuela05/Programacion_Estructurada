#Crear un proyecto  que permita  gestionar (administrar películas); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar películas 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar dict  para almacenar  los siguentes atrivutos (nombre, categoria, clasificacion, genero,idioama de la película, )

import peliculas

opcion=True
while opcion:
    peliculas.borra_pantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n\n 1.- Crear \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar una caracteristica  \n 5.- Modificar caracteristica \n 6.- Borrar Caracterisitcas  \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crear_peliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrar_peliculas()
            peliculas.esperarTecla() 
        case "3":
            peliculas.mostrarPeliculas()   
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristcaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
            peliculas.esperarTecla()
            print("/n\tTerminaste la ejecucion del SW")
        case _:
            opsion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")