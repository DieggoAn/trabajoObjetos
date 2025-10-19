from abc import ABC, abstractmethod
from controllers.functions_informe import * 

class GestionInformeInterfaz(ABC):

    @abstractmethod
    def crearInforme(self):
        crear_informe()

    @abstractmethod
    def buscarInforme(self):
        buscar_informe()

    @abstractmethod
    def modificarInforme(self):
        modificar_informe()

    @abstractmethod
    def eliminarInforme(self):
        eliminar_informe()