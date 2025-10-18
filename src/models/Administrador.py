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

from utils.validador import *
from datetime import datetime


class Administrador(Persona, GestionEmpInterfaz, GestionInformeInterfaz, GestionDeptoInterfaz):
    def __init__(self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, rut_administrador, estadoSesion, id_departamento):
        
        super().__init__(
            rut=rut_administrador,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            fecha_inicio_contrato=fecha_inicio_contrato,
            salario=salario,
            telefono=telefono,
            contraseña=None,
            rol="Administrador",
            id_departamento=id_departamento)

    def __str__(self):
        return (
            f"Datos del Administrador\n"
            f"RUT: {self.rut}\n"
            f"Nombre(s): {self.nombres}\n"
            f"Apellidos: {self.apellido_paterno} {self.apellido_materno}\n"
            f"Departamento: {self.id_departamento}\n"
            f"Estado de sesión: {'Activa' if self.estadoSesion else 'Cerrada'}"
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
        return self.rut_administrador
    @rut.setter
    def rut(self, rut):
        self.__rut_administrador = rut
    @rut.deleter
    def rut(self):
        del self.__rut_administrador
 
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
        self.estadoSesion = True

    def cerrarSesion(self):
        self.estadoSesion = False


    # Nota: Esta funcion crea cualquier tipo de empleado, incluyendo Gerente y Administrador, o cualquiera que se quiera implementar a futuro.
    def crear_empleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                validar_rut(rut)
                break
            except ValueError as Error:
                print(Error)
                
        roles_validos = {"empleado", "gerente", "administrador"}
        while True:
            try:
                rol_usuario = input("Ingrese el rol del usuario: ").strip().lower()
                if rol_usuario not in roles_validos:
                    raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
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
                    return
                
                if len(str(id_departamento)) > 15:
                    raise ValueError("Debe ser un número de hasta 15 dígitos.")
                break
            except ValueError:
                    print("Debe ingresar carácteres numéricos.")

        while True:
            try:
                contraseña_texto_plano = input("Ingrese la contraseña para el nuevo empleado: ")
                if validar_contraseña_segura(contraseña_texto_plano):
                    contraseña_hash = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    break
            except ValueError as Error:
                print(f"Error inesperado al guardar la contraseña: {Error}")

        clases_usuario = {
            "Empleado":Empleado,
            "Gerente":Gerente,
            "Administrador":Administrador
        }

        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT rut_usuario FROM usuario_basico WHERE rut_usuario = %s", (rut.upper(),))
        if cursor.fetchone():
            print("El usuario ya existe en el sistema.")
            cursor.close()
            conexion.close()
            return
        cursor.close() #Y aquí se cierra la conexión a la db.
        conexion.close()

        nuevo_usuario: Persona = clases_usuario[rol_usuario](
            rut.upper(), nombre, apellido_paterno, apellido_materno,
            direccion, fecha_nacimiento, fecha_inicio_contrato,
            salario, nro_telefono, contraseña_hash, id_departamento
        )

        datos_basico = (
            nuevo_usuario.rut,
            nuevo_usuario.nombres,
            nuevo_usuario.apellido_paterno,
            nuevo_usuario.apellido_materno,
            nuevo_usuario.fecha_nacimiento,
            nuevo_usuario.telefono,
            nuevo_usuario.contraseña_hash,
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
        insertar_empleado_detalle(datos_basico, datos_detalle)
        print(f"Empleado {nombre} {apellido_paterno} creado exitosamente.")
        print(f"Rol: {rol_usuario} | RUT: {rut.upper()} | ID Departamento: {id_departamento}\n")

    def buscarEmpleado(self):
        pass

    def modificarEmpleado(self):
        pass

    def eliminarEmpleado(self):
        pass

    def reasignarEmpleadoDeDep(self):
        pass

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
        pass

    def buscarInforme(self):
        pass

    def modificarInforme(self):
        pass

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

    def asignarEmpleadoDeDep(self):
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

