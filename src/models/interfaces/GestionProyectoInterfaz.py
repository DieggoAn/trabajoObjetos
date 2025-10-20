from abc import ABC, abstractmethod
from controllers.functions_proyecto import * 

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
