from .Persona import Persona
from models.interfaces.RegistroTiempoInterfaz import RegistroTiempoInterfaz
from .RegistroTiempo import RegistroTiempo
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz 
from config import conectar_db
from datetime import datetime
from functions.validador import (validar_rut,
                             buscar_empleado_general,
                             buscar_proyecto_general)

class Empleado(Persona, RegistroTiempoInterfaz, GestionInformeInterfaz):
    def __init__ (self, rut,direccion, fecha_inicio_contrato,salario,rol,id_departamento,email=None, nombres=None, apellido_paterno=None, apellido_materno=None, 
                 fecha_nacimiento=None,  telefono=None, contraseña=None):
        
        super().__init__(
        rut=rut,
        nombres=nombres,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        direccion=direccion, 
        fecha_nacimiento=fecha_nacimiento,
        fecha_inicio_contrato=fecha_inicio_contrato,
        salario=salario,
        telefono=telefono,
        contraseña=contraseña,
        rol=rol,
        id_departamento=id_departamento,
        email=email)
        

    def mostrar_rol(self):
        return f"ROL: Empleado\nID Departamento: {self.id_departamento}"

    def crearRegistroTiempo(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)

        resultado_rut = buscar_empleado_general(rut)

        if resultado_rut:
            while True:
                try:
                    id_proyecto = int(input("Ingrese la ID del proyecto para el registro de tiempo: "))
                    break
                except ValueError as Error:
                    print(f"Error inesperado: {Error}")
            
            resultado_pro = buscar_proyecto_general(id_proyecto)

            if resultado_pro:
                while True:
                    try:
                        fecha= input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
                        fecha1 = datetime.strptime(fecha, '%d/%m/%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha1}")
                        break
                    except ValueError:
                        print("Formato inválido. Use el formato DD/MM/AAAA.")

                while True:
                    try:
                        horas_trabajadas = int(input("Ingrese las horas trabajadas: "))
                        if 1 <= horas_trabajadas <= 999:
                            break
                        else:
                            print("El número puede tener solo hasta 3 dígitos.")
                    except ValueError:
                        print("Debe ingresar solo números enteros.")

                while True:
                    try:
                        descripcion = input("Agrege una descripcion al registro de tiempo: ")
                        if not descripcion:
                            raise ValueError("No puede quedar el campo vacio")
                        break 
                    except ValueError as Error:
                        print(Error)

                try:
                    conexion = conectar_db()
                    cursor = conexion.cursor()
                    query = """
                        INSERT INTO registro_tiempo (
                            fecha, horas_trabajadas, descripcion_tarea, 
                            rut_usuario, id_proyecto 
                        ) VALUES (%s, %s, %s, %s, %s)
                    """
                    valores = (
                        fecha, horas_trabajadas, descripcion, rut, id_proyecto
                    )
                    cursor.execute(query, valores)
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                    id_generado = cursor.lastrowid
                    print(f"Registro de tiempo creado con ID: {id_generado}")
                except Exception as e:
                    print(f"Error al guardar el registro de tiempo: {e}")
                finally:
                    if cursor:
                        cursor.close()
                    if conexion:
                        conexion.close()

            else:
                print("El proyecto no está registrado.")
        else:
            print("El usuario no está registrado.")

    def buscarRegistroTiempo(self):
        while True:
            try:
                id_registro_tiempo = int(input("Ingrese el ID del registro de tiempo a buscar: "))
                if not id_registro_tiempo:
                    raise ValueError("No puede dejar el campo vacio")
                break
            except ValueError as Error:
                print(f"Error inesperado al buscar la ID: {Error}")
            
        try:
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)

            query = "SELECT * FROM registro_tiempo WHERE id_registro_tiempo = %s"
            cursor.execute(query, (id_registro_tiempo,))
            registro = cursor.fetchone()

            if registro:
                print("\nRegistro encontrado:")
                print(f"ID: {registro['id_registro_tiempo']}")
                print(f"Fecha: {registro['fecha']}")
                print(f"Horas trabajadas: {registro['horas_trabajadas']}")
                print(f"Descripción: {registro['descripcion_tarea']}")
                print(f"RUT Usuario: {registro['rut_usuario']}")
                print(f"ID Proyecto: {registro['id_proyecto']}")
            else:
                print("\nNo se encontró ningún registro con esa ID.")
        except Exception as Error:
            print(f"Error inesperado al buscar el registro: {Error}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def eliminarRegistroTiempo(self):
        pass

    def modificarRegistroTiempo(self):
        pass

    """Métodos de Gestion de Informe Interfaz"""
    def crearInforme(self):
        print("\n--- Creación de Nuevo Informe (Empleado) ---")
        
        # 1. Obtener datos por input
        while True:
            descripcion = input("Ingrese la descripción del informe: ").strip()
            if descripcion:
                break
            print("Error: La descripción no puede estar vacía.")
        
        # 2. Obtener datos automáticos
        fecha_creacion = datetime.now().date()
        
        try:
            rut_admin = self.rut
        except AttributeError:
            print("Error: No se pudo obtener el RUT del administrador.")
            return

        # 3. Operación de Base de Datos
        conexion = None
        cursor = None
        
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            query = """
                INSERT INTO informe (descripcion, fecha, rut_usuario)
                VALUES (%s, %s, %s)
            """
            valores = (descripcion, fecha_creacion, rut_admin)
            cursor.execute(query, valores)
            conexion.commit()
            
            id_informe = cursor.lastrowid
            print(f"\n¡Éxito! Informe ID:{id_informe} creado exitosamente.")
            print(f"Autor: {rut_admin}")
            print(f"Fecha: {fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")

        except Exception as e:
            print(f"\nError al guardar el informe en la base de datos: {e}")
            if conexion:
                conexion.rollback() # Revertir cambios si algo falló
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def buscarInforme(self):
        print("\n--- Búsqueda de Informe ---")

        # 1. Obtener y validar el ID del informe (sin cambios)
        id_a_buscar = None
        while True:
            try:
                id_a_buscar = int(input("Ingrese el ID del informe a buscar: "))
                if id_a_buscar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")

        # 2. Operación de Base de Datos
        conexion = None
        cursor = None
        
        try:
            # --- INICIO DE LA MODIFICACIÓN ---

            # Obtenemos el RUT del usuario (manejando el error de tupla)
            mi_rut = self.rut
            # Definimos la consulta base y los valores
            query = """
                SELECT id_informe, descripcion, fecha, rut_usuario
                FROM informe
                WHERE id_informe = %s
            """
            valores = (id_a_buscar,)

            # Si el usuario NO es admin, añadimos una restricción a la consulta
            if self.rol.lower() != "administrador":
                query += " AND rut_usuario = %s"
                valores = (id_a_buscar, mi_rut)
            
            # --- FIN DE LA MODIFICACIÓN ---

            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            
            cursor.execute(query, valores)
            resultado = cursor.fetchone()

            # 3. Imprimir resultados
            if resultado:
                print("\n--- Informe Encontrado ---")
                print(f"ID Informe:  {resultado['id_informe']}")
                print(f"Autor (RUT): {resultado['rut_usuario']}")
                print(f"Fecha (YYYY-MM-DD): {resultado['fecha']}")
                print(f"Descripción: {resultado['descripcion']}")
            else:
                # Esta respuesta ahora cubre "no existe" y "no tienes permiso"
                print(f"\nNo se encontró ningún informe con el ID: {id_a_buscar} (o no tiene permisos para verlo).")

        except Exception as e:
            print(f"\nError al buscar el informe en la base de datos: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def modificarInforme(self):
        print("\n--- Modificación de Informe ---")

        # 1. Obtener ID a modificar
        id_a_modificar = None
        while True:
            try:
                id_a_modificar = int(input("Ingrese el ID del informe a modificar: "))
                if id_a_modificar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")

        # 2. Pedimos los nuevos datos ANTES de la conexión
        nueva_descripcion = ""
        while True:
            nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
            if nueva_descripcion:
                break
            print("Error: La descripción no puede estar vacía.")

        # Obtenemos la fecha actual (tipo DATE)
        nueva_fecha = datetime.now().date()

        # 3. Operación de Base de Datos
        conexion = None
        cursor = None
        
        try:
            # --- INICIO DE LA MODIFICACIÓN ---

            # Obtenemos el RUT del usuario (manejando el error de tupla)
            mi_rut = self.rut

            # 4. Construimos la consulta base
            query_actualizar = """
                UPDATE informe 
                SET descripcion = %s, fecha = %s 
                WHERE id_informe = %s
            """
            valores = (nueva_descripcion, nueva_fecha, id_a_modificar)

            # 5. Añadimos el filtro de seguridad para roles no-administradores
            if self.rol.lower() != "administrador":
                query_actualizar += " AND rut_usuario = %s"
                # Añadimos el RUT a la tupla de valores
                valores = (nueva_descripcion, nueva_fecha, id_a_modificar, mi_rut)
            
            # --- FIN DE LA MODIFICACIÓN ---

            conexion = conectar_db()
            cursor = conexion.cursor()

            # 6. EJECUTAR LA ACTUALIZACIÓN
            cursor.execute(query_actualizar, valores)
            conexion.commit()
            
            # 7. VERIFICAR EL RESULTADO
            if cursor.rowcount > 0:
                # rowcount > 0 significa que la actualización fue exitosa
                print("\n¡Éxito! El informe ha sido modificado.")
                print(f"ID: {id_a_modificar}")
                print(f"Nueva Fecha: {nueva_fecha}")
            else:
                # rowcount == 0 significa que el ID no se encontró O el RUT no coincidió
                print(f"\nNo se pudo modificar el informe (ID: {id_a_modificar}).")
                print("Verifique que el ID exista y que tenga permisos para modificarlo.")

        except Exception as e:
            print(f"\nError al modificar el informe: {e}")
            if conexion:
                conexion.rollback() # Revertir cambios si algo falló
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def eliminarInforme(self):
        pass

    def buscarProyecto(self):
        print("\n--- Búsqueda de Proyecto ---")

        id_a_buscar = None
        while True:
            try:
                id_a_buscar = int(input("Ingrese la ID del proyecto a buscar: "))
                if id_a_buscar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError as Error:
                print(f"Debe ingresar un carácter numérico para continuar: {Error}")

        conexion = None
        cursor = None

        try:
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)

            query = """
                SELECT p.id_proyecto, p.nombre, p.descripcion, p.fecha_inicio
                FROM proyecto p
                JOIN proyecto_has_usuario_detalle pud ON p.id_proyecto = pud.id_proyecto
                WHERE p.id_proyecto = %s AND pud.rut_usuario = %s;
            """
            valores = (id_a_buscar, self.rut)

            cursor.execute(query, valores)
            resultado = cursor.fetchone()

            if resultado:
                print("\n--- Proyecto Encontrado ---")
                print(f"ID Proyecto:     {resultado['id_proyecto']}")
                print(f"Nombre:          {resultado['nombre']}")
                print(f"Descripción:     {resultado['descripcion']}")
                print(f"Fecha de inicio: {resultado['fecha_inicio']}")
                print(f"Fecha de término:{resultado['fecha_fin']}")
            else:
                print(f"\nNo se encontró ningún proyecto con el ID: {id_a_buscar} (o no estás asignado a él).")

        except Exception as e:
            print(f"\nError al buscar el proyecto en la base de datos: {e}")

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()