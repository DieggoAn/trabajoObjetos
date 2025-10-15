from Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz
from models.interfaces.GestionDeptoInterfaz import GestionDeptoInterfaz
from config import conectar_db

class Administrador(Persona, GestionEmpInterfaz, GestionInformeInterfaz, GestionDeptoInterfaz):
    def __init__(self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, rut_administrador, estadoSesion, id_departamento):
        
        super().__init__(
            rut=rut_administrador,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            fecha_inicio_contrato=fecha_inicio_contrato,
            salario=salario,
            telefono=telefono,
            contraseña=None,
            rol="Administrador",
            id_departamento=id_departamento)

    def __str__(self):
        return (
            f"Datos del Administrador\n"
            f"RUT: {self.rut}\n"
            f"Nombre(s): {self.nombres}\n"
            f"Apellidos: {self.apellido_paterno} {self.apellido_materno}\n"
            f"Departamento: {self.id_departamento}\n"
            f"Estado de sesión: {'Activa' if self.estadoSesion else 'Cerrada'}"
        )

    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.nombre = nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    @property
    def rut(self):
        return self.rut_administrador
    @rut.setter
    def rut(self, rut):
        self.__rut_administrador = rut
    @rut.deleter
    def rut(self):
        del self.__rut_administrador
 
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, rut):
        self.__direccion = rut
    @direccion.deleter
    def direccion(self):
        del self.__direccion

    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @salario.deleter
    def salario(self):
        del self.__salario

    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    @telefono.deleter
    def telefono(self):
        del self.__telefono

    def guardar_en_db(self):
        from config import conectar_db
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = """
                INSERT INTO usuario (
                    rut_usuario, nombres, apellido_paterno, apellido_materno,
                    direccion, fecha_nacimiento, fecha_inicio_contrato,
                    salario, numero_telefonico, rol, id_departamento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.rut_administrador, self.nombres, self.apellido_paterno, self.apellido_materno,
                self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
                self.salario, self.telefono, "Administrador", self.id_departamento
            )
            cursor.execute(query, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            print("Administrador guardado correctamente en la base de datos.")
        except Exception as e:
            print(f"Error al guardar al administrador: {e}")
        finally:
            cursor.close()
            conexion.close()

    def iniciarSesion(self):
        self.estadoSesion = True

    def cerrarSesion(self):
        self.estadoSesion = False


    def crearEmpleado(self):
        pass

    def buscarEmpleado(self):
        pass

    def modificarEmpleado(self):
        pass

    def eliminarEmpleado(self):
        pass

    def reasignarEmpleadoDeDep(self):
        pass

    def eliminarEmpleadoDeDep(self):
        pass


    def crearDepartamento(self):
        pass

    def buscarDepartamento(self):
        pass

    def modificarDepartamento(self):
        pass

    def eliminarDepartamento(self):
        pass


    def crearInforme(self):
        pass

    def buscarInforme(self):
        pass

    def modificarInforme(self):
        pass

    def eliminarInforme(self):
        pass

    
    def crearProyecto(self):
        pass

    def buscarProyecto(self):
        pass

    def modificarProyecto(self):
        pass

    def eliminarProyecto(self):
        pass

    def asignarEmpleadoDeDep(self):
        pass


