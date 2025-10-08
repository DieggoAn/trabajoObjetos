class Proyecto:
    def __init__ (self, idProyecto,
                  nombre,
                  descripcion,
                  fechaInicio):
        
        self.idProyecto = idProyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio

    def __str__ (self):
        return f"Los datos del proyecto son los siguientes:\nID: {self.idProyecto}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fechaInicio}"
    
    def asignarEmpleado(self):
        pass