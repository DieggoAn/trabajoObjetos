# SQL connection configuration y datos de prueba

import mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root",passwd="",database="backend_proyecto")

cursor1 = conexion1.cursor()

# Sentencia SQL
sql = "INSERT INTO Departamento (id_departamento, nombre) VALUES (%s, %s)"

# Datos de ejemplo
# Lista de tuplas con varios departamentos
datos = [
    ("DEP01", "Recursos Humanos"),
    ("DEP02", "Finanzas"),
    ("DEP03", "TI"),
    ("DEP04", "Marketing")
]

# Ejecutar todos de una vez
cursor1.executemany(sql, datos)

# Ejecución
conexion1.commit()
conexion1.close()
