from Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionProyectoInterfaz import GestionProyectoInterfaz

class Gerente(Persona, GestionEmpInterfaz, GestionProyectoInterfaz):
    def __init__ (self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, rut_gerente, id_departamento):
        
        super().__init__(nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono)
        
        self.rut_gerente = rut_gerente
        self.id_departamento = id_departamento

    """Metodo de la clase Persona"""
    def guardar_en_db(self):
        from config import conectar_db
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
            self.rut_gerente, self.nombres, self.apellido_paterno, self.apellido_materno,
            self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
            self.salario, self.telefono, "Gerente", self.id_departamento
        )
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print(f"Gerente guardado correctamente en la base de datos.")


    def mostrar_rol(self):
        return f"ROL: Gerente\nID Departamento: {self.id_departamento}"
    
    def supervisarDepartamento(self):
        print("Supervisión registrada")

    def evaluarEmpleado(self):
        print("Evaluación a empleado registrado")

    """Metodos de la interfaz de gestión de empleados"""
    def crearEmpleado(self):
        print("Empleado creado")

    def buscarEmpleado(self):
        print("Empleado buscado")

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

