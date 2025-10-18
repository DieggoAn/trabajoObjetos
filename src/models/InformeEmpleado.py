from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from fpdf import FPDF
from datetime import datetime
from config import conectar_db

class InformeEmpleado(Informe, ExportarInformeInterfaz):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  formato,
                  fecha, rutEmpleado):
        super().__init__(idInforme, descripcion, formato, fecha)

        self.rutEmpleado = rutEmpleado

    def __str__(self):
        return (f"Datos del informe de EMPLEADO:\n"
                f"ID: {self.idInforme}\n"
                f"Descripción: {self.descripcion}\n"
                f"Formato: {self.formato}\n"
                f"Fecha: {self.fecha}\n"
                f"RUT Empleado: {self.rutEmpleado}")

    def formatearDatosParaPDF(self):
        class pdf(FPDF):
            def header(self):
                if hasattr(self, 'document_title'):
                    self.set_font(family = 'Arial', style = 'B', size = 16)
                    self.cell(w = 0, h = 10, text = self.document_title, border = 0, ln = 1, align = 'C')

            def cuerpo(self):
                pass

            def footer(self):
                self.set_y(-15)
                self.set_font(family = "Arial", style = "I", size = 12)
                self.cell(w = 0, h = 10, text = f"Generado el {datetime.now().strftime('%d/%m/%y')}", ln = 0, align = "C")


        ##pdf.output(name = f'Informe Empleado{datetime.now().strftime('%d/%m/%y')}', dest='"C:\Users\juann\Downloads"')

    def formatearDatosParaExcel(self):
        pass

    """Métodos de la interfaz para exportar informe"""
    def generarPDF(self):
        pass

    def generarExcel(self):
        pass

    def exportarInforme(self):
        pass

    