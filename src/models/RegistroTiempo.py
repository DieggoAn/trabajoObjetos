from utils.validador import * 
import datetime

class RegistroTiempo:
    def __init__ (self,
                  rutEmpleado,
                  fecha,
                  horasTrabajadas,
                  descripcionTarea,
                  ):
        
        self.rutEmpleado = rutEmpleado
        self.fecha = fecha
        self.horasTrabajadas = horasTrabajadas
        self.descripcionTarea = descripcionTarea

    @property
    def rutEmpleado(self):
        return self.__rutEmpleado
    @rutEmpleado.setter
    def rutEmpleado(self, rutEmpleado):
        self.__rutEmpleado = rutEmpleado
    @rutEmpleado.deleter
    def rutEmpleado(self):
        del self.__rutEmpleado

    @property
    def horasTrabajadas(self):
        return self.__horasTrabajadas
    @horasTrabajadas.setter
    def horasTrabajadas(self, horasTrabajadas):
        self.__horasTrabajadas = horasTrabajadas
    @horasTrabajadas.deleter
    def horasTrabajadas(self):
        del self.__horasTrabajadas

    @property
    def descripcionTarea(self):
        return self.__descripcionTarea
    @descripcionTarea.setter
    def descripcionTarea(self, descripcionTarea):
        self.__descripcionTarea = descripcionTarea
    @descripcionTarea.deleter
    def descripcionTarea(self):
        del self.__descripcionTarea    

    def __str__ (self):
        return f"Datos del registro de tiempo:\nRUT Empleado: {self.rutEmpleado}\nFecha: {self.fecha}\nHoras trabajadas: {self.horasTrabajadas}\nDescripción de tarea: {self.descripcionTarea}"

            