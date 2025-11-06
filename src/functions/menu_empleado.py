from .menus import (menu_gestion_informe,
                    menu_gestion_proyecto,
                    menu_gestion_registrotiempo)
from models.Empleado import Empleado

def menu_empleado(empleado: Empleado):
    """
    Muestra el menú principal para el rol de empleado.
    Permite gestionar informes y proyectos.
    """
    print("¡Bienvenido Empleado!")
    while True:
        print("--- OPCIONES DISPONIBLES ---\n")
        print("OPCIÓN 1. GESTIONAR INFORMES")
        print("OPCIÓN 2. GESTIONAR PROYECTOS")
        print("OPCIÓN 3. CERRAR SESIÓN\n")

        try: 
            opcion_user = int(input("Ingresar opción (1 - 3): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3):
            print("Debe ingresar una de las opciones disponibles (1 - 3) para continuar.")
            continue

        match opcion_user:
            case 1:
                menu_gestion_informe(empleado)

            case 2:
                menu_gestion_proyecto(empleado)

            case 3:
                print("Sesión cerrada exitosamente.")
                break
