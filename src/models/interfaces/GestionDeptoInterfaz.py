from abc import ABC, abstractmethod
from controllers.functions_departamento import * 

class GestionDeptoInterfaz(ABC):
    @abstractmethod
    def crearDepartamento(self):
        pass

    @abstractmethod
    def buscarDepartamento(self):
        pass

    @abstractmethod
    def modificarDepartamento(self):
        pass
    @abstractmethod
    def eliminarDepartamento(self):
        pass

    