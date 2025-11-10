from models.Gerente import Gerente
from models.Empleado import Empleado
from models.Administrador import Administrador
from .functions_departamento import (
    crear_departamento,
    buscar_departamento,
    modificar_departamento,
    eliminar_departamento
)
from .functions_informe import generarInforme
from typing import Union, Optional
from functions.validador import generarPDF
from functions.validador import generarExcel
from functions.menu_valores import(menu_utm,
                                   menu_uf,
                                   menu_dolar,
                                   menu_euro,
                                   menu_ipc,
                                   menu_ivp)
from models.Persona import Persona

def menu_gestion_proyecto(usuario: Union [Administrador,Gerente]):
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
                if usuario:
                    usuario.crearProyecto()
                else:
                    print("No tienes los privilegios necesarios para acceder.")
            case 2:
                if usuario:
                    usuario.buscarProyecto()
                else:
                    print("No tienes los privilegios de acceso necesarios para continuar.")
            case 3:
                if usuario:
                    usuario.modificarProyecto()
                else:
                    print("No tienes los privilegios ncesarios para continuar.")
            case 4:
                if usuario:
                    usuario.eliminarProyecto()
                else:
                    print("No tienes los privilegios necesarios para continuar.")
            case 5:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_gestion_informe(usuario: Optional[Union [Administrador, Gerente]] = None, empleado: Empleado=None):
    print("MENÚ DE GESTION DE INFORMES\n")
    while True:
        print("OPCIÓN 1. CREAR INFORME")
        print("OPCIÓN 2. BUSCAR INFORME")
        print("OPCIÓN 3. MODIFICAR INFORME")
        print("OPCIÓN 4. ELIMINAR INFORME")
        if usuario:
            print("OPCION 5. GENERAR ARCHIVO DE INFORME")
            print("OPCION 6. VOLVER AL MENU PRINCIPAL")
            try: 
                opcion_user = int(input("Ingresar opción (1 - 6): "))
            except ValueError:
                print("Debe ingresar una opción válida para continuar.")
                continue

            if opcion_user not in (1,2,3,4,5,6):
                print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
                continue

            match opcion_user:
                case 1:
                    if usuario:
                        usuario.crearInforme()
                        print(usuario.rut)
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 2:
                    if usuario:
                        usuario.buscarInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 3:
                    if usuario:
                        usuario.modificarInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 4:
                    if usuario:
                        usuario.eliminarInforme()
                    else:
                        print("No tienes los privilegios necesarios para continuar.")
                case 5:
                    if usuario:
                        while True:
                            print("OPCION 1. GENERAR ARCHIVO PDF")
                            print("OPCION 2. GENERAR ARCHIVO EXCEL")
                            print("OPCION 3. VOLVER AL MENU ANTERIOR")
                            try: 
                                opcion_informe = int(input("Ingresar opción (1 - 3): "))
                            except ValueError:
                                print("Debe ingresar una opción válida para continuar.")
                                continue

                            if opcion_informe not in (1,2,3):
                                print("Debe ingresar una de las opciones disponibles (1 - 3) para continuar.")
                                continue
                            match opcion_informe:
                                case 1:
                                    generarPDF()
                                case 2:
                                    generarExcel()
                                case 3:
                                    print("Será devuelto al menú principal...")
                                    input("PRESIONE ENTER PARA CONTINUAR ")
                                    break

                    else:
                        print("No tienes los privilegios de acceso necesarios para continuar")
                case 6:
                    print("Será devuelto al menú principal...")
                    input("PRESIONE ENTER PARA CONTINUAR ")
                    break


        elif empleado:
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
                    if empleado:
                        empleado.crearInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 2:
                    if empleado:
                        empleado.buscarInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 3:
                    if empleado:
                        empleado.modificarInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios.")
                case 4:
                    if empleado:
                        empleado.eliminarInforme()
                    else:
                        print("No tienes los privilegios de acceso necesarios para continuar")
                case 5:
                    print("Será devuelto al menú principal...")
                    input("PRESIONE ENTER PARA CONTINUAR ")
                    break


def menu_gestion_emp(usuario: Union [Administrador, Gerente]):
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
                usuario.crearEmpleado()
            case 2:
                usuario.crearEmpleadoDetalle()
            case 3:
                usuario.super_buscar_empleado()
            case 4:
                usuario.modificarEmpleado()
            case 5:
                usuario.eliminarEmpleado()
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

def menu_gestion_registrotiempo(usuario: Empleado):
    print("MENÚ DE GESTION DE REGISTRO DE TIEMPO(S)\n")
    while True:
        print("OPCIÓN 1. CREAR REGISTRO DE TIEMPO")
        print("OPCIÓN 2. BUSCAR REGISTRO DE TIEMPO")
        print("OPCIÓN 3. VOLVER AL MENÚ PRINCIPAL\n")
        try:
            opcion_user = int(input("Ingresar opción (1-3): "))
        except ValueError as Error:
            print(f"Debe ingresar un carácter válido para continuar: {Error}")
        
        if opcion_user not in (1,2,3):
            print("Debe ingresar una opción válida para continuar.")
            return
        
        match opcion_user:
            case 1:
                usuario.crearRegistroTiempo()
            case 2:
                usuario.buscarRegistroTiempo()
            case 3:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break

def menu_gestion_proyecto_emp(usuario: Empleado):
    print("MENÚ DE GESTIÓN DE PROYECTOS PARA EMPLEADO\n")
    while True:
        print("OPCIÓN 1. BUSCAR PROYECTO.")
        print("OPCIÓN 2. VOLVER AL MENÚ PRINCIPAL.")
        try:
            opcion_user = int(input("Ingresar opción (1-2): "))
        except ValueError as Error:
            print(f"Debe ingresar un carácter válido para continuar: {Error}")
        
        if opcion_user not in (1,2):
            print("Debe ingresar una opción válida para continuar.")

        match opcion_user:
            case 1:
                usuario.buscarProyecto()

            case 2:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break
            
def menu_gestion_valores(usuario:Persona):
    while True:
        print("MENÚ DE CONSULTA DE INDICADORES ECONOMICOS\n")
        print("         1.- UF          ")
        print("         2.- IVP          ")
        print("         3.- ICP         ")
        print("         4.- UTM          ")
        print("         5.- DOLAR          ")
        print("         6.- EURO          ")
        print("         7.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-7")

        if opcion not in (1,2,3,4,5,6,7):
            print("Debe ingresar una de las opciones del 1-7")

        match opcion:
            case 1:
                menu_uf(usuario)
            case 2:
                menu_ivp(usuario)
            case 3:
                menu_ipc(usuario)
            case 4:
                menu_utm(usuario)
            case 5:
                menu_dolar(usuario)
            case 6:
                menu_euro(usuario)
            case 7:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break

    
