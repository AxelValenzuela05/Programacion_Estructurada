import funciones
from usuarios import usuario
from registros import registro
from consultas import consulta
from modificaciones import modificaciones
import getpass

def main():
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        opcion = funciones.menu_usuarios()

        if opcion == "1" or opcion.upper() == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t📝 ..:: Registro de Usuario en el Sistema de la Tiendita ::..")
            nombre = input("\t¿Cual es tu nombre?: ").upper().strip()
            apellidos = input("\t¿Cuales son tus apellidos?: ").upper().strip()
            email = input("\tIngresa tu email: ").lower().strip()
            password = getpass.getpass("\tIngresa tu contraseña: ").strip()

            regresar = usuario.registrar(nombre, apellidos, email, password)
            if regresar:
                print(f"\n✅ {nombre} {apellidos} se registró correctamente con el e-mail: {email}")
            else:
                print("\n❌ No fue posible realizar el registro. Intenta de nuevo.")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "LOGIN":
            funciones.borrarPantalla()
            print("\n\t🔐 ..:: Inicio de Sesión - Tiendita ::.. ")
            email = input("\tIngresa tu E-mail: ").lower().strip()
            password = getpass.getpass("\tIngresa tu contraseña: ").strip()

            lista_usuario = usuario.iniciar_sesion(email, password)

            if lista_usuario:
                nombre, apellidos, email = lista_usuario[:3]
                print(f"\n✅ Bienvenido {nombre} {apellidos} al sistema de la Tiendita 🛒")
                funciones.esperarTecla()
                menu_sistema()  # Este ya debe ser el nuevo menú de productos/ventas
            else:
                print("\n❌ El E-mail y/o contraseña son incorrectos.")
            funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "ELIMINAR USUARIO":
            funciones.borrarPantalla()
            print("\n\t🗑️ ..:: Eliminar Usuario ::..")
            email = input("\tE-mail a eliminar: ").lower().strip()
            password = getpass.getpass("\tConfirma tu contraseña: ").strip()

            confirmado = input("\n⚠️ ¿Estás seguro que deseas eliminar este usuario? (s/n): ").strip().lower()
            if confirmado == "s":
                if usuario.eliminar_usuario(email, password):
                    print("\n✅ Usuario eliminado exitosamente.")
                else:
                    print("\n❌ No se pudo eliminar el usuario. Verifica tus datos.")
            else:
                print("\n🔄 Operación cancelada.")
            funciones.esperarTecla()

        elif opcion == "4" or opcion.upper() == "SALIR":
            print("\n🚪 Terminó la ejecución del sistema.")
            opcion = False
            funciones.esperarTecla()

        else:
            print("\n❌ Opción no válida.")
            funciones.esperarTecla()



def menu_sistema():
    while True:
        funciones.borrarPantalla()
        print("\n\t🛒..::: SISTEMA PRINCIPAL TIENDITA :::..🛒\t\n")
        print("\n\t..::: Miscelánea ''El Guero'' :::..\t\n")
        print("1️⃣\t 🧾 Ir al menú de Productos 🧾")
        print("2️⃣\t 💰 Ir al menú de Ventas 💰")
        print("3️⃣\t 🚪 Salir del sistema 🚪\n")

        opcion = input("👉\t Elige una opción: ").strip()

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_ventas()
        elif opcion == "3":
            funciones.borrarPantalla()
            print("\n🎉\t Gracias por usar el sistema de la tiendita. ¡Hasta pronto!\n")
            break
        else:
            input("❌\t Opción inválida. Intenta de nuevo...")



def menu_productos():
    while True:
        funciones.borrarPantalla()
        print("\n\t📦..::: MENÚ DE PRODUCTOS :::..📦\n")
        print("1️⃣\t Agregar nuevo producto")
        print("2️⃣\t Reabastecer stock")
        print("3️⃣\t Editar producto")
        print("4️⃣\t Inventario")
        print("5️⃣\t 🔙 Volver al menú principal 🔙")

        opcion = input("👉\t Elige una opción: ").strip()

        match opcion:
            case "1":
                registro.agregarProducto()
                funciones.esperarTecla()
            case "2":
                modificaciones.reabastecerStock()  # Nueva función para aumentar stock
                funciones.esperarTecla()
            case "3":
                modificaciones.editarProducto()
                funciones.esperarTecla()
            case "4":
                consulta.consultarInventario()
                funciones.esperarTecla()
            case "5":
                break
            case _:
                input("❌\t Opción inválida. Intenta de nuevo...")




def menu_ventas():
    while True:
        funciones.borrarPantalla()
        print("\n\t💰..::: MENÚ DE VENTAS :::..💰\n")
        print("1️⃣\t Registrar nueva venta")
        print("2️⃣\t Consultar ventas por día")
        print("3️⃣\t Consultar ventas por producto")
        print("4️⃣\t 🔙 Volver al menú principal 🔙")

        opcion = input("👉\t Elige una opción: ").strip()

        match opcion:
            case "1":
                registro.registrarVenta()
                funciones.esperarTecla()
            case "2":
                consulta.consultarVentasPorDia()
                funciones.esperarTecla()
            case "3":
                consulta.consultarVentasPorProducto()
                funciones.esperarTecla()
            case "4":
                break
            case _:
                input("❌\t Opción inválida. Intenta de nuevo...")



if __name__ == "__main__":
    main()

