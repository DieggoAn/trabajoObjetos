from Persona import Persona
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz
from models.interfaces.GestionDeptoInterfaz import GestionDeptoInterfaz

class Administrador(Persona, GestionEmpInterfaz, GestionInformeInterfaz, GestionDeptoInterfaz):
    def __init__(self, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, rut_administrador, estadoSesion, id_departamento):
        
        super().__init__(nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono)
        
        self.rut_administrador = rut_administrador
        self.estadoSesion = estadoSesion
        self.id_departamento = id_departamento

    def __str__(self):
        return (
            f"Datos del Administrador\n"
            f"RUT: {self.rut_administrador}\n"
            f"Nombre(s): {self.nombres}\n"
            f"Apellidos: {self.apellido_paterno} {self.apellido_materno}\n"
            f"Departamento: {self.id_departamento}\n"
            f"Estado de sesión: {'Activa' if self.estadoSesion else 'Cerrada'}"
        )

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


