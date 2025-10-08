from functions import (menu_gestion_emp,
                       menu_gestion_depto,
                       menu_gestion_informe,
                       menu_gestion_proyecto)

def menu_admin():
    """
    Muestra el menú principal para el rol de administrador.
    Permite gestionar empleados, departamentos, informes y proyectos.
    """
    print("¡Bienvenido administrador!")
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
                menu_gestion_emp()

            case 2:
                menu_gestion_depto()

            case 3:
                menu_gestion_informe()

            case 4:
                menu_gestion_proyecto()

            case 5:
                print("Sesión cerrada exitosamente.")
                break

        