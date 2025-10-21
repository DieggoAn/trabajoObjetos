from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from fpdf import FPDF
from datetime import datetime
from config import conectar_db

class InformeEmpleado(Informe, ExportarInformeInterfaz):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  fecha, rutEmpleado):
        super().__init__(idInforme, descripcion, fecha)

        self.rutEmpleado = rutEmpleado

    def __str__(self):
        return (f"Datos del informe de EMPLEADO:\n"
                f"ID: {self.idInforme}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha: {self.fecha}\n"
                f"RUT Empleado: {self.rutEmpleado}")


    def formatearDatosParaExcel(self):
        pass

    """Métodos de la interfaz para exportar informe"""
    def generarPDF(self):
        pass

    def generarExcel(self):
        pass

    