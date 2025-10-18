from config import conectar_db
from models import Departamento
from utils.validador import validar_rut
import mysql.connector

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
        
        depto_obj = Departamento.Departamento(id_departamento)

        print("\nDepartamento encontrado. ¿Qué campo desea modificar?")
        print("1. Nombre")
        print("2. Descripción")
        print("3. Añadir empleado")
        print("4 Cambiar gerente")

        try:
            opcion = int(input("Seleccione una opción (1..4): "))
            campos = {
                1: "nombre",
                2: "descripcion",
                3: "anadir empleado",
                4: "cambiar gerente"
            }
        except ValueError:
            print("Debe ingresar un carácter numérico para continuar.")
            return
        
        if opcion not in campos:
            print("Opción inválida.")
            return
                            
        campo = campos[opcion]
        if campo == "anadir empleado":
            while True:
                try:
                    rut_empleado = input("Ingrese el RUT del empleado (ej: 12345678-K): ").strip().lower()
                    validar_rut(rut_empleado)

                        # Verificación de existencia del empleado en la base de datos

                    conexion = conectar_db()
                    cursor = conexion.cursor(dictionary=True)
                    cursor.execute("SELECT rol FROM usuario_basico WHERE rut_usuario = %s", (rut_empleado.upper(),))
                    resultado = cursor.fetchone()

                    if not resultado:
                        print("El RUT no está registrado en el sistema.")
                        continue
                    else:
                        depto_obj.asignarEmpleado(cursor,rut_empleado)
                        break
                except ValueError as Error:
                    print(f"Error inesperado: {Error}")
                finally:
                    if cursor:
                        cursor.close()
                    if conexion:
                        conexion.close()
                return True
        elif campo == "cambiar gerente":
            while True:
                try:
                    rut_gerente = input("Ingrese el RUT del gerente (ej: 12345678-K): ").strip().lower()
                    validar_rut(rut_gerente)

                        # Verificación de existencia del empleado en la base de datos

                    conexion = conectar_db()
                    cursor = conexion.cursor(dictionary=True)
                    cursor.execute("SELECT rol FROM usuario_basico WHERE rut_usuario = %s", (rut_gerente.upper(),))
                    resultado = cursor.fetchone()

                    if not resultado:
                        print("El RUT no está registrado en el sistema.")
                        continue
                    else:
                        depto_obj.asignarGerente(cursor,rut_gerente)
                        break
                except ValueError as Error:
                    print(f"Error inesperado: {Error}")
                finally:
                    if cursor:
                        cursor.close()
                    if conexion:
                        conexion.close()
                return True
        else:
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