from .Persona import Persona
from .Empleado import Empleado
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionProyectoInterfaz import GestionProyectoInterfaz
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz
from config import conectar_db
from utils.validador import *
from datetime import datetime
import re
import pwinput
import bcrypt

class Gerente(Persona, GestionEmpInterfaz, GestionProyectoInterfaz, GestionInformeInterfaz):
    def __init__ (self, rut, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, contraseña, rol, email , id_departamento):
        
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
            contraseña=contraseña ,
            rol="Gerente",
            email=email,
            id_departamento=id_departamento
)

    def mostrar_rol(self):
        return f"ROL: Gerente\nID Departamento: {self.id_departamento}"
    
    def supervisarDepartamento(self):
        print("Supervisión registrada")

    def evaluarEmpleado(self):
        print("Evaluación a empleado registrado")

    """Metodos de la interfaz de gestión de empleados"""
    def crearEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                validar_rut(rut) # Asumo que esta función levanta ValueError si es inválido
                break
            except ValueError as Error:
                print(Error)
                
        rol_usuario = "Empleado"        
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
                    raise ValueError("Ingrese una dirección válida")
                break
            except ValueError as Error:
                print(Error)

        while True:
            try:
                fecha_nac = input("Ingrese la fecha de nacimiento del empleado (formato DD/MM/AAAA): ")
                fecha_nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y').date()
                print(f"Fecha ingresada correctamente: {fecha_nac}")
                break
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")

        while True:
            try:
                fecha_con = input("Ingrese la fecha de inicio del contrato del empleado (formato DD/MM/AAAA): ")
                fecha_inicio_contrato = datetime.strptime(fecha_con, '%d/%m/%Y').date()
                print(f"Fecha ingresada correctamente: {fecha_con}")
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
        id_departamento = self.id_departamento
        while True:
            try:
                email = input("Ingrese el email del empleado (ej: usuario@dominio.cl): ").strip()
                patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"               
                if not re.match(patron, email):
                    raise ValueError("Formato de email inválido. Intente nuevamente.")               
                break  
                
            except ValueError as Error:
                print(Error)
        while True:
            try:
                contraseña_texto_plano = pwinput.pwinput("Ingrese la contraseña para el nuevo empleado: ", mask = "*")
                if validar_contraseña_segura(contraseña_texto_plano):
                    contraseña_hash = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    break
            except ValueError as Error:
                # Asumo que validar_contraseña_segura levanta ValueError
                print(Error)
            except Exception as Error: 
                print(f"Error inesperado al guardar la contraseña: {Error}")

        clases_usuario = {
            "Empleado": Empleado,
        }

        # (Manejo de conexión temporalmente movido a la función de inserción)
        # (Es mejor práctica pasar la conexión a la función de inserción)
        
        # --- ### INICIO DE LA CORRECCIÓN ### ---
        #
        # Aquí usamos "argumentos por palabra clave" (ej: rut=...)
        # para asegurarnos de que pasamos todos los 12 argumentos
        # a la clase correcta y con los nombres correctos.
        #
        try:
            nuevo_usuario: Persona = clases_usuario[rol_usuario](
                rut=rut.upper(),
                nombres=nombre,                 # La clase espera 'nombres'
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                fecha_inicio_contrato=fecha_inicio_contrato,
                salario=salario,
                telefono=nro_telefono,          # La clase espera 'telefono'
                contraseña=contraseña_hash,     # La clase espera 'contraseña'
                rol=rol_usuario,                # <-- ¡Este era el que faltaba!
                id_departamento=id_departamento,
                email=email
            )
        except Exception as e:
            print(f"Error al crear el objeto: {e}")
            return
        #
        # --- ### FIN DE LA CORRECCIÓN ### ---
        #

        datos_basico = (
            nuevo_usuario.rut,
            nuevo_usuario.nombres,
            nuevo_usuario.apellido_paterno,
            nuevo_usuario.apellido_materno,
            nuevo_usuario.fecha_nacimiento,
            nuevo_usuario.telefono,
            nuevo_usuario.direccion,
            nuevo_usuario.contraseña, # La clase padre guarda el hash en 'contraseña'
            nuevo_usuario.email
        )

        datos_detalle = (
            nuevo_usuario.rut,
            nuevo_usuario.fecha_inicio_contrato,
            nuevo_usuario.salario,
            nuevo_usuario.rol,
            nuevo_usuario.id_departamento
        )
        #para mayor persistencia y modularidad, se implementa la función insertar_empleado()
        insertar_empleado_completo(datos_basico, datos_detalle)
        print(f"Empleado {nombre} {apellido_paterno} creado exitosamente.")
        print(f"Rol: {rol_usuario} | RUT: {rut.upper()} | ID Departamento: {id_departamento}\n")


    def super_buscar_empleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)
        id_departamento_gerente = self.id_departamento
        conexion = conectar_db()
        cursor = conexion.cursor()
        query = """
                SELECT ub.rut_usuario, ub.nombres, ub.apellido_paterno, ub.apellido_materno,
                    ub.direccion, ub.fecha_nacimiento, ud.fecha_inicio_contrato,
                    ud.salario, ub.numero_telefonico, ud.rol, ud.id_departamento, ub.email
                FROM usuario_basico ub
                JOIN usuario_detalle ud ON ub.rut_usuario = ud.rut_usuario
                WHERE ub.rut_usuario = %s AND ud.id_departamento = %s
                """
        
        # 1. Crear una tupla con AMBOS valores en el orden correcto
        valores = (rut, id_departamento_gerente)
        
        # 2. Pasar la nueva tupla 'valores'
        cursor.execute(query, valores)
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
            print("No se encontró a ningún empleado con ese RUT o no pertenece a su departamento.\n")

    def buscarEmpleado(self):
        return super().buscarEmpleado()

    def modificarEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado a modificar: ").strip().upper()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            id_departamento_gerente = self.id_departamento

            cursor.execute("SELECT * FROM usuario_basico WHERE rut_usuario = %s", (rut,))
            empleado_basico = cursor.fetchone()
            
            query_detalle = """
                SELECT * FROM usuario_detalle 
                WHERE rut_usuario = %s AND id_departamento = %s
            """
            valores_detalle = (rut, id_departamento_gerente)
            
            cursor.execute(query_detalle, valores_detalle)
            empleado_detalle = cursor.fetchone()

            if not empleado_basico or not empleado_detalle:
                print("No se encontró ningún empleado con ese RUT o no pertenece a su departamento.")
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
            print("9. ID Departamento")
        except Exception as e:
            print(f"Error al guardar el empleado: {e}")

        try:
            opcion = int(input("Seleccione una opción (1-10): "))
            basico = [1,2,3,5,8]
            detalle = [4,6,7,9]
            campos = {
                1: "nombres",
                2: "apellido_paterno",
                3: "apellido_materno",
                4: "direccion",
                5: "fecha_nacimiento",
                6: "fecha_inicio_contrato",
                7: "salario",
                8: "numero_telefonico",
                9: "id_departamento"
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
            if opcion in basico:
                query = f"UPDATE usuario_basico SET {campo} = %s WHERE rut_usuario = %s"
            elif opcion in detalle:
                query = f"UPDATE usuario_detalle SET {campo} = %s WHERE rut_usuario = %s"
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


    def eliminarEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado a eliminar (ej: 12345678-K): ").strip().lower()
                if validar_rut(rut):
                    rut = rut.upper()
                    break
            except ValueError as Error:
                print(Error)

        conexion = None
        cursor = None
        
        try:
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return 

            cursor.execute(
                "SELECT T1.nombres, T1.apellido_paterno, T2.rol, T2.id_departamento " 
                "FROM usuario_basico AS T1 "
                "JOIN usuario_detalle AS T2 ON T1.rut_usuario = T2.rut_usuario "
                "WHERE T1.rut_usuario = %s", 
                (rut,)
            )
            empleado = cursor.fetchone()

            if not empleado:
                print("No se encontró ningún empleado con ese RUT.")
                return
            
            if empleado['id_departamento'] != id_depto_gerente:
                print("\nOperación denegada. No tiene permisos para eliminar a este empleado.")
                print(f"El empleado (RUT: {rut}) no pertenece a su departamento (ID: {id_depto_gerente}).")
                return 

            print("\nEmpleado encontrado:")
            print(f"Nombre: {empleado['nombres']} {empleado['apellido_paterno']}")
            print(f"Rol: {empleado['rol']}")

            confirmacion = input("¿Estás seguro que deseas eliminar este empleado? (S/N): ").strip().lower()
            if confirmacion != "s":
                print("Operación cancelada.")
                return
            cursor.execute("UPDATE informe SET rut_usuario = NULL WHERE rut_usuario = %s", (rut,))
            
            cursor.execute("DELETE FROM usuario_detalle WHERE rut_usuario = %s", (rut,))

            cursor.execute("DELETE FROM usuario_basico WHERE rut_usuario = %s", (rut,)) 
            
            conexion.commit()
            print(f"El empleado con RUT {rut} ha sido eliminado de forma permanente.\n")

        except Exception as e:
            print(f"Error inesperado al eliminar: {e}")
            if conexion:
                conexion.rollback() 
                
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def crearInforme(self):
        while True:
            descripcion = input("Ingrese la descripción del informe: ").strip()
            if descripcion:
                break
            print("Error: La descripción no puede estar vacía.")

        fecha_creacion = datetime.now().date()
        
        try:
            rut_admin = self.rut
        except AttributeError:
            print("Error: No se pudo obtener el RUT del gerente.")
            return

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

        id_a_buscar = None
        while True:
            try:
                id_a_buscar = int(input("Ingrese el ID del informe a buscar: "))
                if id_a_buscar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")

        conexion = None
        cursor = None
        
        try:
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return 
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            query = """
                SELECT i.id_informe, i.descripcion, i.fecha, i.rut_usuario
                FROM informe AS i
                JOIN usuario_detalle AS ud ON i.rut_usuario = ud.rut_usuario
                WHERE i.id_informe = %s AND ud.id_departamento = %s
            """
            
            valores = (id_a_buscar, id_depto_gerente)
            
            cursor.execute(query, valores)
            resultado = cursor.fetchone()
            
            if resultado:
                print("\n--- Informe Encontrado ---")
                print(f"ID Informe:  {resultado['id_informe']}")
                print(f"Autor (RUT): {resultado['rut_usuario']}")
                print(f"Fecha (YYYY-MM-DD): {resultado['fecha']}")
                print(f"Descripción: {resultado['descripcion']}")
            else:
                print(f"\nNo se encontró ningún informe con el ID: {id_a_buscar} (o no pertenece a su departamento).")

        except Exception as e:
            print(f"\nError al buscar el informe en la base de datos: {e}")
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def modificarInforme(self):

        print("\n--- Modificación de Informe (Gerente) ---")

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
        # (Es una buena práctica no mantener la conexión abierta mientras se espera al usuario)
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
            # 4. Obtenemos el ID de departamento del Gerente (self)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return # Salimos de la función

            conexion = conectar_db()
            cursor = conexion.cursor()

            # 5. EJECUTAR LA ACTUALIZACIÓN RESTRINGIDA
            # Este query une 'informe' y 'usuario_detalle'.
            # Solo actualiza 'informe' (alias 'i') si TODAS
            # las condiciones del WHERE (ID y Depto.) se cumplen.
            query_actualizar = """
                UPDATE informe AS i
                JOIN usuario_detalle AS ud ON i.rut_usuario = ud.rut_usuario
                SET 
                    i.descripcion = %s, 
                    i.fecha = %s 
                WHERE 
                    i.id_informe = %s AND ud.id_departamento = %s
            """
            valores = (nueva_descripcion, nueva_fecha, id_a_modificar, id_depto_gerente)
            
            cursor.execute(query_actualizar, valores)
            conexion.commit()
            
            # 6. VERIFICAR EL RESULTADO
            # cursor.rowcount nos dice cuántas filas fueron afectadas
            if cursor.rowcount > 0:
                print("\n¡Éxito! El informe ha sido modificado.")
                print(f"ID: {id_a_modificar}")
                print(f"Nueva Fecha: {nueva_fecha}")
            else:
                # Si rowcount es 0, significa que el ID no existía O no tenía permisos
                print(f"\nNo se pudo modificar el informe (ID: {id_a_modificar}).")
                print("Verifique que el ID exista y que pertenezca a su departamento.")

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
        """
        (Gerente) Elimina un informe de la base de datos por su ID.
        Solo puede borrar informes si el autor pertenece a su departamento.
        """
        print("\n--- Eliminación de Informe (Gerente) ---")

        # 1. Obtener y validar el ID del informe
        id_a_borrar = None
        while True:
            try:
                id_a_borrar = int(input("Ingrese el ID del informe a eliminar: "))
                if id_a_borrar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")

        # 2. Operación de Base de Datos
        conexion = None
        cursor = None
        
        try:
            # 3. Obtenemos el ID de departamento del Gerente (self)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return 

            conexion = conectar_db()
            cursor = conexion.cursor()

            # 4. Pedir confirmación
            confirmacion = input(f"¿Confirmas eliminar el informe ID: {id_a_borrar} (si pertenece a su dpto.)? (S/N): ").strip().lower()
            if confirmacion != "s":
                print("Eliminación cancelada.")
                return

            # 5. EJECUTAR LA ELIMINACIÓN RESTRINGIDA
            # Este query une 'informe' y 'usuario_detalle'
            # y solo borra de 'informe' (alias 'i') si AMBAS
            # condiciones del WHERE se cumplen.
            query_eliminar = """
                DELETE i FROM informe AS i
                JOIN usuario_detalle AS ud ON i.rut_usuario = ud.rut_usuario
                WHERE i.id_informe = %s AND ud.id_departamento = %s
            """
            valores = (id_a_borrar, id_depto_gerente)
            
            cursor.execute(query_eliminar, valores)
            conexion.commit()
            
            # 6. VERIFICAR RESULTADO
            if cursor.rowcount > 0:
                # Se borró al menos 1 fila
                print("\n¡Éxito! El informe ha sido eliminado.")
            else:
                # No se borró nada (ID no existe O no tenía permisos)
                print(f"\nNo se eliminó el informe (ID: {id_a_borrar}).")
                print("Motivo: El ID no existe o no pertenece a su departamento.")

        except Exception as e:
            print(f"\nError al eliminar el informe: {e}")
            if conexion:
                conexion.rollback() 
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    """Metodos de la interfaz de gestión de proyectos"""
    def crearProyecto(self):
        while True:
            try: 
                nombre = input("Ingrese el nombre del proyecto: ")
                if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                    print("Ingrese un nombre valido")
                    continue
                nombre = ' '.join(nombre.split()).title()
                break
            except Exception as Error:
                print(f"Error inesperado: {Error}")
        
        # ... (Tu segundo 'while True' para 'descripcion' - sin cambios) ...
        while True:
            try:
                descripcion = input("Ingrese una descripcion al proyecto: ")
                if not descripcion:
                    print("Ingrese una descripcion valida")
                    continue
                break
            except Exception as Error:
                print(f"Error inesperado: {Error}")

        # ... (Tu tercer 'while True' para 'fecha_inicio' - sin cambios) ...
        while True:
            try:
                fecha_inicio = input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
                fecha = datetime.strptime(fecha_inicio, '%d/%m/%Y').date()
                print(f"Fecha ingresada correctamente: {fecha}")
                break
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")
            
        # --- INICIO DE LA MODIFICACIÓN ---
        
        conexion = None
        cursor = None
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            
            # 1. Verificación de nombre (sin cambios)
            cursor.execute("SELECT id_proyecto FROM proyecto WHERE LOWER(nombre) = %s", (nombre.lower(),))
            if cursor.fetchone():
                print("Ya existe un proyecto con ese nombre.")
                return
    
            # 2. PASO 1: Insertar en la tabla 'proyecto'
            query_proyecto = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
            valores_proyecto = (nombre, descripcion, fecha)
            cursor.execute(query_proyecto, valores_proyecto)
            
            # 3. Obtenemos el ID del proyecto que acabamos de crear
            id_generado = cursor.lastrowid
            
            # 4. PASO 2: Obtener el RUT del usuario 'self' (manejando la tupla)
            mi_rut = self.rut
            if isinstance(mi_rut, tuple):
                 mi_rut = mi_rut[0] # Arreglo del problema de la tupla

            # 5. PASO 3: Insertar en la tabla de enlace 'proyecto_has_usuario_detalle'
            print(f"Vinculando proyecto ID: {id_generado} al usuario RUT: {mi_rut}...")
            query_link = "INSERT INTO proyecto_has_usuario_detalle (id_proyecto, rut_usuario) VALUES (%s, %s)"
            valores_link = (id_generado, mi_rut)
            cursor.execute(query_link, valores_link)

            # 6. PASO 4: Confirmar AMBAS inserciones (Transacción)
            # (El commit se movió aquí, al final)
            conexion.commit() 
            
            print(f"\nDetalles del proyecto creado:")
            print(f"Nombre: {nombre} | ID: {id_generado} | Vinculado a: {mi_rut}")


        except Exception as Error:
            print(f"Error al crear el proyecto: {Error}")
            # Añadimos rollback para deshacer AMBOS inserts si algo falla
            if conexion:
                conexion.rollback()
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


    def buscarProyecto(self):
        while True:
            try:
                id_proyecto = int(input("Ingrese la ID del proyecto que desea buscar: "))
                break
            except ValueError as Error:
                print(f"Error inesperado: {Error}")

        conexion = None
        cursor = None
        
        try:
            # --- INICIO DE LA MODIFICACIÓN ---

            # 1. Obtenemos el ID de departamento del Gerente (self)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return # Salimos de la función

            # --- FIN DE LA MODIFICACIÓN ---

            conexion = conectar_db()
            cursor = conexion.cursor() # Mantenido como cursor estándar para que 'zip' funcione

            # --- INICIO DE LA MODIFICACIÓN (QUERY) ---
            
            # 2. Query arreglado:
            # - Usa INNER JOIN (más eficiente para esta restricción).
            # - Selecciona 'd.nombre' para que coincida con tu bucle print.
            # - Añade la restricción 'ud.id_departamento = %s' al WHERE.
            query = """
                SELECT 
                    p.id_proyecto, 
                    p.nombre, 
                    p.descripcion, 
                    p.fecha_inicio, 
                    ud.id_departamento, 
                    d.nombre AS nombre_departamento 
                FROM 
                    proyecto AS p
                JOIN 
                    proyecto_has_usuario_detalle AS phu ON p.id_proyecto = phu.id_proyecto
                JOIN 
                    usuario_detalle AS ud ON phu.rut_usuario = ud.rut_usuario
                JOIN 
                    departamento AS d ON ud.id_departamento = d.id_departamento
                WHERE 
                    p.id_proyecto = %s AND ud.id_departamento = %s;
                """
            
            # 3. Se pasan AMBOS valores al 'execute'
            valores = (id_proyecto, id_depto_gerente)
            cursor.execute(query, valores)
            resultado = cursor.fetchone()

            # --- FIN DE LA MODIFICACIÓN (QUERY) ---

            if resultado:
                print("\nDatos del proyecto encontrado:")
                campos = [
                    "ID Proyecto",
                    "Nombre",
                    "Descripcion",
                    "Fecha de inicio",
                    "ID Departamento",
                    "Nombre del departamento"
                ]      
                # Tu bucle 'zip' ahora funcionará correctamente
                for campo, valor in zip(campos, resultado):
                    print(f"{campo}: {valor}")
            else:
                # 4. Mensaje de error actualizado
                print("No se encontró ningún proyecto con esta ID o no pertenece a su departamento.\n")
                
        except Exception as Error:
            print(f"Error inesperado al buscar el proyecto: {Error}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def modificarProyecto(self):
        while True:
            try:
                id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
                break
            except ValueError as Error:
                print(f"Entrada inválida: {Error}")

        conexion = None
        cursor = None
        
        try:
            # --- INICIO DE LA MODIFICACIÓN ---

            # 1. Obtenemos el ID de departamento del Gerente (self)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return # Salimos de la función

            # --- FIN DE LA MODIFICACIÓN ---

            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)

            # --- INICIO DE LA MODIFICACIÓN (QUERY) ---
            
            # 2. Modificamos el SELECT para que SOLO encuentre el proyecto
            #    si pertenece al departamento del Gerente.
            #    Usamos DISTINCT por si el proyecto tiene varios usuarios del mismo depto.
            query_verificar = """
                SELECT DISTINCT p.*
                FROM proyecto AS p
                JOIN proyecto_has_usuario_detalle AS phu ON p.id_proyecto = phu.id_proyecto
                JOIN usuario_detalle AS ud ON phu.rut_usuario = ud.rut_usuario
                WHERE p.id_proyecto = %s AND ud.id_departamento = %s
            """
            valores_verificar = (id_proyecto, id_depto_gerente)
            
            cursor.execute(query_verificar, valores_verificar)
            proyecto = cursor.fetchone()

            # 3. Mensaje de error actualizado
            if not proyecto:
                print("No se encontró ningún proyecto con esa ID o no pertenece a su departamento.")
                return

            # --- FIN DE LA MODIFICACIÓN (QUERY) ---
            
            # 4. SI EXISTE Y TIENE PERMISOS, el resto del código continúa igual
            print("\nProyecto encontrado. ¿Qué campo desea modificar?")
            print("1. Nombre")
            print("2. Descripción")
            print("3. Fecha de inicio\n")

            try:
                opcion = int(input("Seleccione una opción (1-3): "))
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                return
            
            campos = { 1: "nombre", 2: "descripcion", 3: "fecha_inicio" }

            if opcion not in campos:
                print("Opción inválida.")
                return

            campo = campos[opcion]
            print(f"Valor actual de '{campo}': {proyecto[campo]}")
            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip()

            # ... (Validaciones de nombre, descripcion, fecha_inicio - sin cambios) ...
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

            # ... (Confirmación 'S/N' - sin cambios) ...
            while True:
                confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
                if confirmacion == "s":
                    break
                elif confirmacion == "n":
                    print("Modificación cancelada.")
                    return
                else:
                    print("Entrada inválida. Debes ingresar 'S' o 'N'.")

            # 5. El UPDATE no necesita cambiarse, porque ya validamos el permiso
            #    en el SELECT inicial.
            #    (ADVERTENCIA: este f-string es vulnerable a Inyección SQL)
            query = f"UPDATE proyecto SET {campo} = %s WHERE id_proyecto = %s"
            cursor.execute(query, (nuevo_valor, id_proyecto))
            conexion.commit()
            print("Modificación realizada con éxito.")

        except ValueError as Error:
            print(f"Error: {Error}")
        except Exception as e:
            print(f"Error inesperado al modificar el proyecto: {e}")
            if conexion:
                conexion.rollback() # Añadido rollback por seguridad
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def eliminarProyecto(self):
        while True:
            try:
                id_proyecto = int(input("Ingrese la ID del proyecto que desea eliminar: "))
                break
            except ValueError as Error:
                print(f"Error inesperado: {Error}")
    
        conexion = None
        cursor = None
        
        try:
            # --- INICIO DE LA MODIFICACIÓN (PERMISOS) ---
            
            # 1. Obtenemos el ID de departamento del Gerente (self)
            try:
                id_depto_gerente = self.id_departamento
                if id_depto_gerente is None:
                    raise AttributeError("Usted no está asignado a un departamento.")
            except AttributeError as e:
                print(f"Error de permisos: {e}")
                return # Salimos de la función

            # --- FIN DE LA MODIFICACIÓN (PERMISOS) ---

            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)

            # --- INICIO DE LA MODIFICACIÓN (QUERY) ---

            # 2. Modificamos el SELECT para que SOLO encuentre el proyecto
            #    si pertenece al departamento del Gerente.
            query_verificar = """
                SELECT DISTINCT p.id_proyecto, p.nombre, p.descripcion
                FROM proyecto AS p
                JOIN proyecto_has_usuario_detalle AS phu ON p.id_proyecto = phu.id_proyecto
                JOIN usuario_detalle AS ud ON phu.rut_usuario = ud.rut_usuario
                WHERE p.id_proyecto = %s AND ud.id_departamento = %s
            """
            valores_verificar = (id_proyecto, id_depto_gerente)

            cursor.execute(query_verificar, valores_verificar)
            proyecto = cursor.fetchone()

            # 3. Mensaje de error actualizado
            if not proyecto:
                print(f"No se encontró ningún proyecto con la ID: {id_proyecto} (o no pertenece a su departamento).")
                return
            
            # --- FIN DE LA MODIFICACIÓN (QUERY) ---
            
            # 4. SI EXISTE Y TIENE PERMISOS, el resto del código continúa
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
            
            # --- INICIO DE LA MODIFICACIÓN (DELETE) ---
            
            # 5. PASO 1: Borramos los "hijos" (enlaces) para evitar error de integridad
            cursor.execute("DELETE FROM proyecto_has_usuario_detalle WHERE id_proyecto = %s", (id_proyecto,))
            
            # 6. PASO 2: Borramos el "padre" (proyecto)
            cursor.execute("DELETE FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
            
            # 7. PASO 3: Confirmamos AMBAS eliminaciones
            conexion.commit()
            
            # --- FIN DE LA MODIFICACIÓN (DELETE) ---

            print(f"\nEl proyecto ha sido eliminado exitosamente.")
            print(f"ID: {id_proyecto}")
            print(f"Nombre: {proyecto['nombre']}")
            print(f"Descripción: {proyecto['descripcion']}")

        except Exception as Error:
            print(f"Error inesperado: {Error}")
            # 8. Añadimos rollback por seguridad
            if conexion:
                conexion.rollback()
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def asignar_emp_a_proyecto(self, id_proyecto, rut_usuario):
        # (Esta función no se modifica)
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = "INSERT INTO proyecto_has_usuario_detalle (id_proyecto, rut_usuario) VALUES (%s, %s)"
            cursor.execute(query, (id_proyecto, rut_usuario))
            conexion.commit()
            print("Usuario asignado al proyecto correctamente.")
        except Exception as Error: # (Cambiado a 'Exception' genérica)
            print(f"Error inesperado al realizar la acción: {Error}")
        finally:
            if cursor: # (Faltaba 'if cursor:')
                cursor.close()
            if conexion: # (Faltaba 'if conexion:')
                conexion.close()

