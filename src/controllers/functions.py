from config import conectar_db
from itertools import cycle
from datetime import datetime, date
from models import (Persona,
                    Empleado,
                    Gerente,
                    Administrador)
import re


# Nota: Esta funcion crea cualquier tipo de empleado, incluyendo Gerente y Administrador, o cualquiera que se quiera implementar a futuro.
def crear_empleado():
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
                
    roles_validos = {"empleado", "gerente", "administrador"}
    while True:
        try:
            rol_usuario = input("Ingrese el rol del usuario: ").strip().lower()
            if rol_usuario not in roles_validos:
                raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
            rol_usuario = rol_usuario.capitalize()

            break
        except ValueError as Error:
            print(Error)
        
    while True:
        try: 
            nombre = input("Ingrese el primer nombre del empleado: ")
            if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
            break
        except ValueError as Error:
            print(Error)   
    while True:
        try: 
            apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
            if not apellido_paterno or not all(c.isalpha() or c.isspace() for c in apellido_paterno):
                raise ValueError("Ingrese un apellido paterno válido (solo letras y espacios).")
            break
        except ValueError as Error:
                print(Error)
    while True:
        try: 
            apellido_materno = input("Ingrese el apellido materno del empleado: ")
            if not apellido_materno or not all(c.isalpha() or c.isspace() for c in apellido_materno):
                raise ValueError("Ingrese un apellido materno válido (solo letras y espacios).")
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
            if salario <= 0:
                raise ValueError("El salario debe ser un número positivo")
            break
        except ValueError:
            print("Ingrese un sueldo valido") 

    while True:
        try:
            nro_telefono = input("Ingrese el número de teléfono del empleado (formato: +56 9 XXXX XXXX): ").strip()
            patron = r"^\+56 9 \d{4} \d{4}$"
            if not re.match(patron, nro_telefono):
                raise ValueError("Formato inválido. Use: +56 9 XXXX XXXX")
            break
        except ValueError as Error:
            print(Error)

    while True:
        try:
            id_departamento = int(input("Ingrese ID del departamento asignado al empleado: "))
            if len(str(id_departamento)) < 15:
                raise ValueError("Debe ser un número de hasta 15 dígitos.")
            break
        except ValueError:
                print("Debe ingresar carácteres numéricos.")

    clases_usuario = {
        "Empleado":Empleado,
        "Gerente":Gerente,
        "Administrador":Administrador
    }

    nuevo_usuario: Persona = clases_usuario[rol_usuario](
        rut_empleado.upper(), nombre, apellido_paterno, apellido_materno,
        direccion, fecha_nacimiento, fecha_inicio_contrato,
        salario, nro_telefono, id_departamento
    )

    nuevo_usuario.guardar_en_db()

def buscar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a buscar (ej: 12345678-K): ").strip().upper()
            if rut.count('-') != 1:
                raise ValueError("El RUT debe contener un solo guion ('-').")

            parte_num, dv = rut.split('-')

            if len(rut) < 9 or len(rut) > 10:
                raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

            if not parte_num.isdigit():
                raise ValueError("Los caracteres antes del guion deben ser solo números.")

            if len(parte_num) not in [7, 8]:
                raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

            if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
                raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

            print(f"RUT ingresado correctamente: {rut.upper()}")
            break
        except ValueError as Error:
            print(Error)

    conexion = conectar_db()
    cursor = conexion.cursor()

    query = """
    SELECT rut_usuario, nombres, apellido_paterno, apellido_materno,
            direccion, fecha_nacimiento, fecha_inicio_contrato,
            salario, numero_telefonico, rol, id_departamento
    FROM usuario
    WHERE rut_usuario = %s
"""
    cursor.execute(query, (rut,))
    resultado = cursor.fetchone()

    cursor.close()
    conexion.close()

    if resultado:
        print("\nDatos del empleado encontrado:")
        campos = ["RUT",
                  "Nombre",
                  "Apellido Paterno",
                  "Apellido Materno",
                  "Dirección",
                  "Fecha Nacimiento",
                  "Inicio Contrato",
                  "Salario",
                  "Teléfono",
                  "Rol",
                  "ID Departamento"]
        
        for campo, valor in zip(campos, resultado):
            print(f"{campo}: {valor}")
        print()
    else:
        print("No se encontró a ningún empleado con ese RUT.\n")

