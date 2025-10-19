from abc import ABC, abstractmethod
#from controllers.functions import * 
#from controllers.LogUser import registrar_usuario

class GestionEmpInterfaz(ABC):

    @abstractmethod
    def crearEmpleado(self):
        pass

    @abstractmethod
    def buscarEmpleado(self):
        pass

    @abstractmethod
    def modificarEmpleado(self):
        pass

    @abstractmethod
    def eliminarEmpleado(self):
        pass

    @abstractmethod
    def asignarEmpleadoDeDep(self):
        pass

    @abstractmethod
    def reasignarEmpleadoDeDep(self):
        pass

    @abstractmethod
    def eliminarEmpleadoDeDep(self):
        pass


