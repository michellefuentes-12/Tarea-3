import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Gestión de Almacén", layout="wide")
st.title("Sistema de Control - Almacén")

# 1. Obtener credenciales de las variables de entorno de Render
db_host = os.getenv("MYSQL_HOST")
db_user = os.getenv("MYSQL_USER")
db_password = os.getenv("MYSQL_PASSWORD")
db_name = os.getenv("MYSQL_DATABASE")
db_port = os.getenv("MYSQL_PORT", "3306")

# 2. Crear conexión a la base de datos MySQL en Clever Cloud
@st.cache_resource
def get_db_engine():
    connection_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    return create_engine(connection_url)

# 3. Consultar y mostrar los datos
try:
    engine = get_db_engine()
    
    # Consulta SQL a la tabla Almacén
    query = "SELECT * FROM Almacén;"
    df = pd.read_sql(query, con=engine)
    
    st.success("¡Conexión exitosa a la base de datos en Clever Cloud!")
    st.subheader("Registros en la tabla Almacén")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error("Error al conectar con la base de datos MySQL.")
    st.exception(e)
