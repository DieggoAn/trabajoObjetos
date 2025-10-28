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
        print("OPCIÓN 1. GESTIONAR REGISTROS DE TIEMPO")
        print("OPCIÓN 2. GESTIONAR INFORMES")
        print("OPCIÓN 3. GESTIONAR PROYECTOS")
        print("OPCIÓN 4. CERRAR SESIÓN\n")

        try: 
            opcion_user = int(input("Ingresar opción (1 - 4): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4):
            print("Debe ingresar una de las opciones disponibles (1 - 4) para continuar.")
            continue

        match opcion_user:
            case 1:
                menu_gestion_registrotiempo(empleado)

            case 2:
                menu_gestion_informe(empleado)

            case 3:
                menu_gestion_proyecto(empleado)

            case 4:
                print("Sesión cerrada exitosamente.")
                break
