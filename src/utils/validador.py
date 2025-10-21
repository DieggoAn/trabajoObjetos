from config import conectar_db
import mysql.connector
import re 
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

def insertar_empleado_detalle(datos_detalle):

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query_detalle = """
            INSERT INTO usuario_detalle (
                rut_usuario, fecha_inicio_contrato,
                salario, rol, id_departamento
            ) VALUES (%s, %s, %s, %s, %s)
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

def insertar_empleado_completo(datos_basico, datos_detalle):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query_basico = """
            INSERT INTO usuario_basico (
                rut_usuario, nombres, apellido_paterno, apellido_materno,
                fecha_nacimiento, numero_telefonico, direccion , contraseña, email
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        query_detalle = """
            INSERT INTO usuario_detalle (
                rut_usuario, fecha_inicio_contrato,
                salario, rol, id_departamento
            ) VALUES (%s, %s, %s, %s, %s)
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




def validar_contraseña_segura(contraseña):
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    
    if not re.search(r"[A-Z]", contraseña):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
    
    if not re.search(r"[a-z]", contraseña):
        raise ValueError("La contraseña debe contener al menos una letra minúscula.")
    
    if not re.search(r"\d", contraseña):
        raise ValueError("La contraseña debe contener al menos un número.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        raise ValueError("La contraseña debe contener al menos un carácter especial.")
    
    return True

def buscar_empleado_general(rut):
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
            print("El usuario se encuentra registrado en el sistema.\n")
            return True
        else:
            print("El usuario no está registrado.")
            return False
    except Exception as e:
        print(f"Error inesperado al buscar el empleado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def buscar_proyecto_general(id_proyecto):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
            SELECT p.id_proyecto
            FROM proyecto p
            JOIN departamento d ON p.id_departamento = d.id_departamento
            WHERE p.id_proyecto = %s
        """
        cursor.execute(query, (id_proyecto,))
        resultado = cursor.fetchone()

        if resultado:
            print("El proyecto se encuentra registrado en el sistema.\n")
            return True
        else:
            print("No se encontró a ningún proyecto con esta ID.\n")
            return False
    except Exception as Error:
        print(f"Error inesperado al buscar el proyecto: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
