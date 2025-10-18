from models import Administrador, Empleado, Gerente, InformeAdmin
from utils.validador import validar_rut
import datetime
from config import conectar_db
import mysql.connector


def crear_informe(admin: Administrador, emp: Empleado, gerente: Gerente):
    formatos_disp = {
        1: "pdf",
        2: "excel"
    }

    while True:
        print("Formatos disponibles:\n")
        print("1. PDF")
        print("2. Excel\n")

        try:
            formato_opcion = int(input("Ingrese el formato (1-2): "))
            if formato_opcion not in formatos_disp:
                print("Ingrese un formato válido.")
                continue
            formato = formatos_disp[formato_opcion]
            break
        except ValueError:
            print(f"Debe ingresar una de las opciones disponibles para continuar.")
    
    while True:
        try:
            rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
            if validar_rut(rut):
                break
            else:
                print("El RUT no ha sido validado correctamente.")
                return
        except ValueError as Error:
            print(f"Error inesperado: {Error}")

    while True:
        try:
            descripcion = input("Ingrese una descripcion al informe: ")
            if not descripcion:
                print("Ingrese una descripción válida")
                continue
            break
        except Exception as Error:
            print(f"Error inesperado: {Error}")

    while True:
        try:
            fecha_inicio = input("Ingrese la fecha del informe (formato DD/MM/AAAA): ")
            fecha = datetime.strptime(fecha_inicio, '%d/%m/%Y').date()
            print(f"Fecha ingresada correctamente: {fecha}")
            break
        except ValueError:
            print("Formato inválido. Use el formato DD/MM/AAAA.")
     
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        query = """
            INSERT INTO informe (descripcion, formato, fecha, rut_usuario)
            VALUES (%s, %s, %s, %s)
        """
        valores = (descripcion, formato, fecha, rut)
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Detalles del informe creado:\n")
        print(f"ID generado: {id_generado} | Formato: {formato} | Fecha: {fecha} | RUT: {rut}\nDescripción: {descripcion}\n")

        if admin:
            informe_nuevo = InformeAdmin(id_generado, descripcion, formato, fecha, rut)
            return informe_nuevo
        elif gerente:
            informe_nuevo = InformeGerente(id_generado, descripcion, formato, fecha, rut)
            return informe_nuevo
        elif emp:
            informe_nuevo = InformeEmpleado(id_generado, descripcion, formato, fecha, rut)
            return informe_nuevo
        else:
            print("No tienes un rol disponible para seguir con la acción.")
    except Exception as Error:
        print(f"Error al crear el informe: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def buscar_informe(admin: Administrador, emp: Empleado, gerente: Gerente):
    while True:
        try:
            id_informe = int(input("Ingrese la ID del informe que desea buscar: "))
            break
        except ValueError as Error:
            print(f"Entrada inválida: {Error}")
    
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT i.id_informe, i.descripcion, i.formato, i.fecha, i.rut_usuario, u.rol
            FROM informe i
            JOIN usuario_basico u ON i.rut_usuario = u.rut_usuario
            WHERE i.id_informe = %s
        """
        cursor.execute(query, (id_informe,))
        resultado = cursor.fetchone()

        if not resultado:
            print(f"No se ha encontrado ningún informe con la ID proporcionada: {id_informe}")
            return
        
        print("Informe encontrado con éxito: ")
        print(f"ID: {resultado['id_informe']}")
        print(f"Formato: {resultado['formato'].upper()}")
        print(f"Fecha: {resultado['fecha']}")
        print(f"RUT Usuario: {resultado['rut_usuario']}")
        print(f"Descripción: {resultado['descripcion']}")
        print(f"ROL: {resultado['rol'].capitalize()}")

        informe_nuevo = None
        if admin:
            informe_nuevo = InformeAdmin(
                resultado['id_informe'],
                resultado['descripcion'],
                resultado['formato'],
                resultado['fecha'],
                resultado['rut_usuario']
            )
        elif gerente:
            informe_nuevo = InformeGerente(
                resultado['id_informe'],
                resultado['descripcion'],
                resultado['formato'],
                resultado['fecha'],
                resultado['rut_usuario']
            )
        elif emp:
            informe_nuevo = InformeEmpleado(
                resultado['id_informe'],
                resultado['descripcion'],
                resultado['formato'],
                resultado['fecha'],
                resultado['rut_usuario']
            )
        else:
            print("No se pudo instanciar el informe: rol no reconocido.")

        return informe_nuevo

    except mysql.connector.Error as Error:
        print(f"Error inesperado: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def modificar_informe(admin: Administrador, emp: Empleado, gerente: Gerente):
    while True:
        try:
            id_informe = int(input("Ingrese la ID del informe que desea modificar: "))
            break
        except ValueError as Error:
            print(f"Entrada inválida: {Error}")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT i.id_informe, i.descripcion, i.formato, i.fecha, i.rut_usuario, u.rol
            FROM informe i
            JOIN usuario_basico u ON i.rut_usuario = u.rut_usuario
            WHERE i.id_informe = %s
        """
        cursor.execute(query, (id_informe,))
        informe = cursor.fetchone()

        if not informe:
            print(f"No se encontró ningún informe con la ID: {id_informe}")
            return

        print("Informe encontrado:\n")
        print(f"Descripción actual: {informe['descripcion']}")
        print(f"Formato actual: {informe['formato'].upper()}")
        print(f"Fecha actual: {informe['fecha']}")
        print(f"RUT Usuario: {informe['rut_usuario']}")
        print(f"Rol: {informe['rol'].capitalize()}\n")

        print("¿Qué campo desea modificar?")
        print("1. Descripción")
        print("2. Formato")
        print("3. Fecha")

        try:
            opcion = int(input("Seleccione una opción (1-3): "))
        except ValueError:
            print("Entrada inválida.")
            return

        campos = {
            1: "descripcion",
            2: "formato",
            3: "fecha"
        }

        if opcion not in campos:
            print("Opción inválida.")
            return

        campo = campos[opcion]
        nuevo_valor = None

        if campo == "descripcion":
            nuevo_valor = input("Ingrese la nueva descripción: ").strip()
            if not nuevo_valor:
                print("La descripción no puede estar vacía.")
                return
        elif campo == "formato":
            formatos_disp = {1: "pdf", 2: "excel"}
            print("Formatos disponibles:\n1. PDF\n2. Excel")
            try:
                formato_opcion = int(input("Seleccione el nuevo formato (1-2): "))
                if formato_opcion not in formatos_disp:
                    print("Formato inválido.")
                    return
                nuevo_valor = formatos_disp[formato_opcion]
            except ValueError:
                print("Entrada inválida.")
                return
        elif campo == "fecha":
            try:
                fecha_input = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
                nuevo_valor = datetime.strptime(fecha_input, "%d/%m/%Y").date()
            except ValueError:
                print("Formato de fecha inválido.")
                return

        confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
        if confirmacion != "s":
            print("Modificación cancelada.")
            return

        cursor.execute(f"UPDATE informe SET {campo} = %s WHERE id_informe = %s", (nuevo_valor, id_informe))
        conexion.commit()

        print("Modificación realizada con éxito.")

        informe_modificado = None
        if admin:
            informe_modificado = InformeAdmin(informe['id_informe'],
                                              informe['descripcion'],
                                              informe['formato'],
                                              informe['fecha'],
                                              informe['rut_usuario'])
        elif gerente:
            informe_modificado = InformeGerente(informe['id_informe'],
                                                informe['descripcion'],
                                                informe['formato'],
                                                informe['fecha'],
                                                informe['rut_usuario'])
        elif emp:
            informe_modificado = InformeEmpleado(informe['id_informe'],
                                                 informe['descripcion'],
                                                 informe['formato'],
                                                 informe['fecha'],
                                                 informe['rut_usuario'])

        return informe_modificado
    except Exception as Error:
        print(f"Error inesperado al modificar el informe: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def eliminar_informe(admin: Administrador, emp: Empleado, gerente: Gerente):
    while True:
        try:
            id_informe = int(input("Ingrese la ID del informe que desea eliminar: "))
            break
        except ValueError as Error:
            print(f"Entrada inválida. {Error}")
    
    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)

        query = """
            SELECT id_informe, descripcion, formato, fecha, rut_usuario
            FROM informe
            WHERE id_informe = %s
        """
        cursor.execute(query,(id_informe,))
        informe = cursor.fetchone()

        if not informe:
            print(f"No se encontró ningún informe con la ID ingresada: {id_informe}")
            return

        # Validación de propiedad de informe (para que cada rol solo borre sus propios informes.)

        rut_actual = None
        if admin:
            rut_actual = admin.rut
        elif gerente:
            rut_actual = gerente.rut_gerente
        elif emp:
            rut_actual = emp.rut
        else:
            print("No se ha encontrado ningún usuario o rol válidos para realizar la acción.")
            return
        
        if informe['rut_usuario'] != rut_actual:
            print("No tienes los permisos necesarios para eliminar este informe. (ROL denegado)")
            return
        
        print("Informe encontrado:\n")
        print(f"Descripción: {informe['descripcion']}")
        print(f"Formato: {informe['formato'].upper()}")
        print(f"Fecha: {informe['fecha']}")

        confirmacion = input("¿Está seguro de eliminar el informe seleccionado? (S/N): ").strip().lower()
        if confirmacion != "s":
            print("Eliminación cancelada.")
            return
        
        cursor.execute("DELETE FROM informe WHERE id_informe = %s", (id_informe,))
        conexion.commit()
    except Exception as Error:
        print(f"Informe con ID {id_informe} eliminado exitosamente.")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
