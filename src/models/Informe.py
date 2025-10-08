from abc import ABC, abstractmethod

class Informe(ABC):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  formato,
                  fecha):
        
        self.idInforme = idInforme
        self.descripcion = descripcion
        self.formato = formato
        self.fecha = fecha

    def __str__ (self):
        return f"Datos del informe:\nID: {self.idInforme}\nFormato: {self.formato}\nFecha: {self.fecha}"
    
    @abstractmethod
    def formatearDatosParaPDF(self):
        pass

    @abstractmethod
    def formatearDatosParaExcel(self):
        pass

