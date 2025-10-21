from abc import ABC, abstractmethod
from config import conectar_db

class Persona(ABC):
    def __init__(self, rut, nombres, apellido_paterno, apellido_materno, direccion,
                 fecha_nacimiento, fecha_inicio_contrato, salario, telefono, rol, email, contraseña, id_departamento):
        self._rut = rut
        self._nombres = nombres
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._direccion = direccion
        self._fecha_nacimiento = fecha_nacimiento
        self._fecha_inicio_contrato = fecha_inicio_contrato
        self._salario = salario
        self._telefono = telefono
        self._contraseña = contraseña
        self._rol = rol
        self._email = email
        self._id_departamento = id_departamento

    @property
    def rut(self):
        if isinstance(self._rut, tuple):
            return self._rut[0]
        return self._rut
    
    @property
    def nombres(self):
        return self._nombres

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @property
    def apellido_materno(self):
        return self._apellido_materno

    @property
    def direccion(self):
        return self._direccion

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @property
    def fecha_inicio_contrato(self):
        return self._fecha_inicio_contrato

    @property
    def salario(self):
        return self._salario

    @property
    def telefono(self):
        return self._telefono
    
    @property
    def rol(self):
        return self._rol

    @property
    def email(self):
        return self._email
        
    @property
    def id_departamento(self):
        return self._id_departamento
    
    @property
    def contraseña(self):
        return self._contraseña

    def __str__(self):
        return (f"DATOS DEL USUARIO:\n"
                f"RUT: {self.rut}\n"
                f"Nombres: {self.nombres}\n"
                f"Apellido paterno: {self.apellido_paterno}\n"
                f"Apellido materno: {self.apellido_materno}\n"
                f"Dirección: {self.direccion}\n"
                f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
                f"Fecha de inicio del contrato: {self.fecha_inicio_contrato}\n"
                f"Salario: {self.salario}\n"
                f"Número telefónico: {self.telefono}"
                f"ID Departamento: {self.id_departamento}")
    
    
    def actualizar_en_db(self):
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = """
                UPDATE Usuario_detalle SET
                    nombres = %s,
                    apellido_paterno = %s,
                    apellido_materno = %s,
                    direccion = %s,
                    fecha_nacimiento = %s,
                    fecha_inicio_contrato = %s,
                    salario = %s,
                    numero_telefonico = %s,
                    rol = %s,
                    id_departamento = %s
                WHERE rut_usuario = %s
                """
            valores = (
                self.nombres,
                self.apellido_paterno,
                self.apellido_materno,
                self.direccion,
                self.fecha_nacimiento,
                self.fecha_inicio_contrato,
                self.salario,
                self.telefono,
                self.rol,
                self.id_departamento,
                self.rut
            )
            cursor.execute(query, valores)
            conexion.commit()
            print(f"Usuario con RUT {self.rut} actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @abstractmethod
    def mostrar_rol(self):
        pass