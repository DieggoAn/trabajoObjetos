from .Informe import Informe 
from models.interfaces.ExportarInformeInterfaz import ExportarInformeInterfaz
from fpdf import FPDF
from openpyxl import Workbook
from config import conectar_db
import datetime
import mysql.connector

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
        pass
    
    def generarPDF(self):
        pass

    def generarExcel(self):
        pass

