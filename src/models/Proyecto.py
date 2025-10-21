class Proyecto:
    def __init__ (self, idProyecto,
                  nombre,
                  descripcion,
                  fechaInicio):
        
        self._idProyecto = idProyecto
        self._nombre = nombre
        self._descripcion = descripcion
        self._fechaInicio = fechaInicio

    @property
    def idProyecto(self):
        return self._idProyecto
        
    @property
    def nombre(self):
        return self._nombre
        
    @property
    def descripcion(self):
        return self._descripcion
        
    @property
    def fechaInicio(self):
        return self._fechaInicio

    def __str__ (self):
        return f"Los datos del proyecto son los siguientes:\nID: {self.idProyecto}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fechaInicio}"
    
    def asignarEmpleado(self):
        pass