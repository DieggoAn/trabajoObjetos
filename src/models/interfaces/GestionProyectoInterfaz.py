from abc import ABC, abstractmethod
from controllers.functions_proyecto import * 

class GestionProyectoInterfaz(ABC):
    @abstractmethod
    def crearProyecto(self):
        crear_proyecto()

    @abstractmethod
    def buscarProyecto(self):
        buscar_proyecto()

    @abstractmethod
    def modificarProyecto(self):
        modificar_proyecto()

    @abstractmethod
    def eliminarProyecto(self):
        eliminar_proyecto()

    #@abstractmethod
    #def asignarEmpleadoAProyecto(self):
        #pass

    #@abstractmethod
    #def desasignarEmpleadoDeProyecto(self):
        #pass