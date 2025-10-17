from config import conectar_db
from datetime import datetime
from models import (Persona,
                    Empleado,
                    Gerente,
                    Administrador,
                    Departamento)
import mysql.connector
import re

from models.Administrador import *

# DEPARTAMENTO
def crear_departamento():
    while True:
        try: 
            nombre = input("Ingrese el nombre del departamento: ").strip()
            if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                print("Ingrese un nombre válido (solo letras y espacios).")
            else:
                break
        except Exception as Error:
                print(f"Error inesperado al ingresar el nombre: {Error}")

    while True:
        try:
            rut_gerente_asociado = input("Ingrese el RUT del gerente (ej: 12345678-K): ").strip().lower()
            validar_rut(rut_gerente_asociado)

            # Verificación de existencia del gerente en la base de datos

            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT rol FROM usuario_basico WHERE rut_usuario = %s", (rut_gerente_asociado.upper(),))
            resultado = cursor.fetchone()

            if not resultado:
                print("El RUT no está registrado en el sistema.")
                continue
            elif resultado['rol'].lower() != "gerente":
                print("El usuario no tiene rol de Gerente.")
                continue
            else:
                break
        except ValueError as Error:
            print(f"Error inesperado: {Error}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_departamento FROM departamento WHERE LOWER(nombre) = %s", (nombre.lower(),))
        if cursor.fetchone():
            print("Ya existe un departamento con ese nombre.")
            return
        
        query = """
            INSERT INTO departamento (nombre, rut_usuario) VALUES (%s, %s)
        """
        valores = (nombre, rut_gerente_asociado.upper())
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Departamento creado con ID: {id_generado}")

        nuevo_departamento = Departamento(nombre=nombre, rut_gerente=rut_gerente_asociado.upper())
    except Exception as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

    return nuevo_departamento

def modificar_departamento():
    try:
        id_departamento = int(input("Ingrese el ID del departamento a modificar: "))
    except ValueError:
        print("Debe ingresar un carácter numérico para continuar.")
        return

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM departamento WHERE id_departamento = %s", (id_departamento,))
        departamento = cursor.fetchone()

        if not departamento:
            print("No se encontró ningún departamento con esa ID.")
            return
        
        print("\nDepartamento encontrado. ¿Qué campo desea modificar?")
        print("1. Nombre")
        print("2. Descripción")

        try:
            opcion = int(input("Seleccione una opción (1-2): "))
            campos = {
                1: "nombre",
                2: "descripcion",
            }
        except ValueError:
            print("Debe ingresar un carácter numérico para continuar.")
            return
        
        if opcion not in campos:
            print("Opción inválida.")
            return
                            
        campo = campos[opcion]
        nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}'").strip()

        # Validaciones
        if campo == "nombre":
            if not nuevo_valor or not all(c.isalpha() or c.isspace() for c in nuevo_valor):
                print("Solo se permiten letras y espacios.")
                return
        elif campo == "descripcion":
            if not nuevo_valor:
                print("La descripción no puede estar vacía.")
                return
            
        # Confirmación
        while True:
            confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
            if confirmacion == "s":
                break
            elif confirmacion == "n":
                print("Modificación cancelada.")
                return
            else:
                print("Entrada inválida. Debes ingresar 'S' o 'N'.")  

        # Actualización
        try:
            query = f"UPDATE departamento SET {campo} = %s WHERE id_departamento = %s"
            cursor.execute(query, (nuevo_valor, id_departamento))
            conexion.commit()
            print(f"El campo {campo} del departamento con ID {id_departamento} se ha actualizado correctamente a: {nuevo_valor}")
        except mysql.connector.Error as Error:
            print(f"Error inesperado al actualizar los datos del departamento con ID {id_departamento}\nDetalles del error: {Error}")
    except Exception as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close() 
        if conexion:
            conexion.close()

