from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, rut, nombres, apellido_paterno, apellido_materno, direccion,
                 fecha_nacimiento, fecha_inicio_contrato, salario, telefono, rol, id_departamento):
        self.rut = rut
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.direccion = direccion
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_inicio_contrato = fecha_inicio_contrato
        self.salario = salario
        self.telefono = telefono
        self.rol = rol
        self.id_departamento = id_departamento

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
    
    def guardar_en_db(self, rol):
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
                self.rut, self.nombres, self.apellido_paterno, self.apellido_materno,
                self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
                self.salario, self.telefono, rol, self.id_departamento
            )
            cursor.execute(query, valores)
            conexion.commit()
            cursor.close()
            conexion.close()
            print(f"{rol} guardado correctamente en la base de datos.")
        except Exception as e:
            print(f"Error al guardar {rol}: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
    
    def actualizar_en_db(self):
        from config import conectar_db
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            query = """
                UPDATE usuario SET
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