# Lógica de LogIn del sistema, con opciones de iniciar sesión y registro. // posiblemente también recuperar contraseña
from functions import validar_rut, buscar_empleado
import bcrypt
import re

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

def registrar_usuario():
    while True:
        try:
            rut = input("Ingrese su RUT: (ej: 12345678-K o 9876543-1): ").strip().lower()
            rut = validar_rut(rut)
            if not buscar_empleado(rut):
                print("El usuario ya está registrado. No se puede continuar.")
                return
            break
        except ValueError as Error:
            print(f"Error inesperado al ingresar el RUT: {Error}")

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
