from abc import ABC

class Informe(ABC):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  fecha):
        
        self._idInforme = idInforme
        self._descripcion = descripcion
        self._fecha = fecha

    @property
    def idInforme(self):
        return self._idInforme
        
    @property
    def descripcion(self):
        return self._descripcion
        
    @property
    def fecha(self):
        return self._fecha  


    def __str__ (self):
        return f"Datos del informe:\nID: {self.idInforme}\nFecha: {self.fecha}"
    


