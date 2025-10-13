# SQL connection configuration

import mysql.connector

def conectar_db():
    return mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="backend_proyecto")


