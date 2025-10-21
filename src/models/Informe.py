from abc import ABC

class Informe(ABC):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  fecha):
        
        self.idInforme = idInforme
        self.descripcion = descripcion
        self.fecha = fecha

    def __str__ (self):
        return f"Datos del informe:\nID: {self.idInforme}\nFecha: {self.fecha}"
    


