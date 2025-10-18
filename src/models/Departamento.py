class Departamento:
    def __init__ (self, idDepartamento=None, nombre=None, rutGerenteAsociado=None):

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
        
    def asignarGerente(self,cursor,rut_usuario):
        try:
            query = "UPDATE usuario_detalle SET id_departamento = %s, rol = %s WHERE rut_usuario = %s"
            cursor.execute(query,(self.idDepartamento, "gerente", rut_usuario))
        except Exception as e:
            print(f"Error en metodo AsignarGerente: {e}")
        pass

    def asignarEmpleado(self,cursor ,rut_usuario):
        try:
            query = "UPDATE usuario_detalle SET id_departamento = %s WHERE rut_usuario = %s"
            cursor.execute(query,(self.idDepartamento, rut_usuario))

            print(f"SQL: Asignando empleado {rut_usuario} a departamento {self.idDepartamento}")
        except Exception as e:
            print(f"Error en metodo asignarEmpleado: {e}")