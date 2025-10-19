from abc import ABC, abstractmethod
#from controllers.functions_informe import * 

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