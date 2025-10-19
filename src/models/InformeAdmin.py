from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz

class InformeAdmin(Informe, ExportarInformeInterfaz):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  formato,
                  fecha, rutAdmin):
        
        super().__init__(idInforme, descripcion, formato, fecha)

        self.rutAdmin = rutAdmin

    def __str__ (self):
        return f"Datos del informe de ADMIN:\nID: {self.idInforme}\nFormato: {self.formato}\nFecha: {self.fecha}"
    
    """Métodos de la interfaz exportar informe"""

    def formatearDatosParaExcel(self):
        pass

    """Métodos propios de InformeAdmin"""
    def generarPDF(self):
        pass

    def generarExcel(self):
        pass
