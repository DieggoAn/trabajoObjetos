from abc import ABC, abstractmethod

class GestionProyectoInterfaz(ABC):
    @abstractmethod
    def crearProyecto(self):
        pass

    @abstractmethod
    def buscarProyecto(self):
        pass

    @abstractmethod
    def modificarProyecto(self):
        pass

    @abstractmethod
    def eliminarProyecto(self):
        pass

    @abstractmethod
    def asignarEmpleadoAProyecto(self):
        pass

    @abstractmethod
    def desasignarEmpleadoDeProyecto(self):
        pass