def modificar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a modificar: ").strip().upper()
            if rut.count('-') != 1:
                raise ValueError("El RUT debe contener un solo guion ('-').")

            parte_num, dv = rut.split('-')

            if len(rut) < 9 or len(rut) > 10:
                raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

            if not parte_num.isdigit():
                raise ValueError("Los caracteres antes del guion deben ser solo números.")

            if len(parte_num) not in [7, 8]:
                raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

            if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
                raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

            print(f"RUT ingresado correctamente: {rut.upper()}")
            break
        except ValueError as Error:
            print(Error)

        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM Usuario WHERE rut_usuario = %s", (rut,))
            empleado = cursor.fetchone()

            if not empleado:
                print("No se encontró ningún empleado con ese RUT.")
                cursor.close()
                conexion.close()
                return
        
            print("\nEmpleado encontrado. ¿Qué campo desea modificar?")
            print("1. Nombre")
            print("2. Apellido Paterno")
            print("3. Apellido Materno")
            print("4. Dirección")
            print("5. Fecha de Nacimiento")
            print("6. Fecha de Inicio de Contrato")
            print("7. Salario")
            print("8. Teléfono")
            print("9. Rol")
            print("10. ID Departamento")
        except Exception as e:
            print(f"Error al guardar el empleado: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

        try:
            opcion = int(input("Seleccione una opción (1-10): "))
            campos = {
                1: "nombres",
                2: "apellido_paterno",
                3: "apellido_materno",
                4: "direccion",
                5: "fecha_nacimiento",
                6: "fecha_inicio_contrato",
                7: "salario",
                8: "numero_telefonico",
                9: "rol",
                10: "id_departamento"
            }
            if opcion not in campos:
                print("Opción inválida.")
                return
            
            campo = campos[opcion]
            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}'").strip()

            if campo in ["nombres", "apellido_paterno", "apellido_materno"]:
                if not nuevo_valor or not all(c.isalpha() or c.isspace() for c in nuevo_valor):
                    raise ValueError("Solo se permiten letras y espacios.")
            elif campo == "direccion":
                if not nuevo_valor:
                    raise ValueError("La dirección no puede estar vacía.")
            elif campo in ["fecha_nacimiento", "fecha_inicio_contrato"]:
                nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y").date()
            elif campo == "salario":
                nuevo_valor = int(nuevo_valor)
                if nuevo_valor <= 0:
                    raise ValueError("El salario debe ser positivo.")
            elif campo == "numero_telefonico":
                if not(nuevo_valor.isdigit() and len(nuevo_valor) == 9 and nuevo_valor[0] == "9"):
                    raise ValueError("Número telefónico inválido.")
            elif campo == "rol":
                roles_validos = {"empleado", "gerente", "administrador"}
                if nuevo_valor.lower() not in roles_validos:
                    raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
                nuevo_valor = nuevo_valor.capitalize()
            elif campo == "id_departamento":
                if not nuevo_valor.isdigit() or len(nuevo_valor) > 15:
                    raise ValueError("ID Departamento debe ser numérico y de hasta 15 dígitos.")

            while True:
                confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
                if confirmacion == "s":
                    break
                elif confirmacion == "n":
                    print("Modificación cancelada.")
                    return
                else:
                    print("Entrada inválida. Debes ingresar 'S' o 'N'.")

            query = f"UPDATE Usuario SET {campo} = %s WHERE rut_usuario = %s"
            cursor.execute(query, (nuevo_valor, rut))
            conexion.commit()
            print("Modificación realizada con éxito.")

        except ValueError as Error:
            print(f"Error: {Error}")
        finally:
            if cursor:
                cursor.close() 
            if conexion:
                conexion.close()

def eliminar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a eliminar (ej: 12345678-K): ").strip().lower()
            if rut.count('-') != 1:
                raise ValueError("El RUT debe contener un solo guion ('-').")
            parte_num, dv = rut.split('-')
            if len(rut) < 9 or len(rut) > 10:
                raise ValueError("El RUT debe tener entre 9 y 10 caracteres.")
            if not parte_num.isdigit():
                raise ValueError("La parte numérica debe ser solo números.")
            if len(parte_num) not in [7, 8]:
                raise ValueError("Debe tener 7 u 8 dígitos antes del guion.")
            if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
                raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")
            rut = rut.upper()
            break
        except ValueError as Error:
            print(Error)

    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombres, apellido_paterno, rol FROM Usuario WHERE rut_usuario = %s", (rut,))
    empleado = cursor.fetchone()

    if not empleado:
        print("No se encontró ningún empleado con ese RUT.")
        cursor.close()
        conexion.close()
        return
    
    print("\nEmpleado encontrado:")
    print(f"Nombre: {empleado['nombres']} {empleado['apellido_paterno']}")
    print(f"Rol: {empleado['rol']}")

    confirmacion = input("¿Estás seguro que deseas eliminar este empleado? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        cursor.close()
        conexion.close()
        return
    
    try:
        cursor.execute("DELETE FROM Usuario WHERE rut_usuario = %s", (rut,))
        conexion.commit()
        print(f"El empleado con RUT {rut} ha sido eliminado de forma permanente.\n")
    except Exception as e:
        print(f"Error inesperado al eliminar: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def insertar_empleado(datos):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Usuario (
                rut_usuario, nombres, apellido_paterno, apellido_materno,
                direccion, fecha_nacimiento, fecha_inicio_contrato,
                salario, numero_telefonico, rol, id_departamento
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, datos)
        conexion.commit()
        cursor.close()
        print("Empleado creado con éxito.\n")
    except Exception as e:
        print(f"Error al insertar ejemplo: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

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
            continue

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.\n")
            continue

        match opcion_user:
            case 1:
                crear_empleado() 

            case 2:
                buscar_empleado()

            case 3:
                modificar_empleado()

            case 4:
                eliminar_empleado()

            case 5:
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

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                while True:
                    try: 
                        nombre = input("Ingrese el nombre del departamento: ").strip()
                        if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                            raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                        break
                    except ValueError as Error:
                        print(Error)

                while True:
                    try:
                        rut_gerente_asociado = input("Ingrese el RUT del gerente (ej: 12345678-K): ").strip().lower()
                        parte_num, dv = rut_gerente_asociado.split('-')
                        if rut_gerente_asociado.count('-') != 1 or not parte_num.isdigit() or dv not in '0123456789k':
                            raise ValueError("RUT inválido.")
                        print(f"RUT ingresado correctamente: {rut_gerente_asociado.upper()}")
                        break
                    except ValueError as Error:
                        print(Error)

                ##from config import conectar_db
                try:
                    conexion = conectar_db()
                    cursor = conexion.cursor()
                    query = "INSERT INTO departamento (nombre, rut_gerente_asociado) VALUES (%s, %s)"
                    valores = (nombre, rut_gerente_asociado.upper())
                    cursor.execute(query, valores)
                    conexion.commit()
                    id_generado = cursor.lastrowid
                    print(f"Departamento creado con ID: {id_generado}")
                except Exception as e:
                    print(f"Error al crear el departamento: {e}")
                finally:
                    cursor.close()
                    conexion.close()

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