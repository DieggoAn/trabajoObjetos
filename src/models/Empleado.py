from Persona import Persona
from models.interfaces.RegistroTiempoInterfaz import RegistroTiempoInterfaz
from RegistroTiempo import RegistroTiempo
from models.interfaces.GestionInformeInterfaz import GestionInformeInterfaz 

class Empleado(Persona, RegistroTiempoInterfaz, GestionInformeInterfaz):
    def __init__ (self, rut_empleado, nombre, apellido_paterno, apellido_materno, direccion,
                 fecha_nacimiento, fecha_inicio_contrato, salario, telefono, id_departamento):
        
        super().__init__(nombre, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono)
        
        self.rut_empleado = rut_empleado
        self.id_departamento = id_departamento
        self.registro = RegistroTiempo()
    
    def guardar_en_db(self):
        from config import conectar_db
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
            self.rut_empleado, self.nombres, self.apellido_paterno, self.apellido_materno,
            self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
            self.salario, self.telefono, "Empleado", self.id_departamento
        )
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        print("Empleado guardado correctamente en la base de datos.")

    def mostrar_rol(self):
        return f"ROL: Empleado\nID Departamento: {self.id_departamento}"

    def crearRegistroTiempo(self):
        self.registro.crear()

    def modificarRegistroTiempo(self):
        self.registro.modificar()

    def eliminarRegistroTiempo(self):
        self.registro.modificar()

    """Métodos de Gestion de Informe Interfaz"""
    def crearInforme(self):
        pass

    def buscarInforme(self):
        pass

    def modificarInforme(self):
        pass

    def eliminarInforme(self):
        pass

    