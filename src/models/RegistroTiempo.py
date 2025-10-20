from utils.validador import * 
import datetime

class RegistroTiempo:
    def __init__ (self,
                  rutEmpleado,
                  fecha,
                  horasTrabajadas,
                  descripcionTarea,
                  ):
        
        self.rutEmpleado = rutEmpleado
        self.fecha = fecha
        self.horasTrabajadas = horasTrabajadas
        self.descripcionTarea = descripcionTarea

    @property
    def rutEmpleado(self):
        return self.__rutEmpleado
    @rutEmpleado.setter
    def rutEmpleado(self, rutEmpleado):
        self.__rutEmpleado = rutEmpleado
    @rutEmpleado.deleter
    def rutEmpleado(self):
        del self.__rutEmpleado

    @property
    def horasTrabajadas(self):
        return self.__horasTrabajadas
    @horasTrabajadas.setter
    def horasTrabajadas(self, horasTrabajadas):
        self.__horasTrabajadas = horasTrabajadas
    @horasTrabajadas.deleter
    def horasTrabajadas(self):
        del self.__horasTrabajadas

    @property
    def descripcionTarea(self):
        return self.__descripcionTarea
    @descripcionTarea.setter
    def descripcionTarea(self, descripcionTarea):
        self.__descripcionTarea = descripcionTarea
    @descripcionTarea.deleter
    def descripcionTarea(self):
        del self.__descripcionTarea    

    def __str__ (self):
        return f"Datos del registro de tiempo:\nRUT Empleado: {self.rutEmpleado}\nFecha: {self.fecha}\nHoras trabajadas: {self.horasTrabajadas}\nDescripción de tarea: {self.descripcionTarea}"
    
    def crear(self):
        while True:
            try:
                rut = input("Ingrese el RUT del empleado (ej: 12345678-K o 9876543-1): ").strip().lower()
                if validar_rut(rut):
                    break
            except ValueError as Error:
                print(Error)

        resultado_rut = buscar_empleado_general(rut)

        if resultado_rut:
            print("El usuario se encuentra registrado en el sistema.")
            while True:
                try:
                    id_proyecto = int(input("Ingrese la ID del proyecto que desea buscar: "))
                    break
                except ValueError as Error:
                    print(f"Error inesperado: {Error}")
            
            resultado_pro = buscar_proyecto_general(id_proyecto)

            if resultado_pro:
                while True:
                    try:
                        fecha= input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
                        fecha1 = datetime.strptime(fecha, '%d/%m/%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha1}")
                        break
                    except ValueError:
                        print("Formato inválido. Use el formato DD/MM/AAAA.")

                while True:
                    try:
                        horas_trabajadas = int(input("Ingrese un número de hasta 3 dígitos: "))
                        if 1 <= horas_trabajadas <= 999:
                            break
                        else:
                            print("El número puede tener solo hasta 3 dígitos.")
                    except ValueError:
                        print("Debe ingresar solo números enteros.")

                while True:
                    try:
                        descripcion = input("Agrege una descripcion al registro de tiempo: ")
                        if not descripcion:
                            raise ValueError("No puede quedar el campo vacio")
                        break 
                    except ValueError as Error:
                        print(Error)

                try:
                    conexion = conectar_db()
                    cursor = conexion.cursor()
                    query = """
                        INSERT INTO registro_tiempo (
                            fecha, horas_trabajadas, descripcion_tarea, 
                            rut_usuario, id_proyetco 
                        ) VALUES (%s, %s, %s, %s, %s)
                    """
                    valores = (
                        fecha, horas_trabajadas, descripcion, rut, id_proyecto
                    )
                    cursor.execute(query, valores)
                    conexion.commit()
                    cursor.close()
                    conexion.close()
                    id_generado = cursor.lastrowid
                    print(f"Departamento creado con ID: {id_generado}")
                except Exception as e:
                    print(f"Error al guardar al administrador: {e}")
                finally:
                    cursor.close()
                    conexion.close()

            else:
                print("El proyecto no está registrado.")
        else:
            print("El usuario no está registrado.")

    def modificar(self):
        while True:
            try:
                id_registro_tiempo = int(input("Ingrese el ID del registro de tiempo a modificar: "))
                if not id_registro_tiempo:
                     raise ValueError("No puede dejar el campo vacio")
                break
            except ValueError as Error:
                print(Error)
                

        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM registro_timepo WHERE id_registro_tiempo = %s", (id_registro_tiempo,))
            registro_tiempo = cursor.fetchone()

            if not registro_tiempo:
                print("No se encontró ningún registro de tiempo con esa ID.")
                return

            print("\nRegistro de tiempo encontrado. ¿Qué campo desea modificar?")
            print("1. Fecha")
            print("2. Horas Trabajadas")
            print("3. Descripción")
            print("4. ID Proyecto")

            try:
                opcion = int(input("Seleccione una opción (1..4): "))
                campos = {
                    1: "fecha",
                    2: "horas trabajadas",
                    3: "descripcion",
                    4: "id proyecto"
                }
            except ValueError:
                print("Debe ingresar un carácter numérico para continuar.")
                return
            
            if opcion not in campos:
                print("Opción inválida.")
                return
                                
            campo = campos[opcion]
            print(f"Valor actual de '{campo}': {registro_tiempo[campo]}")
            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}': ").strip()

            if campo == "fecha":
                try:
                    nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y").date()
                except ValueError:
                    print("Formato de fecha inválido. Use DD/MM/AAAA para continuar.")
            elif campo == "horas trabajadas":
                nuevo_valor = int(nuevo_valor)  
                if not 1 <= nuevo_valor <= 999:
                    raise ValueError("El numero debe estar entre el 1 y el 999") #dudas sobre si esto va a funcionar
            elif campo == "descripcion":
                if not nuevo_valor:
                    raise ValueError("La descripción no puede estar vacía.")
            elif campo == "id_proyecto":
                nuevo_valor = int(nuevo_valor)
                if not nuevo_valor:
                    raise ValueError("El campo no puede quedar vacio")  

            while True:
                confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
                if confirmacion == "s":
                    break
                elif confirmacion == "n":
                    print("Modificación cancelada.")
                    return
                else:
                    print("Entrada inválida. Debes ingresar 'S' o 'N'.")

            query = f"UPDATE proyecto SET {campo} = %s WHERE id_proyecto = %s"
            cursor.execute(query, (nuevo_valor, id_registro_tiempo))
            conexion.commit()
            print("Modificación realizada con éxito.")

        except ValueError as Error:
            print(f"Error: {Error}")
        except Exception as e:
            print(f"Error inesperado al modificar el proyecto: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
                
        print("Registro de tiempo modificado")

    def eliminar(self):
        while True:
            try:
                id_registro_tiempo = int(input("Ingrese la ID del registro de tiempo que desea eliminar: "))
                break
            except ValueError as Error:
                print(f"Error inesperado: {Error}")
        
            try:
                conexion = conectar_db()
                cursor = conexion.cursor(dictionary=True)

                cursor.execute("SELECT id_registro_tiempo, rut_usuario, descripcion_tarea FROM registro_tiempo WHERE id_registro_tiempo = %s", (id_registro_tiempo,))
                RegistroTiempo = cursor.fetchone()

                if not RegistroTiempo:
                    print(f"No se encontró ningún registro de tiempo con la ID ingresada: {id_registro_tiempo}")
                    return
                
                print("\nProyecto encontrado:")
                print(f"ID del proyecto: {RegistroTiempo['id_registro_tiempó']}")
                print(f"RUT del usuario: {RegistroTiempo['rut_usuario']}")
                print(f"Descripción: {RegistroTiempo['descripcion_tarea']}")

                while True:
                    confirmacion = input("¿Está seguro que desea eliminar este registro de tiempo? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
                    if confirmacion == 's':
                        break
                    elif confirmacion == 'n':
                        print("Operación cancelada.")
                        return
                    else:
                        print("Entrada inválida, debes ingresar 'S' o 'N' para poder continuar.")
                
                cursor.execute("DELETE FROM registro_tiempo WHERE id_registro_tiempo = %s", (id_registro_tiempo,))
                conexion.commit()
                print(f"\nEl registro de tiempo ha sido eliminado exitosamente.")

            except Exception as Error:
                print(f"Error inesperado: {Error}")
            finally:
                if cursor:
                    cursor.close()
                if conexion:
                    conexion.close()
                print("Registro de tiempo eliminado")
            