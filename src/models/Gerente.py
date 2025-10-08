from Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionProyectoInterfaz import GestionProyectoInterfaz

class Gerente(Persona, GestionEmpInterfaz, GestionProyectoInterfaz):
    def __init__ (self, nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico, rutGerente, idDepartamento):
        
        super().__init__(nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico)
        
        self.rutGerente = rutGerente
        self.idDepartamento = idDepartamento

    """Metodo de la clase Persona"""
    def mostrar_rol(self):
        return f"ROL: Gerente\nID Departamento: {self.idDepartamento}"
    
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

