from abc import ABC, abstractmethod

class GestionInformeInterfaz(ABC):

    @abstractmethod
    def crearInforme(self):
        pass

    @abstractmethod
    def buscarInforme(self):
        pass

    @abstractmethod
    def modificarInforme(self):
        pass

    @abstractmethod
    def eliminarInforme(self):
        pass