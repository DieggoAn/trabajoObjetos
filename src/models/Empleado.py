from .Persona import Persona
from models.interfaces.RegistroTiempoInterfaz import RegistroTiempoInterfaz
from .RegistroTiempo import RegistroTiempo
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz 
from config import conectar_db
from datetime import datetime

class Empleado(Persona, RegistroTiempoInterfaz, GestionInformeInterfaz):
    def __init__ (self, rut,direccion, fecha_inicio_contrato,salario,rol,id_departamento, nombres=None, apellido_paterno=None, apellido_materno=None, 
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
        id_departamento=id_departamento)
        
        ##self.registro = RegistroTiempo(self.rut,self.fecha_inicio_contrato,self)
    
    def guardar_en_db(self):

        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT rut_usuario FROM Usuario_detalle WHERE rut_usuario = %s", (self.rut,))
        if cursor.fetchone():
            print(f"El usuario con RUT {self.rut} ya existe en el sistema.")
            return
        
        query = """
            INSERT INTO Usuario_detalle (
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
        print("Empleado guardado correctamente en la base de datos.")

    @property
    def nombres(self):
        return self.__nombres
    @nombres.setter
    def nombres(self, nombres):
        self.__nombres = nombres
    @nombres.deleter
    def nombres(self):
        del self.nombres
    
    @property
    def apellido_paterno(self):
        return self.__apellido_paterno
    @apellido_paterno.setter
    def apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno
    @apellido_paterno.deleter
    def apellido_paterno(self):
        del self.__apellido_paterno

    @property
    def apellido_materno(self):
        return self.__apellido_materno
    @apellido_materno.setter
    def apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno
    @apellido_materno.deleter
    def apellido_materno(self):
        del self.__apellido_materno

    @property
    def rut(self):
        return self.__rut
    @rut.setter
    def rut(self, rut):
        self.__rut = rut
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


    def mostrar_rol(self):
        return f"ROL: Empleado\nID Departamento: {self.id_departamento}"

    def crearRegistroTiempo(self):
        self.registro.crear()

    def modificarRegistroTiempo(self):
        self.registro.modificar()

    def eliminarRegistroTiempo(self):
        self.registro.modificar()

    """Métodos de Gestion de Informe Interfaz"""
    def crearInforme(self):
        print("\n--- Creación de Nuevo Informe (Empleado) ---")
        
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
            if isinstance(mi_rut, tuple):
                mi_rut = mi_rut[0] 

            # Definimos la consulta base y los valores
            query = """
                SELECT id_informe, descripcion, formato, fecha, rut_usuario
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
                print(f"Formato:     {resultado['formato']}")
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
            if isinstance(mi_rut, tuple):
                mi_rut = mi_rut[0]

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

