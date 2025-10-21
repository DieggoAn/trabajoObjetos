from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from openpyxl import Workbook
from fpdf import FPDF

class InformeAdmin(Informe, ExportarInformeInterfaz):
    def __init__ (self,
                  idInforme,
                  descripcion,
                  fecha, rutAdmin):
        
        super().__init__(idInforme, descripcion, fecha)

        self.rutAdmin = rutAdmin

    def __str__ (self):
        return f"Datos del informe de ADMIN:\nID: {self.idInforme}\nFecha: {self.fecha}"
    
    """Métodos propios de InformeAdmin"""
    def generarPDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informe de Administrador", ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=f"ID: {self.idInforme}\nDescripción: {self.descripcion}\nFecha: {self.fecha}\nRUT Admin: {self.rutAdmin}")
        pdf.output(f"informe_admin_{self.idInforme}.pdf")

    def generarExcel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Informe Admin"
        ws.append(["ID", "Descripción", "Fecha", "RUT Admin"])
        ws.append([self.idInforme, self.descripcion, self.fecha.strftime("%Y-%m-%d"), self.rutAdmin])
        wb.save(f"informe_admin_{self.idInforme}.xlsx")