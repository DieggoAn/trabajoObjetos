from datetime import datetime
from functions.functions_api import(consulta_valor_dia,
                                    consulta_valor_hoy,
                                    consulta_valor_rango)
from models.Persona import Persona

def menu_uf(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(UF)\n")
        print("         1.- VALOR DE LA UF HOY          ")
        print("         2.- VALOR DE LA UF EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DE LA UF EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "uf"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "uf"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "uf"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_ivp(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(IVP)\n")
        print("         1.- VALOR DE LA IVP HOY          ")
        print("         2.- VALOR DE LA IVP EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DE LA IVP EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "ivp"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "ivp"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "ivp"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_ipc(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(ICP)\n")
        print("         1.- VALOR DE LA ICP HOY          ")
        print("         2.- VALOR DE LA ICP EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DE LA ICP EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "ipc"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "ipc"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "ipc"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break
            


def menu_utm(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(UTM)\n")
        print("         1.- VALOR DE LA UTM HOY          ")
        print("         2.- VALOR DE LA UTM EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DE LA UTM EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "utm"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "utm"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "utm"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final. usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_dolar(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(DOLAR)\n")
        print("         1.- VALOR DEL DÓLAR HOY          ")
        print("         2.- VALOR DEL DÓLAR EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DEL DÓLAR EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ")
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "dolar"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "dolar"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "dolar"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break


def menu_euro(usuario: Persona):
    while True:
        print("CONSULTA DE INDICADORES ECONÓMICOS(EURO)\n")
        print("         1.- VALOR DEL EURO HOY          ")
        print("         2.- VALOR DEL EURO EN UNA FECHA ESPECÍFICA         ")
        print("         3.- VALOR DEL EURO EN UN RANGO DE TIEMPO         ")
        print("         4.- VOLVER AL MENÚ ANTERIOR          ") 
        try:
            opcion = int(input("Ingrese el numero del indicador que desea usar: "))
        except ValueError:
            print("Debe ingresar un numero entero del 1-4")

        if opcion not in (1,2,3,4):
            print("Debe ingresar una de las opciones del 1-4")

        match opcion:
            case 1:
                tipo_valor = "euro"
                consulta_valor_hoy(tipo_valor, usuario)
            case 2:
                tipo_valor = "euro"
                while True:
                    try:
                        fecha_consulta = input("Ingrese la fecha del informe (formato DD-MM-AAAA): ")
                        fecha = datetime.strptime(fecha_consulta, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_dia(tipo_valor, fecha, usuario)
            case 3:
                tipo_valor = "euro"
                while True:
                    try:
                        fecha_inicial_str = input("Ingrese la fecha inicial que desea consultar (formato DD-MM-AAAA): ")
                        fecha_inicial = datetime.strptime(fecha_inicial_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_inicial}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")

                while True:
                    try:
                        fecha_final_str = input("Ingrese la fecha final que desea consultar (formato DD-MM-AAAA): ")
                        fecha_final = datetime.strptime(fecha_final_str, '%d-%m-%Y').date()
                        print(f"Fecha ingresada correctamente: {fecha_final}")
                        break  
                    except ValueError:
                        print("Formato de fecha incorrecto. Intente nuevamente (ejemplo: 25-12-2024).")
                consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario)
            case 4:
                print("Volviendo al menú anterior...")
                input("PRESIONE ENTER PARA CONTINUAR ")
                break