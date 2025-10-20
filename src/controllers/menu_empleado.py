from .menus import (menu_gestion_emp,
                       menu_gestion_depto,
                       menu_gestion_informe,
                       menu_gestion_proyecto)
from models.Empleado import Empleado

def menu_empleado(empleado: Empleado):
    """
    Muestra el menú principal para el rol de empleado.
    Permite gestionar empleados, departamentos, informes y proyectos.
    """
    print("¡Bienvenido Empleado!")
    while True:
        print("--- OPCIONES DISPONIBLES ---\n")
        print("OPCIÓN 1. GESTIONAR EMPLEADOS")
        print("OPCIÓN 2. GESTIONAR DEPARTAMENTOS")
        print("OPCIÓN 3. GESTIONAR INFORMES")
        print("OPCIÓN 4. GESTIONAR PROYECTOS")
        print("OPCIÓN 5. CERRAR SESIÓN\n")

        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                menu_gestion_emp(empleado)

            case 2:
                menu_gestion_depto()

            case 3:
                menu_gestion_informe(empleado)

            case 4:
                menu_gestion_proyecto(empleado)

            case 5:
                print("Sesión cerrada exitosamente.")
                break

