class Proyecto:
    def __init__ (self, idProyecto,
                  nombre,
                  descripcion,
                  fechaInicio):
        
        self.idProyecto = idProyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre   

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
    @descripcion.deleter
    def descripcion(self):
        del self.__descripcion

    def __str__ (self):
        return f"Los datos del proyecto son los siguientes:\nID: {self.idProyecto}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fechaInicio}"
    
    def asignarEmpleado(self):
        pass