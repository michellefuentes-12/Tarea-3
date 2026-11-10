import os
import mysql.connector
import streamlit as st

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host=os.environ["MYSQL_HOST"],
            port=int(os.environ.get("MYSQL_PORT", 3306)),
            user=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            database=os.environ["MYSQL_DATABASE"]
        )
        return conexion
    except KeyError as error:
        st.error(f"Falta la variable de entorno: {error}")
        return None
    except mysql.connector.Error as error:
        st.error(f"Error al conectar con la base de datos: {error}")
        return None
