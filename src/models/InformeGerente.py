from Informe import Informe 
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz

class InformeGerente(Informe, ExportarInformeInterfaz):
    def __init__(self,
                  idInforme,
                  descripcion,
                  formato,
                  fecha,
                  rutGerente):
        super().__init__(idInforme, descripcion, formato, fecha)

        self.rutGerente = rutGerente

    def __str__(self):
        return (f"Datos del informe de GERENTE:\n"
                f"ID: {self.idInforme}\n"
                f"Descripción: {self.descripcion}\n"
                f"Formato: {self.formato}\n"
                f"Fecha: {self.fecha}\n"
                f"RUT Gerente: {self.rutGerente}")
    
    def formatearDatosParaPDF(self):
        pass

    def formatearDatosParaExcel(self):
        pass
    
    """Métodos de la interfaz para exportar informes"""
    def generarPDF(self):
        pass

    def generarExcel(self):
        pass

    def exportarInforme(self):
        pass