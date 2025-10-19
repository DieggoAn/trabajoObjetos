from models import (Persona,
                    Empleado,
                    Gerente,
                    Departamento,
                    Proyecto)
from models.Administrador import *
from .functions import *
from utils.validador import *
from .functions_proyecto import * 
from .functions_departamento import * 
from .functions_informe import *

def menu_gestion_proyecto(admin: Administrador, gerente: Gerente):
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
                if admin:
                    admin.crearProyecto()
                elif gerente:
                    gerente.crear_proyecto()
                else:
                    print("No tienes los privilegios necesarios para acceder.")
            case 2:
                if admin:
                    admin.buscar_proyecto()
                elif gerente:
                    gerente.buscar_proyecto()
                else:
                    print("No tienes los privilegios de acceso necesarios para continuar.")
            case 3:
                if admin:
                    admin.modificar_proyecto()
                elif gerente:
                    gerente.modificar_proyecto()
                else:
                    print("No tienes los privilegios ncesarios para continuar.")
            case 4:
                if admin:
                    admin.eliminar_proyecto()
                elif gerente:
                    gerente.eliminar_proyecto()
                else:
                    print("No tienes los privilegios necesarios para continuar.")
            case 5:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_gestion_informe(admin: Administrador, emp: Empleado, gerente: Gerente):
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
            continue

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                if admin:
                    admin.crear_informe()
                elif gerente:
                    gerente.crear_informe()
                elif emp:
                    emp.crear_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 2:
                if admin:
                    admin.buscar_informe()
                elif gerente:
                    gerente.buscar_informe()
                elif emp:
                    emp.buscar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 3:
                if admin:
                    admin.modificar_informe()
                elif gerente:
                    gerente.modificar_informe()
                elif emp:
                    emp.modificar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 4:
                if admin:
                    admin.eliminar_informe()
                elif gerente:
                    gerente.eliminar_informe()
                elif emp:
                    emp.eliminar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios para continuar")
            case 5:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_gestion_emp(admin: Administrador):
    print("MENÚ DE GESTION DE EMPLEADOS\n")
    while True:
        print("OPCIÓN 1. CREAR EMPLEADO DESDE CERO")
        print("OPCIÓN 2. INSERTAR DATOS CONTRACTUALES DE EMPLEADO")
        print("OPCIÓN 3. BUSCAR EMPLEADO")
        print("OPCIÓN 4. MODIFICAR EMPLEADO")
        print("OPCIÓN 5. ELIMINAR EMPLEADO")
        print("OPCIÓN 6. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 6): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.\n")
            continue

        if opcion_user not in (1,2,3,4,5,6):
            print("Debe ingresar una de las opciones disponibles (1 - 6) para continuar.\n")
            continue

        match opcion_user:
            case 1:
                admin.crearEmpleado()
            case 2:
                admin.insertar_empleado_detalle()
            case 3:
                admin.super_buscar_empleado()
            case 4:
                admin.modificar_empleado()
            case 5:
                admin.eliminar_empleado()
            case 6:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


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
            return
        
        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                crear_departamento()
            case 2:
                buscar_departamento()
            case 3:
                modificar_departamento()     
            case 4:
                eliminar_departamento()
            case 5:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break

