from .Informe import Informe 
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from fpdf import FPDF
from openpyxl import Workbook
from datetime import datetime

class InformeGerente(Informe, ExportarInformeInterfaz):
    def __init__(self,
                  idInforme,
                  descripcion,
                  fecha,
                  rutGerente):
        super().__init__(idInforme, descripcion, fecha)

        self.rutGerente = rutGerente

    def __str__(self):
        return (f"Datos del informe de GERENTE:\n"
                f"ID: {self.idInforme}\n"
                f"Descripción: {self.descripcion}\n"
                f"Fecha: {self.fecha}\n"
                f"RUT Gerente: {self.rutGerente}")
    

    def formatearDatosParaExcel(self):
        return {
            "ID": self.idInforme,
            "Descripción": self.descripcion,
            "Fecha": self.fecha.strftime("%Y-%m-%d"),
            "RUT Gerente": self.rutGerente
        }
    
    """Métodos de la interfaz para exportar informes"""
    def generarPDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informe de Gerente", ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=(
            f"ID: {self.idInforme}\n"
            f"Descripción: {self.descripcion}\n"
            f"Fecha: {self.fecha.strftime('%Y-%m-%d')}\n"
            f"RUT Gerente: {self.rutGerente}"
        ))
        pdf.output(f"informe_gerente_{self.idInforme}.pdf")
    

    def generarExcel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Informe Gerente"
        ws.append(["ID", "Descripción", "Fecha", "RUT Gerente"])
        ws.append([
            self.idInforme,
            self.descripcion,
            self.fecha.strftime("%Y-%m-%d"),
            self.rutGerente
        ])
        wb.save(f"informe_gerente{self.idInforme}.xlsx")

