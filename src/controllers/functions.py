from config import conectar_db
from datetime import datetime
from models import (Persona,
                    Empleado,
                    Gerente,
                    Administrador,
                    Departamento,
                    Proyecto)
import mysql.connector
import re
from models import (InformeEmpleado,
                    InformeGerente,
                    InformeAdmin)
from utils.validador import validar_rut
from models.Administrador import *

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


