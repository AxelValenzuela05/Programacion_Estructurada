
import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- modificar \n\t\t 4.- mostrar \n\t\t 5.- Buscar \n\t\t 6.- limpiar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminarpeliculas()
            peliculas.esperarTecla()   
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()   
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False   
            peliculas.esperarTecla() 
            print("Terminaste la ejecucion del SW")
        case _: 
            input("Opción invalida vuelva a intentarlo ... por favor")