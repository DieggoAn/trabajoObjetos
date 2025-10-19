from abc import ABC, abstractmethod
from controllers.functions import * 
from controllers.LogUser import *

class GestionEmpInterfaz(ABC):

    @abstractmethod
    def crearEmpleado(self):
        registrar_usuario()

    @abstractmethod
    def buscarEmpleado(self):
        buscar_empleado()

    @abstractmethod
    def modificarEmpleado(self):
        modificar_empleado()

    @abstractmethod
    def eliminarEmpleado(self):
        eliminar_empleado()

    #@abstractmethod
    #def asignarEmpleadoDeDep(self):
        #pass

    #@abstractmethod
    #def reasignarEmpleadoDeDep(self):
        #pass

    @abstractmethod
    def eliminarEmpleadoDeDep(self):
        pass


