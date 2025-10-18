from .Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionProyectoInterfaz import GestionProyectoInterfaz
from config import conectar_db
from utils import *

class Gerente(Persona, GestionEmpInterfaz, GestionProyectoInterfaz):
    def __init__ (self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, rut_gerente, id_departamento):
        
        super().__init__(
            rut=rut_gerente,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            fecha_inicio_contrato=fecha_inicio_contrato,
            salario=salario,
            telefono=telefono,
            contraseña=None,
            rol="Gerente",
            id_departamento=id_departamento
)

        self.rut_gerente = rut_gerente
        self.id_departamento = id_departamento

    """Metodo de la clase Persona"""
    def guardar_en_db(self):
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT rut_usuario FROM Usuario_detalle WHERE rut_usuario = %s", (self.rut,))
            if cursor.fetchone():
                print(f"El usuario con RUT {self.rut} ya existe en Usuario_detalle.")
                return

            query = """
                INSERT INTO Usuario_detalle (
                    rut_usuario, direccion, fecha_nacimiento, fecha_inicio_contrato,
                    salario, numero_telefonico, rol, id_departamento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.rut, self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
                self.salario, self.telefono, self.rol, self.id_departamento
            )
            cursor.execute(query, valores)
            conexion.commit()
            print(f"{self.rol} guardado correctamente en la base de datos.")
        except Exception as Error:
            print(f"Error al guardar {self.rol}: {Error}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def mostrar_rol(self):
        return f"ROL: Gerente\nID Departamento: {self.id_departamento}"
    
    def supervisarDepartamento(self):
        print("Supervisión registrada")

    def evaluarEmpleado(self):
        print("Evaluación a empleado registrado")

    """Metodos de la interfaz de gestión de empleados"""
    def crearEmpleado(self):
        print("Empleado creado")

    def buscarEmpleado(self, rut):
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
            SELECT ub.rut_usuario
            FROM usuario_basico ub
            WHERE ub.rut_usuario = %s
            """
            cursor.execute(query, (rut,))
            resultado = cursor.fetchone()

            if resultado:
                print("¡ERROR!. El usuario se encuentra registrado en el sistema.\n")
            else:
                print("El usuario no está registrado.")
        except Exception as e:
            print(f"Error inesperado al buscar el empleado: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def modificarEmpleado(self):
        print("Empleado modificado")

    def eliminarEmpleado(self):
        print("Empleado eliminado")

    def asignarEmpleadoDeDep(self):
        pass

    def reasignarEmpleadoDeDep(self):
        pass

    def eliminarEmpleadoDeDep(self):
        pass

    """Metodos de la interfaz de gestión de proyectos"""
    def crearProyecto(self):
        print("Proyecto creado")

    def buscarProyecto(self):
        print("Proyecto buscado")

    def modificarProyecto(self):
        print("Proyecto modificado")

    def eliminarProyecto(self):
        print("Proyecto eliminado")

