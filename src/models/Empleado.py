from Persona import Persona
from models.interfaces.RegistroTiempoInterfaz import RegistroTiempoInterfaz
from RegistroTiempo import RegistroTiempo
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz 

class Empleado(Persona, RegistroTiempoInterfaz, GestionInformeInterfaz):
    def __init__ (self, nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico, rutEmpleado, idDepartamento):
        
        super().__init__(nombres, apellidoPaterno, apellidoMaterno,
                 direccion, fechaNacimiento, fechaInicioContrato,
                 salario, numeroTelefonico)
        
        self.rutEmpleado = rutEmpleado
        self.idDepartamento = idDepartamento
        self.registro = RegistroTiempo()

    def mostrar_rol(self):
        return f"ROL: Empleado\nID Departamento: {self.idDepartamento}"

    def crearRegistroTiempo(self):
        self.registro.crear()

    def modificarRegistroTiempo(self):
        self.registro.modificar()

    def eliminarRegistroTiempo(self):
        self.registro.modificar()

    """Métodos de Gestion de Informe Interfaz"""
    def crearInforme(self):
        pass

    def buscarInforme(self):
        pass

    def modificarInforme(self):
        pass

    def eliminarInforme(self):
        pass

    