import requests, json, mysql.connector
from datetime import datetime, timedelta
from config import conectar_db
from models.Verificador import Autentificador
from models.Persona import Persona

aut = Autentificador()
def consulta_valor_hoy(tipo_valor, usuario: Persona):
    autor = "mindicador.cl"
    
    url = requests.get(f'https://mindicador.cl/api/{tipo_valor}')
    string = url.text
    datos = json.loads(string)
    fecha_consulta = datetime.now()
    fecha_actual = datetime.now()
    rut_usuario = usuario.rut
        
    serie = datos.get('serie', [])
    if serie:
        valor = serie[0]['valor']
        print(f"El valor de {tipo_valor} hoy es de ${valor}")
    else:
        print(f"No hay datos disponibles para {tipo_valor} hoy.")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        query = """
            INSERT INTO indicadores_economicos (rut_usuario, fecha_consulta, nombre_indicador, valor, fecha_consulta, proveedor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (rut_usuario, fecha_consulta, tipo_valor, valor, fecha_consulta, autor)
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Detalles de consulta creado, ID de consulta generado: {id_generado} \n")

    except Exception as Error:
        print(f"Error al crear detalles de consulta: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()



def consulta_valor_dia(tipo_valor, fecha_consulta, usuario:Persona):
    autor = "mindicador.cl"

    url = requests.get(f'https://mindicador.cl/api/{tipo_valor}/{fecha_consulta}')
    string = url.text
    datos = json.loads(string)
    fecha_actual = datetime.now()
    rut_usuario = usuario.rut

    serie = datos.get('serie', [])
    if serie:
        valor = serie[0]['valor']
        print(f"El valor de {tipo_valor} en la fecha {fecha_consulta} es de ${valor}")
    else:
        print(f"No hay datos disponibles para {tipo_valor} el {fecha_consulta}.")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        query = """
            INSERT INTO indicadores_economicos (rut_usuario, fecha_actual, nombre_indicador, valor, fecha_consulta, proveedor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (rut_usuario, fecha_actual, tipo_valor, valor, fecha_consulta, autor)
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Detalles de consulta creado, ID de consulta generado: {id_generado} \n")

    except Exception as Error:
        print(f"Error al crear detalles de consulta: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()



def consulta_valor_rango(tipo_valor, fecha_inicial, fecha_final, usuario: Persona):
    autor = "mindicador.cl"
            
    for i in range((fecha_final - fecha_inicial).days + 1):
        fecha_iterada = fecha_inicial + timedelta(days = i)
        fecha_iterada_str = fecha_iterada.strftime("%d-%m-%Y")
        print(type(fecha_iterada))

        url = requests.get(f'https://mindicador.cl/api/{tipo_valor}/{fecha_iterada_str}')
        string = url.text
        datos = json.loads(string)
        fecha_actual = datetime.now()
        rut_usuario = usuario.rut

        serie = datos.get('serie', [])
        if serie:
            valor = serie[0]['valor']
            print(f"El valor de {tipo_valor} en la fecha {fecha_iterada} es de ${valor}")
        else:
            print(f"No hay datos disponibles para {tipo_valor} el {fecha_iterada_str}.")

    try:
        conexion = conectar_db()
        cursor = conexion.cursor(dictionary=True)
        query = """
            INSERT INTO indicadores_economicos (rut_usuario, fecha_actual, nombre_indicador, valor, fecha_consulta, proveedor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (rut_usuario, fecha_actual, tipo_valor, valor, fecha_iterada, autor)
        cursor.execute(query, valores)
        conexion.commit()
        id_generado = cursor.lastrowid
        print(f"Detalles de consulta creado, ID de consulta generado: {id_generado} \n")

    except Exception as Error:
        print(f"Error al crear detalles de consulta: {Error}")
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
