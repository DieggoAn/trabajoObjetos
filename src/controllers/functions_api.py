import requests
import json
from datetime import date, timedelta, datetime

###Iterador de fechas https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days+1):
        yield start_date + timedelta(n)


def consulta_UF(fecha = None, fecha2 = None):
    if fecha is None and fecha2 is None:
        url = requests.get("https://mindicador.cl/api/uf")
        text = url.text
        datos = json.loads(text)
        for clave, valor in datos.items():
            if clave == 'serie':
                print("El valor de la UF es: {} CLP".format(valor[0]['valor']))
    elif fecha is not None and fecha2 is None:
        fechaString =fecha.strftime("%d-%m-%Y")
        url = requests.get(f"https://mindicador.cl/api/uf/{fechaString}")
        text = url.text
        datos = json.loads(text)        
        for clave, valor in datos.items():
            if clave == 'serie':
                print("El valor de la UF para el dia {} es de: {} CLP".format(fecha,valor[0]['valor']))
    elif fecha is not None and fecha2 is not None:
        for fecha_actual in daterange(fecha, fecha2):
            fechaString = fecha_actual.strftime("%d-%m-%Y")
            url = requests.get(f"https://mindicador.cl/api/uf/{fechaString}")
            text = url.text
            datos = json.loads(text)
            for clave, valor in datos.items():
                if clave == 'serie':
                    print("El valor de la UF para el dia {} es de: {} CLP".format(fechaString,valor[0]['valor']))       
        pass

def consulta_IVP():
    url = requests.get("https://mindicador.cl/api/ivp")
    text = url.text
    datos = json.loads(text)
    for clave, valor in datos.items():
        if clave == 'serie':
            print("El valor del IVP es: {} CLP".format(valor[0]['valor']))

def consulta_IPC():
    url = requests.get("https://mindicador.cl/api/ipc")
    text = url.text
    datos = json.loads(text)
    for clave, valor in datos.items():
        if clave == 'serie':
            print("El valor del IPC es: {} CLP".format(valor[0]['valor']))

def consulta_UTM():
    url = requests.get("https://mindicador.cl/api/utm")
    text = url.text
    datos = json.loads(text)
    for clave, valor in datos.items():
        if clave == 'serie':
            print("El valor de la UTM es: {} CLP".format(valor[0]['valor']))

def consulta_USD():
    url = requests.get("https://mindicador.cl/api/dolar")
    text = url.text
    datos = json.loads(text)
    for clave, valor in datos.items():
        if clave == 'serie':
            print("El valor del dolar es: {} CLP".format(valor[0]['valor']))

def consulta_EUR():
    url = requests.get("https://mindicador.cl/api/euro")
    text = url.text
    datos = json.loads(text)
    for clave, valor in datos.items():
        if clave == 'serie':
            print("El valor del euro de hoy es: {} CLP".format(valor[0]['valor']))


