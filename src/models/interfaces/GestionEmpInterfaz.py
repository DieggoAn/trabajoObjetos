from abc import ABC, abstractmethod

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


