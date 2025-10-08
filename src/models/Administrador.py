from Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz
from models.interfaces.GestionDeptoInterfaz import GestionDeptoInterfaz

class Administrador(Persona, GestionEmpInterfaz, GestionInformeInterfaz, GestionDeptoInterfaz):
    def __init__(self, nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico, rutAdmin, estadoSesion):
        
        super().__init__(nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico)
        
        self.rutAdmin = rutAdmin
        self.estadoSesion = estadoSesion

    def __str__(self):
        return f"Datos del administrador:\nRUT: {self.rutAdmin}\nNombre(s): {self.nombres}\nApellidos: {self.apellidoPaterno} {self.apellidoMaterno}\nEstado de sesión: {self.estadoSesion}"
    
    def iniciarSesion(self):
        self.estadoSesion = True

    def cerrarSesion(self):
        self.estadoSesion = False


    def crearEmpleado(self):
        pass

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


