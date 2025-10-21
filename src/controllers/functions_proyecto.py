from config import conectar_db
from models import Proyecto
from datetime import datetime


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

        proyecto_nuevo = Proyecto(id_generado, nombre, descripcion, fecha)
        return proyecto_nuevo
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
        nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip() #agregar un while True???

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