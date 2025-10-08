import mysql.connector

conexion1 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="backend_proyecto")

cursor1 = conexion1.cursor()

def menu_gestion_emp():
    print("MENÚ DE GESTION DE EMPLEADOS\n")
    while True:
        print("OPCIÓN 1. CREAR EMPLEADO")
        print("OPCIÓN 2. BUSCAR EMPLEADO")
        print("OPCIÓN 3. MODIFICAR EMPLEADO")
        print("OPCIÓN 4. ELIMINAR EMPLEADO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.\n")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.\n")
            continue

        match opcion_user:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass


def menu_gestion_depto():
    print("MENÚ DE GESTION DE DEPARTAMENTOS\n")
    while True:
        print("OPCIÓN 1. CREAR DEPARTAMENTO")
        print("OPCIÓN 2. BUSCAR DEPARTAMENTO")
        print("OPCIÓN 3. MODIFICAR DEPARTAMENTO")
        print("OPCIÓN 4. ELIMINAR DEPARTAMENTO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

def menu_gestion_informe():
    print("MENÚ DE GESTION DE INFORMES\n")
    while True:
        print("OPCIÓN 1. CREAR INFORME")
        print("OPCIÓN 2. BUSCAR INFORME")
        print("OPCIÓN 3. MODIFICAR INFORME")
        print("OPCIÓN 4. ELIMINAR INFORME")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass

def menu_gestion_proyecto():
    print("MENÚ DE GESTION DE PROYECTOS\n")
    while True:
        print("OPCIÓN 1. CREAR PROYECTO")
        print("OPCIÓN 2. BUSCAR PROYECTO")
        print("OPCIÓN 3. MODIFICAR PROYECTO")
        print("OPCIÓN 4. ELIMINAR PROYECTO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass