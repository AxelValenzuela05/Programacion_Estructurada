peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t...Oprime cualquier tecla para continuar... ")
    
def agregarPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar peliculas ::.\n")
    peliculas.append(input("Ingrese el nombre ").upper().strip())
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def consultarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o mostrar peliculas ::. \n")
    if len(peliculas)>0:
        for i in range (0,len (peliculas)):
            print(f"\t(i+1): (peliculas[i])")   
    else:
        print("\n\t .:: No ha peliculas en el sistema en este momento ::.")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t.:: Vaciar o quitar TODAS las peliculas ::.")
    resp=input("¿Deseas quitar TODAS las peliculas del sistema? (Si/No)").lower().strip()
    if resp=="si":
        peliculas.clear()
        input("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar Peliculas::. \n")
    pelicula_buscar=input("ingrese el nombre de la pelicula a buscar: ").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t ¡No se encontro la pelicula!")
    else:
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula{pelicula_buscar} si la tenemos en la casilla {i+1}")
                encontro+=1
        print(f"\n Tenemos {encontro} pelicula(s) con este titulo")
        print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")       

def eliminarPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar Peliculas::. \n")
    pelicula_buscar=input("ingrese el nombre de la pelicula a borrar: ").upper().strip()
    encontro=0
    if not (pelicula_buscar in peliculas):
        print("\n\t ¡No se encontro la pelicula!")
    else:
        resp="si"
        while pelicula_buscar in peliculas and resp=="si":
            resp=input("¿Deseas borrar la pelicula del sistema? (Si/No) ")
            if resp=="si":
                posicion=peliculas.index(pelicula_buscar)
                print(f"La pelicula que se borro es: {pelicula_buscar} y estaba en la casilla {posicion+1}")
                peliculas.remove(pelicula_buscar)
                encontro+=1
                print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
    print(f"\n\t Se borro { encontro} pelicula(s) con este titulo")





