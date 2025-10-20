from .Persona import Persona
from .Empleado import Empleado
from models.interfaces.GestionEmpInterfaz import GestionEmpInterfaz
from models.interfaces.GestionProyectoInterfaz import GestionProyectoInterfaz
from config import conectar_db
from utils.validador import *
from datetime import datetime
import re
import pwinput
import bcrypt

class Gerente(Persona, GestionEmpInterfaz, GestionProyectoInterfaz):
    def __init__ (self, rut, nombres, apellido_paterno, apellido_materno,
                 direccion, fecha_nacimiento, fecha_inicio_contrato,
                 salario, telefono, contraseña, rol, id_departamento):
        
        super().__init__(
            rut=rut,
            nombres=nombres,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento,
            fecha_inicio_contrato=fecha_inicio_contrato,
            salario=salario,
            telefono=telefono,
            contraseña=contraseña ,
            rol="Gerente",
            id_departamento=id_departamento
)

        self.rut = rut
        self.id_departamento = id_departamento

    """Metodo de la clase Persona"""
    def guardar_en_db(self):
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT rut_usuario FROM Usuario_detalle WHERE rut_usuario = %s", (self.rut,))
            if cursor.fetchone():
                print(f"El usuario con RUT {self.rut} ya existe en Usuario_detalle.")
                return

            query = """
                INSERT INTO Usuario_detalle (
                    rut_usuario, direccion, fecha_nacimiento, fecha_inicio_contrato,
                    salario, numero_telefonico, rol, id_departamento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.rut, self.direccion, self.fecha_nacimiento, self.fecha_inicio_contrato,
                self.salario, self.telefono, self.rol, self.id_departamento
            )
            cursor.execute(query, valores)
            conexion.commit()
            print(f"{self.rol} guardado correctamente en la base de datos.")
        except Exception as Error:
            print(f"Error al guardar {self.rol}: {Error}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    def mostrar_rol(self):
        return f"ROL: Gerente\nID Departamento: {self.id_departamento}"
    
    def supervisarDepartamento(self):
        print("Supervisión registrada")

    def evaluarEmpleado(self):
        print("Evaluación a empleado registrado")

    """Metodos de la interfaz de gestión de empleados"""
    def crearEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                validar_rut(rut) # Asumo que esta función levanta ValueError si es inválido
                break
            except ValueError as Error:
                print(Error)
                
        rol_usuario = "Empleado"        
        while True:
            try: 
                nombre = input("Ingrese el primer nombre del empleado: ")
                if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                    raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)   
        while True:
            try: 
                apellido_paterno = input("Ingrese el apellido paterno del empleado: ")
                if not apellido_paterno or not all(c.isalpha() or c.isspace() for c in apellido_paterno):
                    raise ValueError("Ingrese un apellido paterno válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)
        while True:
            try: 
                apellido_materno = input("Ingrese el apellido materno del empleado: ")
                if not apellido_materno or not all(c.isalpha() or c.isspace() for c in apellido_materno):
                    raise ValueError("Ingrese un apellido materno válido (solo letras y espacios).")
                break
            except ValueError as Error:
                print(Error)      

        while True:
            try:
                direccion = input("Ingrese la direccion del empleado (ej: Av Arturo Prat 967): ")
                if not direccion:
                    raise ValueError("Ingrese una dirección válida")
                break
            except ValueError as Error:
                print(Error)

        while True:
            try:
                fecha_nacimiento = input("Ingrese la fecha de nacimiento del empleado (formato DD/MM/AAAA): ")
                fecha = datetime.strptime(fecha_nacimiento, '%d/%m/%Y').date()
                print(f"Fecha ingresada correctamente: {fecha}")
                break
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")

        while True:
            try:
                fecha_inicio_contrato = input("Ingrese la fecha de inicio del contrato del empleado (formato DD/MM/AAAA): ")
                fecha = datetime.strptime(fecha_inicio_contrato, '%d/%m/%Y').date()
                print(f"Fecha ingresada correctamente: {fecha}")
                break
            except ValueError:
                print("Formato inválido. Use el formato DD/MM/AAAA.")

        while True:
            try:
                salario = int(input("Ingrese el salario asignado al empleado: "))
                if salario <= 0:
                    raise ValueError("El salario debe ser un número positivo")
                break
            except ValueError:
                print("Ingrese un sueldo valido") 

        while True:
            try:
                nro_telefono = input("Ingrese el número de teléfono del empleado (formato: +56 9 XXXX XXXX): ").strip()
                patron = r"^\+56 9 \d{4} \d{4}$"
                if not re.match(patron, nro_telefono):
                    raise ValueError("Formato inválido. Use: +56 9 XXXX XXXX")
                break
            except ValueError as Error:
                print(Error)

        while True:
            try:
                id_departamento = int(input("Ingrese ID del departamento asignado al empleado: "))
                # Se abre la conexión a la db
                conexion = conectar_db() 
                cursor = conexion.cursor()
                cursor.execute("SELECT id_departamento FROM departamento WHERE id_departamento = %s", (id_departamento,))
                if not cursor.fetchone():
                    print("El departamento ingresado no existe en el sistema.")
                    cursor.close()
                    conexion.close()
                    # Aquí deberías usar 'continue' para volver a pedir el ID, en lugar de 'return'
                    continue 
                
                if len(str(id_departamento)) > 15:
                    raise ValueError("Debe ser un número de hasta 15 dígitos.")
                
                cursor.close()
                conexion.close()
                break # Si el ID es válido y existe, rompemos el bucle
            except ValueError:
                    print("Debe ingresar carácteres numéricos.")

        while True:
            try:
                contraseña_texto_plano = pwinput.pwinput("Ingrese la contraseña para el nuevo empleado: ", mask = "*")
                if validar_contraseña_segura(contraseña_texto_plano):
                    contraseña_hash = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    break
            except ValueError as Error:
                # Asumo que validar_contraseña_segura levanta ValueError
                print(Error)
            except Exception as Error: 
                print(f"Error inesperado al guardar la contraseña: {Error}")

        clases_usuario = {
            "Empleado": Empleado,
        }

        # (Manejo de conexión temporalmente movido a la función de inserción)
        # (Es mejor práctica pasar la conexión a la función de inserción)
        
        # --- ### INICIO DE LA CORRECCIÓN ### ---
        #
        # Aquí usamos "argumentos por palabra clave" (ej: rut=...)
        # para asegurarnos de que pasamos todos los 12 argumentos
        # a la clase correcta y con los nombres correctos.
        #
        try:
            nuevo_usuario: Persona = clases_usuario[rol_usuario](
                rut=rut.upper(),
                nombres=nombre,                 # La clase espera 'nombres'
                apellido_paterno=apellido_paterno,
                apellido_materno=apellido_materno,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento,
                fecha_inicio_contrato=fecha_inicio_contrato,
                salario=salario,
                telefono=nro_telefono,          # La clase espera 'telefono'
                contraseña=contraseña_hash,     # La clase espera 'contraseña'
                rol=rol_usuario,                # <-- ¡Este era el que faltaba!
                id_departamento=id_departamento
            )
        except Exception as e:
            print(f"Error al crear el objeto: {e}")
            return
        #
        # --- ### FIN DE LA CORRECCIÓN ### ---
        #

        datos_basico = (
            nuevo_usuario.rut,
            nuevo_usuario.nombres,
            nuevo_usuario.apellido_paterno,
            nuevo_usuario.apellido_materno,
            nuevo_usuario.fecha_nacimiento,
            nuevo_usuario.telefono,
            nuevo_usuario.contraseña, # La clase padre guarda el hash en 'contraseña'
            nuevo_usuario.rol
        )

        datos_detalle = (
            nuevo_usuario.rut,
            nuevo_usuario.direccion,
            nuevo_usuario.fecha_inicio_contrato,
            nuevo_usuario.salario,
            nuevo_usuario.rol,
            nuevo_usuario.id_departamento
        )
        #para mayor persistencia y modularidad, se implementa la función insertar_empleado()
        insertar_empleado_completo(datos_basico, datos_detalle)
        print(f"Empleado {nombre} {apellido_paterno} creado exitosamente.")
        print(f"Rol: {rol_usuario} | RUT: {rut.upper()} | ID Departamento: {id_departamento}\n")


    def super_buscar_empleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)

        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
        SELECT ub.rut_usuario, ub.nombres, ub.apellido_paterno, ub.apellido_materno,
            ud.direccion, ub.fecha_nacimiento, ud.fecha_inicio_contrato,
            ud.salario, ub.numero_telefonico, ub.rol, ud.id_departamento
        FROM usuario_basico ub
        JOIN usuario_detalle ud ON ub.rut_usuario = ud.rut_usuario
        WHERE ub.rut_usuario = %s
        """
        cursor.execute(query, (rut,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            print("\nDatos del empleado encontrado:")
            campos = ["RUT",
                    "Nombre",
                    "Apellido Paterno",
                    "Apellido Materno",
                    "Dirección",
                    "Fecha Nacimiento",
                    "Inicio Contrato",
                    "Salario",
                    "Teléfono",
                    "Rol",
                    "ID Departamento"]
            
            for campo, valor in zip(campos, resultado):
                print(f"{campo}: {valor}\n")
        else:
            print("No se encontró a ningún empleado con ese RUT.\n")

    def buscarEmpleado(self):
        return super().buscarEmpleado()

    def modificarEmpleado(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado a modificar: ").strip().upper()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM usuario_basico WHERE rut_usuario = %s", (rut,))
            empleado_basico = cursor.fetchone()
            cursor.execute("SELECT * FROM usuario_detalle WHERE rut_usuario = %s", (rut,))
            empleado_detalle = cursor.fetchone()
            if not empleado_basico or not empleado_detalle:
                print("No se encontró ningún empleado con ese RUT o su informacion esta incompleta.")
                cursor.close()
                conexion.close()
                return
        
            print("\nEmpleado encontrado. ¿Qué campo desea modificar?")
            print("1. Nombre")
            print("2. Apellido Paterno")
            print("3. Apellido Materno")
            print("4. Dirección")
            print("5. Fecha de Nacimiento")
            print("6. Fecha de Inicio de Contrato")
            print("7. Salario")
            print("8. Teléfono")
            print("9. ID Departamento")
        except Exception as e:
            print(f"Error al guardar el empleado: {e}")

        try:
            opcion = int(input("Seleccione una opción (1-10): "))
            basico = [1,2,3,5,8]
            detalle = [4,6,7,9]
            campos = {
                1: "nombres",
                2: "apellido_paterno",
                3: "apellido_materno",
                4: "direccion",
                5: "fecha_nacimiento",
                6: "fecha_inicio_contrato",
                7: "salario",
                8: "numero_telefonico",
                9: "id_departamento"
            }
            if opcion not in campos:
                print("Opción inválida.")
                return
            
            campo = campos[opcion]
            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}'").strip()

            if campo in ["nombres", "apellido_paterno", "apellido_materno"]:
                if not nuevo_valor or not all(c.isalpha() or c.isspace() for c in nuevo_valor):
                    raise ValueError("Solo se permiten letras y espacios.")
            elif campo == "direccion":
                if not nuevo_valor:
                    raise ValueError("La dirección no puede estar vacía.")
            elif campo in ["fecha_nacimiento", "fecha_inicio_contrato"]:
                nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y").date()
            elif campo == "salario":
                nuevo_valor = int(nuevo_valor)
                if nuevo_valor <= 0:
                    raise ValueError("El salario debe ser positivo.")
            elif campo == "numero_telefonico":
                if not(nuevo_valor.isdigit() and len(nuevo_valor) == 9 and nuevo_valor[0] == "9"):
                    raise ValueError("Número telefónico inválido.")
            elif campo == "id_departamento":
                if not nuevo_valor.isdigit() or len(nuevo_valor) > 15:
                    raise ValueError("ID Departamento debe ser numérico y de hasta 15 dígitos.")
            while True:
                confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
                if confirmacion == "s":
                    break
                elif confirmacion == "n":
                    print("Modificación cancelada.")
                    return
                else:
                    print("Entrada inválida. Debes ingresar 'S' o 'N'.")
            if opcion in basico:
                query = f"UPDATE usuario_basico SET {campo} = %s WHERE rut_usuario = %s"
            elif opcion in detalle:
                query = f"UPDATE usuario_detalle SET {campo} = %s WHERE rut_usuario = %s"
            cursor.execute(query, (nuevo_valor, rut))
            conexion.commit()
            print("Modificación realizada con éxito.")

        except ValueError as Error:
            print(f"Error: {Error}")
        finally:
            if cursor:
                cursor.close() 
            if conexion:
                conexion.close()


    def eliminarEmpleado(self):
        print("Empleado eliminado")

    """Metodos de la interfaz de gestión de proyectos"""
    def crearProyecto(self):
        print("Proyecto creado")

    def buscarProyecto(self):
        print("Proyecto buscado")

    def modificarProyecto(self):
        print("Proyecto modificado")

    def eliminarProyecto(self):
        print("Proyecto eliminado")

