class RegistroTiempo:
    def __init__ (self,
                  rutEmpleado,
                  fecha,
                  horasTrabajadas,
                  descripcionTarea):
        
        self.rutEmpleado = rutEmpleado
        self.fecha = fecha
        self.horasTrabajadas = horasTrabajadas
        self.descripcionTarea = descripcionTarea

    def __str__ (self):
        return f"Datos del registro de tiempo:\nRUT Empleado: {self.rutEmpleado}\nFecha: {self.fecha}\nHoras trabajadas: {self.horasTrabajadas}\nDescripción de tarea: {self.descripcionTarea}"
    
    def crear(self):
        print("Registro de tiempo creado")

    def modificar(self):
        print("Registro de tiempo modificado")

    def eliminar(self):
        print("Registro de tiempo eliminado")
        