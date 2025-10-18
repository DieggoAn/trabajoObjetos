from config import conectar_db
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


