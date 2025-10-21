from abc import ABC, abstractmethod

class ExportarInformeInterfaz(ABC):
    @abstractmethod
    def generarPDF(self):
        pass

    @abstractmethod
    def generarExcel(self):
        pass


    