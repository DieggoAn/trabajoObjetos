from abc import ABC, abstractmethod

class RegistroTiempoInterfaz(ABC):
    @abstractmethod
    def crearRegistroTiempo(self):
        pass

    @abstractmethod
    def modificarRegistroTiempo(self):
        pass

    @abstractmethod
    def eliminarRegistroTiempo(self):
        pass
     