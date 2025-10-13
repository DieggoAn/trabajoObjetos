import mysql.connector
from itertools import cycle
from datetime import datetime, date

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
                while True:
                    try:
                        rut_empleado = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()

                        if rut_empleado.count('-') != 1:
                            raise ValueError("El RUT debe contener un solo guion ('-').")

                        parte_num, dv = rut_empleado.split('-')

                        if len(rut_empleado) < 9 or len(rut_empleado) > 10:
                            raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

                        if not parte_num.isdigit():
                            raise ValueError("Los caracteres antes del guion deben ser solo números.")

                        if len(parte_num) not in [7, 8]:
                            raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

                        if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
                            raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

                        print(f"RUT ingresado correctamente: {rut_empleado.upper()}")
                        break

                    except ValueError as Error:
                        print(Error)
        
                while True:
                    try: 
                        nombre = input("Ingrese el primer nombre del empleado: ")
                        if not nombre and all(c.isalpha() for c in nombre):
                         raise ValueError("Ingrese un nombre valido")
                        break
                    except ValueError as Error:
                        print(Error)   
                while True:
                    try: 
                        apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
                        if not apellido_paterno and all(c.isalpha() for c in apellido_paterno):
                         raise ValueError("Ingrese un apellido valido")
                        break
                    except ValueError as Error:
                        print(Error)
                while True:
                    try: 
                        apellido_materno = input("Ingrese el apellido materno del empleado: ")
                        if not apellido_materno and all(c.isalpha() for c in apellido_materno):
                         raise ValueError("Ingrese un apellido valido")
                        break
                    except ValueError as Error:
                        print(Error)      

                while True:
                    try:
                        direccion = input("Ingrese la direccion del empleado (ej: Av Arturo Prat 967): ")
                        if not direccion:
                            raise ValueError("Ingrese una direccion valida")
                        break
                    except ValueError as Error:
                        print(Error)

                while True:
                    try:
                        fecha_nacimiento = input("Ingrese la fecha de nacimiento del empleado (formato DD/MM/AAAA): ")
                        fecha = datetime.strptime(fecha_nacimiento, '%d/%m/%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break
                    except ValueError:
                        print("Formato inválido. Use el formato DD/MM/AAAA.")

                while True:
                    try:
                        fecha_inicio_contrato = input("Ingrese la fecha de inicio del contrato del empleado (formato DD/MM/AAAA): ")
                        fecha = datetime.strptime(fecha_inicio_contrato, '%d/%m/%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break
                    except ValueError:
                        print("Formato inválido. Use el formato DD/MM/AAAA.")

                while True:
                    try:
                        salario = int(input("Ingrese el salario asignado al empleado: "))
                        if not salario:
                            raise ValueError
                        break
                    except ValueError:
                        print("Ingrese un sueldo valido") 

                while True:
                    try:
                        nro_telefono = input("Ingrese el nro de telefono del empleado (este debe incluir el numero 9 al comienzo): ")
                        if not(nro_telefono.isdigit() and len(nro_telefono) == 9 and nro_telefono[0] == "9"):
                            raise ValueError("Ingrese un numero telefonico valido")
                        break
                    except ValueError as Error:
                        print(Error)

                #numerico #15 digitos #autoincrementable
                id_departamento = input("Ingrese el ID numerico del departamento asignado a este empleado: ") 

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
                while True:
                    try: 
                        nombre = input("Ingrese el nombre del departamento: ")
                        if not nombre and all(c.isalpha() for c in nombre):
                         raise ValueError("Ingrese un nombre valido")
                        break
                    except ValueError as Error:
                        print(Error)

                while True:
                    try:
                        rut_gerente_asociado = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()

                        if rut_gerente_asociado.count('-') != 1:
                            raise ValueError("El RUT debe contener un solo guion ('-').")

                        parte_num, dv = rut_gerente_asociado.split('-')

                        if len(rut_gerente_asociado) < 9 or len(rut_gerente_asociado) > 10:
                            raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

                        if not parte_num.isdigit():
                            raise ValueError("Los caracteres antes del guion deben ser solo números.")

                        if len(parte_num) not in [7, 8]:
                            raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

                        if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
                            raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

                        print(f"RUT ingresado correctamente: {rut_gerente_asociado.upper()}")
                        break
                    except ValueError as Error:
                        print(Error)
          

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
                while True:
                    try: 
                        nombre = input("Ingrese el nombre del departamento: ")
                        if not nombre and all(c.isalpha() for c in nombre):
                         raise ValueError("Ingrese un nombre valido")
                        break
                    except ValueError as Error:
                        print(Error)
                
                while True:
                    try:
                        descripcion_proyecto = input("Ingrese una descripcion al proyecto: ")
                        if not descripcion_proyecto:
                            raise ValueError("Ingrese una descripcion valida")
                        break
                    except ValueError as Error:
                        print(Error)

                while True:
                    try:
                        fecha_inicio_proyecto = input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
                        fecha = datetime.strptime(fecha_inicio_proyecto, '%d/%m/%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break
                    except ValueError:
                        print("Formato inválido. Use el formato DD/MM/AAAA.")
                

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                pass