class Departamento:
    def __init__ (self, nombre, rutGerenteAsociado, idDepartamento=None):

        self.idDepartamento = idDepartamento
        self.nombre = nombre
        self.rutGerenteAsociado = rutGerenteAsociado

    def __str__(self):
        return f"Datos del Departamento:\nID: {self.idDepartamento}\nNombre: {self.nombre}\nRUT Gerente Asociado: {self.rutGerenteAsociado}"
    
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
    def rutGerenteAsociado(self):
        return self.__rutGerenteAsociado
    @rutGerenteAsociado.setter
    def rutGerenteAsociado(self, rut):
        self.__rutGerenteAsociado = rut
    @rutGerenteAsociado.deleter
    def rutGerenteAsociado(self):
        del self.__rutGerenteAsociado
        
    def asignarGerente():
        pass

    def asignarEmpleado():
        pass
