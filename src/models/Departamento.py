from utils.validador import validar_rut
from config import *
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
            
    def asignarGerente(self):
        
        # --- BLOQUE 1: OBTENER UN RUT CON FORMATO VÁLIDO ---
        rut_gerente_asociado = None
        while True:
            try:
                rut_gerente_asociado = input("Ingrese el RUT del gerente (ej: 12345678-K): ").strip().lower()
                validar_rut(rut_gerente_asociado) # Valida solo el formato
                rut_gerente_asociado = rut_gerente_asociado.upper()
                break  # Si el formato es válido, salimos del bucle de input

            except ValueError as Error:
                # Si validar_rut falla, imprime el error y el bucle repite
                print(f"Error de formato: {Error}")

        # --- BLOQUE 2: LÓGICA DE BASE DE DATOS (UNIFICADA) ---
        conexion = None
        cursor = None
        
        # Un solo 'try' para TODA la operación de DB
        try:
            conexion = conectar_db()
            cursor = conexion.cursor(dictionary=True)
            
            # 1. Verificación (Existencia y Rol)
            cursor.execute("SELECT rol FROM usuario_detalle WHERE rut_usuario = %s", (rut_gerente_asociado,))
            resultado = cursor.fetchone()

            if not resultado:
                print("El RUT no está registrado en el sistema.")
                return  # Salimos de la función, el 'finally' se ejecutará
            
            if resultado['rol'].lower() != "gerente":
                print("El usuario no tiene rol de Gerente.")
                return  # Salimos de la función, el 'finally' se ejecutará

            # 2. Ejecución (Si pasó las verificaciones)
            # El gerente existe y tiene el rol correcto, ahora lo asignamos.
            print(f"Gerente {rut_gerente_asociado} encontrado. Asignando a departamento...")
            
            query = "UPDATE usuario_detalle SET id_departamento = %s, rol = %s WHERE rut_usuario = %s"
            # (Nota: Asumo que 'rol' también existe en 'usuario_detalle')
            cursor.execute(query, (self.idDepartamento, "gerente", rut_gerente_asociado))
            
            conexion.commit() # Guardamos los cambios
            print("Gerente asignado con éxito.")

        except Exception as e:
            # Captura CUALQUIER error (conexión, SELECT, UPDATE)
            print(f"Error en metodo AsignarGerente: {e}")
            if conexion:
                conexion.rollback() # Revierte los cambios si el UPDATE falla

        finally:
            # 3. Limpieza (Se ejecuta SIEMPRE)
            # Cierra la conexión al final, sin importar si
            # la función tuvo éxito o falló.
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
    def asignarEmpleado(self,cursor ,rut_usuario):
        try:
            query = "UPDATE usuario_detalle SET id_departamento = %s WHERE rut_usuario = %s"
            cursor.execute(query,(self.idDepartamento, rut_usuario))

            print(f"SQL: Asignando empleado {rut_usuario} a departamento {self.idDepartamento}")
        except Exception as e:
            print(f"Error en metodo asignarEmpleado: {e}")