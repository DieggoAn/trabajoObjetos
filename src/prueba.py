from controllers.functions import *
from controllers.menus import menu_gestion_emp
from models.Administrador import *
from models.Gerente import *
from controllers.menu_admin import * 
from controllers.functions_informe import *

nombres_ejemplo = "Ana María"
apellido_paterno_ejemplo = "Tapia"
apellido_materno_ejemplo = "Rojas"
direccion_ejemplo = "Calle Falsa 123"
fecha_nacimiento_ejemplo = "1990-11-25"
fecha_inicio_contrato_ejemplo = "2023-03-01"
salario_ejemplo = 1800000
telefono_ejemplo = "912345678"
rut_ejemplo = "15444333-2"
estadoSesion_ejemplo = False
id_departamento_ejemplo = 1
"""
# Instanciar la clase Administrador
nuevo_administrador = Administrador(
    nombres=nombres_ejemplo,
    apellido_paterno=apellido_paterno_ejemplo,
    apellido_materno=apellido_materno_ejemplo,
    direccion=direccion_ejemplo,
    fecha_nacimiento=fecha_nacimiento_ejemplo,
    fecha_inicio_contrato=fecha_inicio_contrato_ejemplo,
    salario=salario_ejemplo,
    telefono=telefono_ejemplo,
    rut_administrador=rut_ejemplo,
    estadoSesion=estadoSesion_ejemplo,
    id_departamento=id_departamento_ejemplo
)

nombres_ejemplo = "Carlos"
apellido_paterno_ejemplo = "Muñoz"
apellido_materno_ejemplo = "Soto"
direccion_ejemplo = "Av. Principal 456, Santiago"
fecha_nacimiento_ejemplo = "1975-08-10"
fecha_inicio_contrato_ejemplo = "2018-06-01"
salario_ejemplo = 3500000.00
telefono_ejemplo = "998765432"
rut_ejemplo = "10222333-4"
id_departamento_ejemplo = 5 # Gerencia General

# Instanciar la clase Gerente
nuevo_gerente = Gerente(
    nombres=nombres_ejemplo,
    apellido_paterno=apellido_paterno_ejemplo,
    apellido_materno=apellido_materno_ejemplo,
    direccion=direccion_ejemplo,
    fecha_nacimiento=fecha_nacimiento_ejemplo,
    fecha_inicio_contrato=fecha_inicio_contrato_ejemplo,
    salario=salario_ejemplo,
    telefono=telefono_ejemplo,
    rut_gerente=rut_ejemplo,
    id_departamento=id_departamento_ejemplo
)
#menu_gestion_informe()
##menu_gestion_proyecto(nuevo_administrador, nuevo_gerente)

"""
#menu_gestion_emp(nuevo_administrador)
generarInforme()

