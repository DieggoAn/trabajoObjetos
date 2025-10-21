from utils.validador import * 
import datetime

class RegistroTiempo:
    def __init__ (self,
                  rutEmpleado,
                  fecha,
                  horasTrabajadas,
                  descripcionTarea,
                  ):
        
        self._rutEmpleado = rutEmpleado
        self._fecha = fecha
        self._horasTrabajadas = horasTrabajadas
        self._descripcionTarea = descripcionTarea

    @property
    def rutEmpleado(self):
        return self._rutEmpleado
        
    @property
    def fecha(self):
        return self._fecha
        
    @property
    def horasTrabajadas(self):
        return self._horasTrabajadas
        
    @property
    def descripcionTarea(self):
        return self._descripcionTarea

    def __str__ (self):
        return f"Datos del registro de tiempo:\nRUT Empleado: {self.rutEmpleado}\nFecha: {self.fecha}\nHoras trabajadas: {self.horasTrabajadas}\nDescripción de tarea: {self.descripcionTarea}"

            