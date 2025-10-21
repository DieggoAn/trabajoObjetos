from abc import ABC, abstractmethod

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

    