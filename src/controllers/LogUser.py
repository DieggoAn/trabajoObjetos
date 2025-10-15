# Lógica de LogIn del sistema, con opciones de iniciar sesión y registro. // posiblemente también recuperar contraseña

import mysql.connector
from functions import validar_rut, buscar_empleado
from config import conectar_db
import bcrypt
import re
from datetime import datetime
from models import Empleado

def presentacion_login():
    while True:
        print("Bienvenido al sistema de EcoTech Solutions\n")
        print("--- OPCIONES DISPONIBLES ---\n")
        print("1. INICIAR SESIÓN.")
        print("2. REGISTRARSE.")
        print("3. CERRAR EL PROGRAMA.\n")
        try:
            opcion_user = int(input("Ingrese una de las opciones disponibles (1-3): "))
        except ValueError:
            print("Debe ingresar un carácter numérico para continuar.")
            continue

        if opcion_user not in (1,2,3):
            print("Debe ingresar una de las opciones disponibles para continuar.")
            continue

        match opcion_user:
            case 1:
                iniciar_sesion()

            case 2:
                registrar_usuario()

            case 3:
                input("PRESIONE ENTER PARA SALIR ")
                break


# IMPORTANTE: el usuario al registrarse, automaticamente adquirirá el rol de EMPLEADO,
# para cambiarlo, lo debe hacer un usuario con el perfil de Administrador.
def registrar_usuario():
    while True:
        try:
            rut = input("Ingrese su RUT: (ej: 12345678-K o 9876543-1): ").strip().lower()
            validar_rut(rut)
            if not buscar_empleado(rut):
                print("El usuario ya está registrado. No se puede continuar.")
                return
            break
        except ValueError as Error:
            print(f"Error inesperado al ingresar el RUT: {Error}")
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
            nro_telefono = input("Ingrese el número de teléfono del empleado (formato: +56 9 XXXX XXXX): ").strip()
            patron = r"^\+56 9 \d{4} \d{4}$"
            if not re.match(patron, nro_telefono):
                raise ValueError("Formato inválido. Use: +56 9 XXXX XXXX")
            break
        except ValueError as Error:
            print(Error)

    while True:
        try:
            print("Requisitos para una contraseña segura:\n")
            print("Al menos una letra mayúsculas.")
            print("Al menos una letra minúsculas.")
            print("Al menos un número.")
            print("Al menos un carácter especial.\n")

            contraseña_texto_plano = input("Crea una contraseña: ").strip()
            validar_contraseña_segura(contraseña_texto_plano)
            
            confirmacion = input("Confirma tu contraseña: ").strip()
            if contraseña_texto_plano != confirmacion:
                raise ValueError("Las contraseñas no coinciden.")
            
            salt = bcrypt.gensalt()
            contraseña_user = bcrypt.hashpw(contraseña_texto_plano.encode('utf-8'), salt)
            print("Contraseña registrada exitosamente.")
            break
        except ValueError as Error:
            print(f"Error inesperado al ingresar la contraseña: {Error}")
        
    usuario = Empleado(
        rut=rut,
        nombres=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        direccion=direccion,
        fecha_nacimiento=fecha,
        fecha_inicio_contrato=None,  
        salario=None,                
        telefono=nro_telefono,
        contraseña=contraseña_user,
        rol="Empleado",
        id_departamento=None         
    )

    try:    
        conexion = conectar_db()
        cursor = conexion.cursor()

        query = """
        INSERT INTO usuario_basico (
            rut_usuario, nombres, apellido_paterno, apellido_materno,
            fecha_nacimiento, numero_telefonico, contraseña
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            rut, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, nro_telefono, contraseña_user
        )
    
        cursor.execute(query, valores)
        conexion.commit()
        print("\nRegistro exitoso. Tu cuenta ha sido creada con el rol de 'Empleado'.")
    except mysql.connector.Error as error:
        print(f"Error inesperado al registrar el usuario: {error}")
    finally:
        cursor.close()
        conexion.close()

def iniciar_sesion():
    pass

def validar_contraseña_segura(contraseña):
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    
    if not re.search(r"[A-Z]", contraseña):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula.")
    
    if not re.search(r"[a-z]", contraseña):
        raise ValueError("La contraseña debe contener al menos una letra minúscula.")
    
    if not re.search(r"\d", contraseña):
        raise ValueError("La contraseña debe contener al menos un número.")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        raise ValueError("La contraseña debe contener al menos un carácter especial.")
    
    return True
