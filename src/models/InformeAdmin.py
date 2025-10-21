from .Informe import Informe
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from openpyxl import Workbook
from fpdf import FPDF
from config import conectar_db
import datetime
import mysql.connector

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
    