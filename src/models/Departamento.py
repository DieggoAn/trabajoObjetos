class Departamento:
    def __init__ (self, idDepartamento, nombre, rutGerenteAsociado):

        self.idDepartamento = idDepartamento
        self.nombre = nombre
        self.rutGerenteAsociado = rutGerenteAsociado

    def __str__(self):
        return f"Datos del Departamento:\nID: {self.idDepartamento}\nNombre: {self.nombre}\nRUT Gerente Asociado: {self.rutGerenteAsociado}"
    
    def asignarGerente():
        pass

    def asignarEmpleado():
        pass