def buscar_departamento():
    while True:
        try:
            id_departamento = int(input("Ingrese el ID del departamento: "))
            break
        except ValueError as Error:
            print(Error)

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
            SELECT id_departamento, nombre, rut_usuario, descripcion   
            FROM departamento
            WHERE id_departamento = %s
        """
        cursor.execute(query, (id_departamento,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            print("\nDatos del departamento encontrado:")
            campos = ["ID Departamento", "Nombre", "RUT del gerente asociado", "Descripción"]             
            for campo, valor in zip(campos, resultado):
                print(f"{campo}: {valor}")
        else:
            print("No se encontró a ningún departamento con esta ID.\n")
    except Exception as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def eliminar_departamento():
    while True:
        try:
            id_departamento = int(input("Ingrese la ID del departamento que desea eliminar: "))
            break
        except ValueError as Error:
            print(Error)
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT id_departamento, nombre, descripcion FROM departamento WHERE id_departamento = %s", (id_departamento,))
        departamento = cursor.fetchone()

        if not departamento:
            print("No se encontró ningún departamento con esta ID.")
            return
                        
        print("\nDepartamento encontrado:")
        print(f"ID del departamento: {departamento['id_departamento']}") 
        print(f"Nombre del departamento: {departamento['nombre']}")
        print(f"Descripción: {departamento['descripcion']}")

        while True:
            confirmacion = input("¿Estás seguro que deseas eliminar este departamento? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
            if confirmacion == "s":
                break
            elif confirmacion == "n":
                print("Operación cancelada.")
                return
            else:
                print("Entrada inválida. Debes ingresar 'S' o 'N'.")
        
        cursor.execute("SELECT COUNT(*) AS total FROM usuario_detalle WHERE id_departamento = %s", (id_departamento,))
        dependencias = cursor.fetchone()
        if dependencias['total'] > 0:
            print("No se puede eliminar el departamento porque tiene empleados asignados.")
            return
                            
        cursor.execute("DELETE FROM departamento WHERE id_departamento = %s", (id_departamento,))
        conexion.commit()
        print(f"El departamento {departamento['nombre']} con la ID {departamento['id_departamento']} se ha eliminado correctamente.")
    except Exception as e:
        print(f"Error inesperado al eliminar: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

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




# EMPLEADO
def validar_rut(rut):
    rut = rut.strip().lower()
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
    return rut.upper()

def buscar_empleado(rut):
    try:
        rut = validar_rut(rut)  # Si es válido, retorna el RUT limpio
        print(f"RUT ingresado correctamente: {rut}")
    except ValueError as Error:
        print(Error)
        return  # Salir si el RUT no es válido

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
        SELECT rut_usuario
        FROM usuario
        WHERE rut_usuario = %s
        """
        cursor.execute(query, (rut,))
        resultado = cursor.fetchone()

        if resultado:
            print("¡ERROR!. El usuario se encuentra registrado en el sistema.\n")
        else:
            print("El usuario no está registrado.")
    except Exception as e:
        print(f"Error inesperado al buscar el empleado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


# Función exclusiva de Administrador y Gerente (o cualquier clase que vaya a poseer esos privilegios)
def super_buscar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
            if validar_rut(rut):
                break
        except ValueError as Error:
            print(Error)

    conexion = conectar_db()
    cursor = conexion.cursor()

    query = """
    SELECT ub.rut_usuario, ub.nombres, ub.apellido_paterno, ub.apellido_materno,
           ud.direccion, ub.fecha_nacimiento, ud.fecha_inicio_contrato,
           ud.salario, ub.numero_telefonico, ub.rol, ud.id_departamento
    FROM usuario_basico ub
    JOIN usuario_detalle ud ON ub.rut_usuario = ud.rut_usuario
    WHERE ub.rut_usuario = %s
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
            print(f"{campo}: {valor}\n")
    else:
        print("No se encontró a ningún empleado con ese RUT.\n")

def modificar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a modificar: ").strip().upper()
            if validar_rut():
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
            if validar_rut(rut):
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

def insertar_empleado_completo(datos_basico, datos_detalle):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query_basico = """
            INSERT INTO usuario_basico (
                rut_usuario, nombres, apellido_paterno, apellido_materno,
                fecha_nacimiento, numero_telefonico, contraseña, rol
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        query_detalle = """
            INSERT INTO usuario_detalle (
                rut_usuario, direccion, fecha_inicio_contrato,
                salario, rol, id_departamento
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_basico, datos_basico)
        cursor.execute(query_detalle, datos_detalle)
        conexion.commit()
        print("Empleado creado con éxito.\n")

    except mysql.connector.Error as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def insertar_empleado_detalle(datos_detalle):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query_detalle = """
            INSERT INTO usuario_detalle (
                rut_usuario, direccion, fecha_inicio_contrato,
                salario, rol, id_departamento
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_detalle, datos_detalle)
        conexion.commit()
        print("Empleado creado con éxito.\n")
    except mysql.connector.Error as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

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
                admin.crear_empleado()
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


#INFORME
def menu_gestion_informe(admin: Administrador, gerente: Gerente):
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
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 2:
                if admin:
                    admin.buscar_informe()
                elif gerente:
                    gerente.buscar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 3:
                if admin:
                    admin.modificar_informe()
                elif gerente:
                    gerente.modificar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios.")
            case 4:
                if admin:
                    admin.eliminar_informe()
                elif gerente:
                    gerente.eliminar_informe()
                else:
                    print("No tienes los privilegios de acceso necesarios para continuar")
            case 5:
                print("Será devuelto al menú principal...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break

# PROYECTO
def crear_proyecto():
    while True:
        try: 
            nombre = input("Ingrese el nombre del proyecto: ")
            if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                print("Ingrese un nombre valido")
                continue
            # Para normalizar el nombre y evitar duplicaciones en la base de datos.
            nombre = ' '.join(nombre.split()).title()
            break
        except Exception as Error:
            print(f"Error inesperado: {Error}")
                    
    while True:
        try:
            descripcion = input("Ingrese una descripcion al proyecto: ")
            if not descripcion:
                print("Ingrese una descripcion valida")
                continue
            break
        except Exception as Error:
            print(f"Error inesperado: {Error}")

    while True:
        try:
            fecha_inicio = input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
            fecha = datetime.strptime(fecha_inicio, '%d/%m/%Y').date()
            print(f"Fecha ingresada correctamente: {fecha}")
            break
        except ValueError:
            print("Formato inválido. Use el formato DD/MM/AAAA.")
             
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_proyecto FROM proyecto WHERE LOWER(nombre) = %s", (nombre.lower(),))
        if cursor.fetchone():
            print("Ya existe un proyecto con ese nombre.")
            return
        
        query = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        valores = (nombre, descripcion, fecha)
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Detalles del proyecto creado:\n")
        print(f"Nombre: {nombre} | Descripción: {descripcion} | Fecha: {fecha} | ID: {id_generado}")
    except Exception as Error:
        print(f"Error al crear el proyecto: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def buscar_proyecto():
    while True:
        try:
            id_proyecto = int(input("Ingrese la ID del proyecto que desea buscar: "))
            break
        except ValueError as Error:
            print(f"Error inesperado: {Error}")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
            SELECT p.id_proyecto, p.nombre, p.descripcion, p.fecha_inicio, p.id_departamento, d.nombre AS nombre_departamento
            FROM proyecto p
            JOIN departamento d ON p.id_departamento = d.id_departamento
            WHERE p.id_proyecto = %s
        """
        cursor.execute(query, (id_proyecto,))
        resultado = cursor.fetchone()

        if resultado:
            print("\nDatos del proyecto encontrado:")
            campos = ["ID Proyecto",
                    "Nombre",
                    "Descripcion",
                    "Fecha de inicio",
                    "ID Departamento",
                    "Nombre del departamento"
            ]               
            for campo, valor in zip(campos, resultado):
                print(f"{campo}: {valor}")
                print()
        else:
            print("No se encontró a ningún proyecto con esta ID.\n")

    except Exception as Error:
        print(f"Error inesperado al buscar el proyecto: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def modificar_proyecto():
    while True:
        try:
            id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
            break
        except ValueError as Error:
            print(f"Entrada inválida: {Error}")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
        proyecto = cursor.fetchone()

        if not proyecto:
            print("No se encontró ningún proyecto con esa ID.")
            return

        print("\nProyecto encontrado. ¿Qué campo desea modificar?")
        print("1. Nombre")
        print("2. Descripción")
        print("3. Fecha de inicio\n")

        try:
            opcion = int(input("Seleccione una opción (1-3): "))
        except ValueError:
            print("Debe ingresar un carácter numérico para continuar.")
            return
        
        campos = {
            1: "nombre",
            2: "descripcion",
            3: "fecha_inicio",
        }

        if opcion not in campos:
            print("Opción inválida.")
            return

        campo = campos[opcion]
        print(f"Valor actual de '{campo}': {proyecto[campo]}")
        nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip()

        if campo == "nombre":
            if not nuevo_valor or not all(c.isalnum() or c.isspace() for c in nuevo_valor):
                raise ValueError("Solo se permiten letras, números y espacios.")
            nuevo_valor = ' '.join(nuevo_valor.split()).title()
        elif campo == "descripcion":
            if not nuevo_valor:
                raise ValueError("La descripción no puede estar vacía.")
        elif campo == "fecha_inicio":
            try:
                nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y").date()
            except ValueError:
                print("Formato de fecha inválido. Use DD/MM/AAAA para continuar.")
                return

        while True:
            confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
            if confirmacion == "s":
                break
            elif confirmacion == "n":
                print("Modificación cancelada.")
                return
            else:
                print("Entrada inválida. Debes ingresar 'S' o 'N'.")

        query = f"UPDATE proyecto SET {campo} = %s WHERE id_proyecto = %s"
        cursor.execute(query, (nuevo_valor, id_proyecto))
        conexion.commit()
        print("Modificación realizada con éxito.")

    except ValueError as Error:
        print(f"Error: {Error}")
    except Exception as e:
        print(f"Error inesperado al modificar el proyecto: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def eliminar_proyecto():
    while True:
        try:
            id_proyecto = int(input("Ingrese la ID del proyecto que desea eliminar: "))
            break
        except ValueError as Error:
            print(f"Error inesperado: {Error}")
    
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT id_proyecto, nombre, descripcion FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
        proyecto = cursor.fetchone()

        if not proyecto:
            print(f"No se encontró ningún proyecto con la ID ingresada: {id_proyecto}")
            return
        
        print("\nProyecto encontrado:")
        print(f"ID del proyecto: {proyecto['id_proyecto']}")
        print(f"Nombre: {proyecto['nombre']}")
        print(f"Descripción: {proyecto['descripcion']}")

        while True:
            confirmacion = input("¿Está seguro que desea eliminar este proyecto? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
            if confirmacion == 's':
                break
            elif confirmacion == 'n':
                print("Operación cancelada.")
                return
            else:
                print("Entrada inválida, debes ingresar 'S' o 'N' para poder continuar.")
        
        cursor.execute("DELETE FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
        conexion.commit()
        print(f"\nEl proyecto ha sido eliminado exitosamente.")
        print(f"ID: {id_proyecto}")
        print(f"Nombre: {proyecto['nombre']}")
        print(f"Descripción: {proyecto['descripcion']}")

    except Exception as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

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
                    admin.crear_proyecto()
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