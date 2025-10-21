from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from fpdf import FPDF
from datetime import datetime
from config import conectar_db
from openpyxl import Workbook

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

    """Métodos de la interfaz para exportar informe"""
    def generarPDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informe de Empleado", ln=True, align='C')
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=(
            f"ID: {self.idInforme}\n"
            f"Descripción: {self.descripcion}\n"
            f"Fecha: {self.fecha.strftime('%Y-%m-%d')}\n"
            f"RUT Empleado: {self.rutEmpleado}"
        ))
        pdf.output(f"informe_empleado_{self.idInforme}.pdf")

    def generarExcel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Informe Empleado"
        ws.append(["ID", "Descripción", "Fecha", "RUT Empleado"])
        ws.append([
            self.idInforme,
            self.descripcion,
            self.fecha.strftime("%Y-%m-%d"),
            self.rutEmpleado
        ])
        wb.save(f"informe_empleado_{self.idInforme}.xlsx")