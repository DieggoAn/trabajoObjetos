from abc import ABC, abstractmethod
from controllers.functions_departamento import * 

class GestionDeptoInterfaz(ABC):
    @abstractmethod
    def crearDepartamento(self):
        crear_departamento()

    @abstractmethod
    def buscarDepartamento(self):
        buscar_departamento()

    @abstractmethod
    def modificarDepartamento(self):
        modificar_departamento()

    @abstractmethod
    def eliminarDepartamento(self):
        eliminar_departamento()

    