from .Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz
from models.interfaces.GestionDeptoInterfaz import GestionDeptoInterfaz
from .Empleado import Empleado
from .Gerente import Gerente
from config import conectar_db
import mysql.connector
import bcrypt
import re
import pwinput
from utils.validador import *
from datetime import datetime


class Administrador(Persona, GestionEmpInterfaz, GestionInformeInterfaz, GestionDeptoInterfaz):
    def __init__(self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono,contraseña, rut,rol, id_departamento):
        
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
            rol="Administrador",
            id_departamento=id_departamento)

    def __str__(self):
        return (
            f"Datos del Administrador\n"
            f"RUT: {self.rut}\n"
            f"Nombre(s): {self.nombres}\n"
            f"Apellidos: {self.apellido_paterno} {self.apellido_materno}\n"
            f"Departamento: {self.id_departamento}\n"
        )

    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    @property
    def rut(self):
        return self.__rut
    @rut.setter
    def rut(self, rut2):
        self.__rut = rut2
    @rut.deleter
    def rut(self):
        del self.__rut
 
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, rut):
        self.__direccion = rut
    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    @salario.deleter
    def salario(self):
        del self.__salario

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    @telefono.deleter
    def telefono(self):
        del self.__telefono

    def guardar_en_db(self):
        from config import conectar_db
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = """
                INSERT INTO usuario (
                    rut_usuario, nombres, apellido_paterno, apellido_materno,
                    direccion, fecha_nacimiento, fecha_inicio_contrato,
                    salario, numero_telefonico, rol, id_departamento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.rut, self.nombres, self.apellido_paterno, self.apellido_materno,
                self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
                self.salario, self.telefono, self.rol, self.id_departamento
            )
            cursor.execute(query, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Administrador guardado correctamente en la base de datos.")
        except Exception as e:
            print(f"Error al guardar al administrador: {e}")
        finally:
            cursor.close()
            conexion.close()

    def iniciarSesion(self):
        pass

    def cerrarSesion(self):
        self.estadoSesion = False


    # Nota: Esta funcion crea cualquier tipo de empleado, incluyendo Gerente y Administrador, o cualquiera que se quiera implementar a futuro.
    def crearEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                validar_rut(rut) # Asumo que esta función levanta ValueError si es inválido
                break
            except ValueError as Error:
                print(Error)
                
        roles_validos = {"empleado", "gerente", "administrador"}
        while True:
            try:
                rol_usuario = input("Ingrese el rol del usuario: ").strip().lower()
                if rol_usuario not in roles_validos:
                    raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
                
                # Capitaliza la primera letra para que coincida con la llave del diccionario
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
                    raise ValueError("Ingrese una dirección válida")
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
                # Se abre la conexión a la db
                conexion = conectar_db() 
                cursor = conexion.cursor()
                cursor.execute("SELECT id_departamento FROM departamento WHERE id_departamento = %s", (id_departamento,))
                if not cursor.fetchone():
                    print("El departamento ingresado no existe en el sistema.")
                    cursor.close()
                    conexion.close()
                    # Aquí deberías usar 'continue' para volver a pedir el ID, en lugar de 'return'
                    continue 
                
                if len(str(id_departamento)) > 15:
                    raise ValueError("Debe ser un número de hasta 15 dígitos.")
                
                cursor.close()
                conexion.close()
                break # Si el ID es válido y existe, rompemos el bucle
            except ValueError:
                    print("Debe ingresar carácteres numéricos.")

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
            "Gerente": Gerente,
            "Administrador": Administrador
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
                id_departamento=id_departamento
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
            nuevo_usuario.contraseña, # La clase padre guarda el hash en 'contraseña'
            nuevo_usuario.rol
        )

        datos_detalle = (
            nuevo_usuario.rut,
            nuevo_usuario.direccion,
            nuevo_usuario.fecha_inicio_contrato,
            nuevo_usuario.salario,
            nuevo_usuario.rol,
            nuevo_usuario.id_departamento
        )
        #para mayor persistencia y modularidad, se implementa la función insertar_empleado()
        insertar_empleado_completo(datos_basico, datos_detalle)
        print(f"Empleado {nombre} {apellido_paterno} creado exitosamente.")
        print(f"Rol: {rol_usuario} | RUT: {rut.upper()} | ID Departamento: {id_departamento}\n")

    def crearEmpleadoDetalle(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                validar_rut(rut) # Asumo que esta función levanta ValueError si es inválido
                break
            except ValueError as Error:
                print(Error)
                
        roles_validos = {"empleado", "gerente", "administrador"}
        while True:
            try:
                rol_usuario = input("Ingrese el rol del usuario: ").strip().lower()
                if rol_usuario not in roles_validos:
                    raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
                
                # Capitaliza la primera letra para que coincida con la llave del diccionario
                rol_usuario = rol_usuario.capitalize() 

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
                id_departamento = int(input("Ingrese ID del departamento asignado al empleado: "))
                # Se abre la conexión a la db
                conexion = conectar_db() 
                cursor = conexion.cursor()
                cursor.execute("SELECT id_departamento FROM departamento WHERE id_departamento = %s", (id_departamento,))
                if not cursor.fetchone():
                    print("El departamento ingresado no existe en el sistema.")
                    cursor.close()
                    conexion.close()
                    # Aquí deberías usar 'continue' para volver a pedir el ID, en lugar de 'return'
                    continue 
                
                if len(str(id_departamento)) > 15:
                    raise ValueError("Debe ser un número de hasta 15 dígitos.")
                
                cursor.close()
                conexion.close()
                break # Si el ID es válido y existe, rompemos el bucle
            except ValueError:
                    print("Debe ingresar carácteres numéricos.")

        clases_usuario = {
            "Empleado": Empleado,
            "Gerente": Gerente,
            "Administrador": Administrador
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
                direccion=direccion,
                fecha_inicio_contrato=fecha_inicio_contrato,
                salario=salario,
                rol=rol_usuario,                # <-- ¡Este era el que faltaba!
                id_departamento=id_departamento
            )
        except Exception as e:
            print(f"Error al crear el objeto: {e}")
            return
        #
        # --- ### FIN DE LA CORRECCIÓN ### ---
        #

        datos_detalle = (
            nuevo_usuario.rut,
            nuevo_usuario.direccion,
            nuevo_usuario.fecha_inicio_contrato,
            nuevo_usuario.salario,
            nuevo_usuario.rol,
            nuevo_usuario.id_departamento
        )
        #para mayor persistencia y modularidad, se implementa la función insertar_empleado()
        insertar_empleado_detalle( datos_detalle)
        print(f"Datos del empleado {rut} añadidos exitosamente.")
        print(f"Rol: {rol_usuario} | RUT: {rut.upper()} | ID Departamento: {id_departamento}\n")


    def mostrar_rol(self):
        print(f"Rol del usuario: Administrador")

    def super_buscar_empleado(self):
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

    def buscarEmpleado(self):
        pass

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

            cursor.execute("SELECT * FROM usuario_basico WHERE rut_usuario = %s", (rut,))
            empleado_basico = cursor.fetchone()
            cursor.execute("SELECT * FROM usuario_detalle WHERE rut_usuario = %s", (rut,))
            empleado_detalle = cursor.fetchone()
            if not empleado_basico or not empleado_detalle:
                print("No se encontró ningún empleado con ese RUT o su informacion esta incompleta.")
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

        try:
            opcion = int(input("Seleccione una opción (1-10): "))
            basico = [1,2,3,5,8]
            detalle = [4,6,7,9,10]
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

        # --- INICIO DE LA CORRECCIÓN ---
        
        # 1. Inicializamos las variables fuera del 'try'
        conexion = None
        cursor = None
        
        # 2. Un SOLO 'try' debe envolver TODA la operación
        try:
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            
            # 3. El SELECT (que antes estaba desprotegido) ahora está dentro
            cursor.execute(
                        "SELECT T1.nombres, T1.apellido_paterno, T2.rol "
                        "FROM usuario_basico AS T1 "
                        "JOIN usuario_detalle AS T2 ON T1.rut_usuario = T2.rut_usuario "
                        "WHERE T1.rut_usuario = %s", 
                        (rut,)
            )
            empleado = cursor.fetchone()

            if not empleado:
                print("No se encontró ningún empleado con ese RUT.")
                # 4. Se quitan los .close() de aquí. El 'finally' lo hará.
                return
            
            print("\nEmpleado encontrado:")
            print(f"Nombre: {empleado['nombres']} {empleado['apellido_paterno']}")
            print(f"Rol: {empleado['rol']}")

            confirmacion = input("¿Estás seguro que deseas eliminar este empleado? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
            if confirmacion != "s":
                print("Operación cancelada.")
                # 5. Se quitan los .close() de aquí. El 'finally' lo hará.
                return
            cursor.execute("UPDATE informe SET rut_usuario = NULL WHERE rut_usuario = %s", (rut,))
            # 6. Se ejecuta el DELETE (ya no necesita su propio 'try...finally')
            cursor.execute("DELETE FROM usuario_detalle WHERE rut_usuario = %s", (rut,))

            # 3. Borramos el registro "padre" de 'usuario_basico' (AL FINAL)
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

    def eliminarEmpleadoDeDep(self):
        pass


    def crearDepartamento(self):
        pass

    def buscarDepartamento(self):
        pass

    def modificarDepartamento(self):
        pass

    def eliminarDepartamento(self):
        pass


    def crearInforme(self):
            """
            Permite al Administrador crear un nuevo registro de informe
            en la base de datos.
            """
            print("\n--- Creación de Nuevo Informe (Admin) ---")
            
            # 1. Obtener datos por input
            while True:
                descripcion = input("Ingrese la descripción del informe: ").strip()
                if descripcion:
                    break
                print("Error: La descripción no puede estar vacía.")

            while True:
                formato = input("Ingrese el formato (ej: PDF, CSV, Excel): ").strip().upper()
                if formato:
                    break
                print("Error: El formato no puede estar vacío.")
            
            # 2. Obtener datos automáticos
            fecha_creacion = datetime.now().date()
            
            # Asumimos que el RUT está guardado en self.rut gracias al __init__
            # (Si usaste una variable privada, podría ser self._rut)
            try:
                rut_admin = self.rut[0]
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
                    INSERT INTO informe (descripcion, formato, fecha, rut_usuario)
                    VALUES (%s, %s, %s, %s)
                """
                valores = (descripcion, formato, fecha_creacion, rut_admin)
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
            """
            Busca un informe en la base de datos por su ID
            e imprime los detalles.
            """
            print("\n--- Búsqueda de Informe ---")

            # 1. Obtener y validar el ID del informe
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
                conexion = conectar_db()
                # Usamos dictionary=True para obtener resultados como diccionarios
                cursor = conexion.cursor(dictionary=True)

                query = """
                    SELECT id_informe, descripcion, formato, fecha, rut_usuario
                    FROM informe
                    WHERE id_informe = %s
                """
                
                cursor.execute(query, (id_a_buscar,))
                resultado = cursor.fetchone()

                # 3. Imprimir resultados
                if resultado:
                    print("\n--- Informe Encontrado ---")
                    print(f"ID Informe:  {resultado['id_informe']}")
                    print(f"Autor (RUT): {resultado['rut_usuario']}")
                    print(f"Fecha (YYYY-MM-DD): {resultado['fecha']}")
                    print(f"Formato:     {resultado['formato']}")
                    print(f"Descripción: {resultado['descripcion']}")
                else:
                    print(f"\nNo se encontró ningún informe con el ID: {id_a_buscar}")

            except Exception as e:
                print(f"\nError al buscar el informe en la base de datos: {e}")
            
            finally:
                if cursor:
                    cursor.close()
                if conexion:
                    conexion.close()

    def modificarInforme(self):
        """
        Busca un informe por ID y actualiza su descripción y fecha.
        """
        print("\n--- Modificación de Informe ---")

        # 1. Obtener y validar el ID del informe
        id_a_modificar = None
        while True:
            try:
                id_a_modificar = int(input("Ingrese el ID del informe a modificar: "))
                if id_a_modificar > 0:
                    break
                print("Error: El ID debe ser un número positivo.")
            except ValueError:
                print("Error: Debe ingresar un valor numérico.")

        # 2. Operación de Base de Datos
        conexion = None
        cursor = None
        
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            # 3. VERIFICAR SI EL INFORME EXISTE
            query_verificar = "SELECT id_informe FROM informe WHERE id_informe = %s"
            cursor.execute(query_verificar, (id_a_modificar,))
            resultado = cursor.fetchone()

            if not resultado:
                print(f"\nNo se encontró ningún informe con el ID: {id_a_modificar}")
                return # Salimos de la función si no existe
            
            # 4. SI EXISTE, PEDIMOS NUEVOS DATOS
            print("Informe encontrado. Ingrese los nuevos datos.")
            
            nueva_descripcion = ""
            while True:
                nueva_descripcion = input("Ingrese la nueva descripción: ").strip()
                if nueva_descripcion:
                    break
                print("Error: La descripción no puede estar vacía.")

            # Obtenemos la fecha actual (tipo DATE)
            nueva_fecha = datetime.now().date()

            # 5. EJECUTAR LA ACTUALIZACIÓN
            query_actualizar = """
                UPDATE informe 
                SET descripcion = %s, fecha = %s 
                WHERE id_informe = %s
            """
            valores = (nueva_descripcion, nueva_fecha, id_a_modificar)
            
            cursor.execute(query_actualizar, valores)
            conexion.commit()
            
            print("\n¡Éxito! El informe ha sido modificado.")
            print(f"ID: {id_a_modificar}")
            print(f"Nueva Fecha: {nueva_fecha}")

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

    
    def crearProyecto(self):
        pass

    def buscarProyecto(self):
        pass

    def modificarProyecto(self):
        pass

    def eliminarProyecto(self):
        pass

    def asignar_emp_a_proyecto(self, id_proyecto, rut_usuario):
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = "INSERT INTO proyecto_has_usuario_detalle (id_proyecto, rut_usuario) VALUES (%s, %s)"
            cursor.execute(query, (id_proyecto, rut_usuario))
            conexion.commit()
            print("Usuario asignado al proyecto correctamente.")
        except mysql.connector.Error as Error:
            print(f"Error inesperado al realizar la acción: {Error}")
        finally:
            cursor.close()
            conexion.close()

