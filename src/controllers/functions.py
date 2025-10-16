from config import conectar_db
from itertools import cycle
from datetime import datetime, date
from models import (Persona,
                    Empleado,
                    Gerente,
                    Administrador)
import mysql.connector
import re

def validar_rut(rut):
    rut = rut.strip().lower()
    if rut.count('-') != 1:
            raise ValueError("El RUT debe contener un solo guion ('-').")

    parte_num, dv = rut.split('-')

    if len(rut) < 9 or len(rut) > 10:
        raise ValueError("El RUT debe tener entre 9 y 10 caracteres en total.")

    if not parte_num.isdigit():
        raise ValueError("Los caracteres antes del guion deben ser solo números.")

    if len(parte_num) not in [7, 8]:
        raise ValueError("La parte numérica del RUT debe tener 7 u 8 dígitos.")

    if dv not in ['0','1','2','3','4','5','6','7','8','9','k']:
        raise ValueError("El dígito verificador debe ser un número o la letra 'k'.")

    print(f"RUT ingresado correctamente: {rut.upper()}")
    return rut.upper()



def buscar_empleado(rut):
    try:
        rut = validar_rut(rut)  # Si es válido, retorna el RUT limpio
        print(f"RUT ingresado correctamente: {rut}")
    except ValueError as Error:
        print(Error)
        return  # Salir si el RUT no es válido

    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
        SELECT rut_usuario
        FROM usuario
        WHERE rut_usuario = %s
        """
        cursor.execute(query, (rut,))
        resultado = cursor.fetchone()

        if resultado:
            print("¡ERROR!. El usuario se encuentra registrado en el sistema.\n")
        else:
            print("El usuario no está registrado.")
    except Exception as e:
        print(f"Error inesperado al buscar el empleado: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


# Función exclusiva de Administrador y Gerente (o cualquier clase que vaya a poseer esos privilegios)
def super_buscar_empleado():
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

def modificar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a modificar: ").strip().upper()
            if validar_rut():
                print(f"RUT ingresado correctamente: {rut.upper()}")
                break
        except ValueError as Error:
            print(Error)

        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute("SELECT * FROM Usuario WHERE rut_usuario = %s", (rut,))
            empleado = cursor.fetchone()

            if not empleado:
                print("No se encontró ningún empleado con ese RUT.")
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
            print("9. Rol")
            print("10. ID Departamento")
        except Exception as e:
            print(f"Error al guardar el empleado: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

        try:
            opcion = int(input("Seleccione una opción (1-10): "))
            campos = {
                1: "nombres",
                2: "apellido_paterno",
                3: "apellido_materno",
                4: "direccion",
                5: "fecha_nacimiento",
                6: "fecha_inicio_contrato",
                7: "salario",
                8: "numero_telefonico",
                9: "rol",
                10: "id_departamento"
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
            elif campo == "rol":
                roles_validos = {"empleado", "gerente", "administrador"}
                if nuevo_valor.lower() not in roles_validos:
                    raise ValueError("Rol inválido. Debe ser: Empleado, Gerente o Administrador.")
                nuevo_valor = nuevo_valor.capitalize()
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

            query = f"UPDATE Usuario SET {campo} = %s WHERE rut_usuario = %s"
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

def eliminar_empleado():
    while True:
        try:
            rut = input("Ingrese el RUT del empleado a eliminar (ej: 12345678-K): ").strip().lower()
            if validar_rut(rut):
                rut = rut.upper()
                break
        except ValueError as Error:
            print(Error)

    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombres, apellido_paterno, rol FROM Usuario WHERE rut_usuario = %s", (rut,))
    empleado = cursor.fetchone()

    if not empleado:
        print("No se encontró ningún empleado con ese RUT.")
        cursor.close()
        conexion.close()
        return
    
    print("\nEmpleado encontrado:")
    print(f"Nombre: {empleado['nombres']} {empleado['apellido_paterno']}")
    print(f"Rol: {empleado['rol']}")

    confirmacion = input("¿Estás seguro que deseas eliminar este empleado? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        cursor.close()
        conexion.close()
        return
    
    try:
        cursor.execute("DELETE FROM Usuario WHERE rut_usuario = %s", (rut,))
        conexion.commit()
        print(f"El empleado con RUT {rut} ha sido eliminado de forma permanente.\n")
    except Exception as e:
        print(f"Error inesperado al eliminar: {e}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def insertar_empleado(datos_basico, datos_detalle):
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        query_basico = """
            INSERT INTO usuario_basico (
                rut_usuario, nombres, apellido_paterno, apellido_materno,
                fecha_nacimiento, numero_telefonico, contraseña, rol
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        query_detalle = """
            INSERT INTO usuario_detalle (
                rut_usuario, direccion, fecha_inicio_contrato,
                salario, rol, id_departamento
            )   VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_basico, datos_basico)
        cursor.execute(query_detalle, datos_detalle)
        conexion.commit()
        print("Empleado creado con éxito.\n")

    except mysql.connector.Error as Error:
        print(f"Error al insertar ejemplo: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def menu_gestion_emp(admin: Administrador):
    print("MENÚ DE GESTION DE EMPLEADOS\n")
    while True:
        print("OPCIÓN 1. CREAR EMPLEADO")
        print("OPCIÓN 2. BUSCAR EMPLEADO")
        print("OPCIÓN 3. MODIFICAR EMPLEADO")
        print("OPCIÓN 4. ELIMINAR EMPLEADO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.\n")
            continue

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.\n")
            continue

        match opcion_user:
            case 1:
                admin.crear_empleado() 

            case 2:
                admin.buscar_empleado()

            case 3:
                admin.modificar_empleado()

            case 4:
                admin.eliminar_empleado()

            case 5:
                while True:
                    print("Será devuelto al menú principal...")
                    opcion = input("PRESIONE ENTER PARA CONTINUAR ")
                    if opcion == "":
                        break  
                    else:
                        print("No escriba nada, solo presione ENTER para continuar.")

def menu_gestion_depto():
    print("MENÚ DE GESTION DE DEPARTAMENTOS\n")
    while True:
        print("OPCIÓN 1. CREAR DEPARTAMENTO")
        print("OPCIÓN 2. BUSCAR DEPARTAMENTO")
        print("OPCIÓN 3. MODIFICAR DEPARTAMENTO")
        print("OPCIÓN 4. ELIMINAR DEPARTAMENTO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                while True:
                    try: 
                        nombre = input("Ingrese el nombre del departamento: ").strip()
                        if not nombre or not all(c.isalpha() or c.isspace() for c in nombre):
                            raise ValueError("Ingrese un nombre válido (solo letras y espacios).")
                        break
                    except ValueError as Error:
                        print(Error)

                while True:
                    try:
                        rut_gerente_asociado = input("Ingrese el RUT del gerente (ej: 12345678-K): ").strip().lower()
                        parte_num, dv = rut_gerente_asociado.split('-')
                        if rut_gerente_asociado.count('-') != 1 or not parte_num.isdigit() or dv not in '0123456789k':
                            raise ValueError("RUT inválido.")
                        print(f"RUT ingresado correctamente: {rut_gerente_asociado.upper()}")
                        break
                    except ValueError as Error:
                        print(Error)

                ##from config import conectar_db
                try:
                    conexion = conectar_db()
                    cursor = conexion.cursor()
                    query = "INSERT INTO departamento (nombre, rut_gerente_asociado) VALUES (%s, %s)"
                    valores = (nombre, rut_gerente_asociado.upper())
                    cursor.execute(query, valores)
                    conexion.commit()
                    id_generado = cursor.lastrowid
                    print(f"Departamento creado con ID: {id_generado}")
                except Exception as e:
                    print(f"Error al crear el departamento: {e}")
                finally:
                    cursor.close()
                    conexion.close()

            case 2:
                def buscar_departamento():
                    while True:
                        try:
                            id_departamento = int(input("Ingrese el ID del departamento: "))
                            break
                        except ValueError as Error:
                                print(Error)

                        conexion = conectar_db()
                        cursor = conexion.cursor()

                        query = """
                        SELECT id_departamento, nombre, rut_gerente_asociado    
                        FROM departamento
                        WHERE id_departamento = %s
                    """
                        cursor.execute(query, (id_departamento,))
                        resultado = cursor.fetchone()

                        cursor.close()
                        conexion.close()

                        if resultado:
                            print("\nDatos del departamento encontrado:")
                            campos = ["ID Departamento",
                                    "Nombre",
                                    "Rut del gerente asociado"]
                            
                            for campo, valor in zip(campos, resultado):
                                print(f"{campo}: {valor}")
                            print()
                        else:
                            print("No se encontró a ningún departamento con esta ID.\n")

            case 3:
                def modificar_departamento():
                    while True:
                        try:
                            id_departamento = int(input("Ingrese el ID del departamento a modificar: "))
                            break
                        except ValueError as Error:
                            print(Error)

                        try:
                            conexion = conectar_db()
                            cursor = conexion.cursor()

                            cursor.execute("SELECT * FROM departamento WHERE id_departamento = %s", (id_departamento,))
                            departamento = cursor.fetchone()

                            if not departamento:
                                print("No se encontró ningún departamento con esa ID.")
                                cursor.close()
                                conexion.close()
                                return
                        
                            print("\nDepartamento encontrado. ¿Qué campo desea modificar?")
                            print("1. Nombre")
                            print("2. Descripción")
                        except Exception as e:
                            print(f"Error al guardar el departamento: {e}")
                        finally:
                            if cursor:
                                cursor.close()
                            if conexion:
                                conexion.close()

                        try:
                            opcion = int(input("Seleccione una opción (1-2): "))
                            campos = {
                                1: "nombre",
                                2: "descripcion",
                            }
                            if opcion not in campos:
                                print("Opción inválida.")
                                return
                            
                            campo = campos[opcion]
                            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}'").strip()

                            if campo == "nombre":
                                if not nuevo_valor or not all(c.isalpha() or c.isspace() for c in nuevo_valor):
                                    raise ValueError("Solo se permiten letras y espacios.")
                            elif campo == "descripcion":
                                if not nuevo_valor:
                                    raise ValueError("La descripción no puede estar vacía.")

                            while True:
                                confirmacion = input(f"¿Confirmas modificar '{campo}' a '{nuevo_valor}'? (S/N): ").strip().lower()
                                if confirmacion == "s":
                                    break
                                elif confirmacion == "n":
                                    print("Modificación cancelada.")
                                    return
                                else:
                                    print("Entrada inválida. Debes ingresar 'S' o 'N'.")

                            query = f"UPDATE departamento SET {campo} = %s WHERE id_departamento = %s"
                            cursor.execute(query, (nuevo_valor, id_departamento))
                            conexion.commit()
                            print("Modificación realizada con éxito.")

                        except ValueError as Error:
                            print(f"Error: {Error}")
                        finally:
                            if cursor:
                                cursor.close() 
                            if conexion:
                                conexion.close()

            case 4:
                def eliminar_departamento():
                    while True:
                        try:
                            id_departamento = int(input("Ingrese la ID del departamento que desea eliminar: "))
                            break
                        except ValueError as Error:
                            print(Error)

                    conexion = conectar_db()
                    cursor = conexion.cursor(dictionary=True)
                    cursor.execute("SELECT id_departamento, nombre, descripcion FROM departamento WHERE id_departamento = %s", (id_departamento,))
                    departamento = cursor.fetchone()

                    if not departamento:
                        print("No se encontró ningún departamento con esta ID.")
                        cursor.close()
                        conexion.close()
                        return
                        
                    print("\nDepartamento encontrado:")
                    print(f"ID del departamento: {departamento['id_departamento']}") 
                    print(f"Nombre del departamento: {departamento['nombre']}")
                    print(f"Descripción: {departamento['descripcion']}")

                    while True:
                        confirmacion = input("¿Estás seguro que deseas eliminar este departamento? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
                        if confirmacion == "s":
                            break
                        elif confirmacion == "n":
                            print("Operación cancelada.")
                            cursor.close()
                            conexion.close()
                            return
                        else:
                            print("Entrada inválida. Debes ingresar 'S' o 'N'.")  
                            
                    try:
                        cursor.execute("DELETE FROM departamento WHERE id_departamento = %s", (id_departamento,))
                        conexion.commit()
                        print(f"El departamento con la ID {id_departamento}, ha sido eliminado de forma permanente.\n")
                    except Exception as e:
                        print(f"Error inesperado al eliminar: {e}")
                    finally:
                        if cursor:
                            cursor.close()
                        if conexion:
                            conexion.close()


            case 5:
                while True:
                    print("Será devuelto al menú principal...")
                    opcion = input("PRESIONE ENTER PARA CONTINUAR ")
                    if opcion == "":
                        break  
                    else:
                        print("No escriba nada, solo presione ENTER para continuar.")

def menu_gestion_informe():
    print("MENÚ DE GESTION DE INFORMES\n")
    while True:
        print("OPCIÓN 1. CREAR INFORME")
        print("OPCIÓN 2. BUSCAR INFORME")
        print("OPCIÓN 3. MODIFICAR INFORME")
        print("OPCIÓN 4. ELIMINAR INFORME")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass

            case 5:
                while True:
                    print("Será devuelto al menú principal...")
                    opcion = input("PRESIONE ENTER PARA CONTINUAR ")
                    if opcion == "":
                        break  
                    else:
                        print("No escriba nada, solo presione ENTER para continuar.")

def menu_gestion_proyecto():
    print("MENÚ DE GESTION DE PROYECTOS\n")
    while True:
        print("OPCIÓN 1. CREAR PROYECTO")
        print("OPCIÓN 2. BUSCAR PROYECTO")
        print("OPCIÓN 3. MODIFICAR PROYECTO")
        print("OPCIÓN 4. ELIMINAR PROYECTO")
        print("OPCIÓN 5. VOLVER AL MENÚ PRINCIPAL\n")
        try: 
            opcion_user = int(input("Ingresar opción (1 - 5): "))
        except ValueError:
            print("Debe ingresar una opción válida para continuar.")

        if opcion_user not in (1,2,3,4,5):
            print("Debe ingresar una de las opciones disponibles (1 - 5) para continuar.")
            continue

        match opcion_user:
            case 1:
                def crear_proyecto():
                    while True:
                        try: 
                            nombre = input("Ingrese el nombre del departamento: ")
                            if not nombre and all(c.isalpha() for c in nombre):
                                raise ValueError("Ingrese un nombre valido")
                            break
                        except ValueError as Error:
                            print(Error)
                    
                    while True:
                        try:
                            descripcion_proyecto = input("Ingrese una descripcion al proyecto: ")
                            if not descripcion_proyecto:
                                raise ValueError("Ingrese una descripcion valida")
                            break
                        except ValueError as Error:
                            print(Error)

                    while True:
                        try:
                            fecha_inicio_proyecto = input("Ingrese la fecha de inicio del proyecto (formato DD/MM/AAAA): ")
                            fecha = datetime.strptime(fecha_inicio_proyecto, '%d/%m/%Y').date()
                            print(f"Fecha ingresada correctamente: {fecha}")
                            break
                        except ValueError:
                            print("Formato inválido. Use el formato DD/MM/AAAA.")
                    
                    #falta instanciar la clase de proyecto y guardarla en la DB

            case 2:
                def buscar_proyecto():
                    while True:
                        try:
                            id_proyecto = int(input("Ingrese el la ID del proyecto que desea buscar: "))
                            break
                        except ValueError as Error:
                            print(Error)

                    conexion = conectar_db()
                    cursor = conexion.cursor()

                    query = """
                    SELECT id_proyecto, nombre, descripcion, fecha_inicio, 
                           id_departamento   
                    FROM usuario
                    WHERE id_proyecto = %s
                """
                    cursor.execute(query, (id_proyecto,))
                    resultado = cursor.fetchone()

                    cursor.close()
                    conexion.close()

                    if resultado:
                        print("\nDatos del proyecto encontrado:")
                        campos = ["ID Proyecto",
                                  "Nombre",
                                  "Descripcion",
                                  "Fecha de inicio",
                                  "ID Departamento"]
                        
                        for campo, valor in zip(campos, resultado):
                            print(f"{campo}: {valor}")
                        print()
                    else:
                        print("No se encontró a ningún proyecto con esta ID.\n")

            case 3:
                def modificar_proyecto():
                    while True:
                        try:
                            id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
                            break
                        except ValueError as Error:
                            print(Error)

                        try:
                            conexion = conectar_db()
                            cursor = conexion.cursor()

                            cursor.execute("SELECT * FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
                            proyecto = cursor.fetchone()

                            if not proyecto:
                                print("No se encontró ningun proyecto con esa ID.")
                                cursor.close()
                                conexion.close()
                                return
                        
                            print("\nProyecto encontrado. ¿Qué campo desea modificar?")
                            print("1. Nombre")
                            print("2. Descripción")
                            print("3. Fecha de inicio")
                        except Exception as e:
                            print(f"Error al guardar el proyecto: {e}")
                        finally:
                            if cursor:
                                cursor.close()
                            if conexion:
                                conexion.close()

                        try:
                            opcion = int(input("Seleccione una opción (1-3): "))
                            campos = {
                                1: "nombre",
                                2: "descripcion",
                                3: "fecha_inicio",
                            }
                            if opcion not in campos:
                                print("Opción inválida.")
                                return
                            
                            campo = campos[opcion]
                            nuevo_valor = input(f"Ingrese el nuevo valor para '{campo}'").strip()

                            if campo == "nombre":
                                if not nuevo_valor or not all(c.isalpha() or c.isspace() for c in nuevo_valor):
                                    raise ValueError("Solo se permiten letras y espacios.")
                            elif campo == "descripcion":
                                if not nuevo_valor:
                                    raise ValueError("La descripción no puede estar vacía.")
                            elif campo == "fecha_inicio":
                                nuevo_valor = datetime.strptime(nuevo_valor, "%d/%m/%Y").date()
                            
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
                            cursor.execute(query, (nuevo_valor, id_proyecto))
                            conexion.commit()
                            print("Modificación realizada con éxito.")

                        except ValueError as Error:
                            print(f"Error: {Error}")
                        finally:
                            if cursor:
                                cursor.close() 
                            if conexion:
                                conexion.close()

            case 4:
                def eliminar_proyecto():
                    while True:
                        try:
                            id_proyecto = int(input("Ingrese la ID del proyecto que desea eliminar: "))
                            break
                        except ValueError as Error:
                            print(Error)

                    conexion = conectar_db()
                    cursor = conexion.cursor(dictionary=True)
                    cursor.execute("SELECT id_proyecto, nombre, descripcion FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
                    proyecto = cursor.fetchone()

                    if not proyecto:
                        print("No se encontró ningún proyecto con esta ID.")
                        cursor.close()
                        conexion.close()
                        return
                        
                    print("\nProyecto encontrado:")
                    print(f"ID del proyecto: {proyecto['id_proyecto']}") 
                    print(f"Nombre del proyecto: {proyecto['nombre']}")
                    print(f"Descripción: {proyecto['descripcion']}")

                    while True:
                        confirmacion = input("¿Estás seguro que deseas eliminar este proyecto? Esta acción no se podrá deshacer. (S/N): ").strip().lower()
                        if confirmacion == "s":
                            break
                        elif confirmacion == "n":
                            print("Operación cancelada.")
                            cursor.close()
                            conexion.close()
                            return
                        else:
                            print("Entrada inválida. Debes ingresar 'S' o 'N'.")  
                            
                    try:
                        cursor.execute("DELETE FROM proyecto WHERE id_proyecto = %s", (id_proyecto,))
                        conexion.commit()
                        print(f"El proyecto con la ID {id_proyecto}, ha sido eliminado de forma permanente.\n")
                    except Exception as e:
                        print(f"Error inesperado al eliminar: {e}")
                    finally:
                        if cursor:
                            cursor.close()
                        if conexion:
                            conexion.close()

            case 5:
                while True:
                    print("Será devuelto al menú principal...")
                    opcion = input("PRESIONE ENTER PARA CONTINUAR ")
                    if opcion == "":
                        break  
                    else:
                        print("No escriba nada, solo presione ENTER para continuar.")