#IMPORTAMOS LAS LIBRERÍAS NECESARIAS PARA EL ANÁLISIS DE DATOS, VISUALIZACIÓN Y APLICACIÓN DE STREAMLIT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from PIL import Image
import urllib.request
import json
import os
import ssl


#CARGAMOS EL DATASET
df = pd.read_csv('car_price.csv')

# Configuración de la página
st.set_page_config(page_title="Opticar - Soluciones Rentables", layout="wide")

# Cargar el banner desde la carpeta del proyecto
banner = Image.open("banner_opticar.jpg")

# Mostrar el banner en la parte superior de la aplicación
st.image(banner, use_column_width=True)

# Aplicar estilos personalizados al menú lateral
st.markdown("""
    <style>
        /* Fondo del menú lateral */
        [data-testid="stSidebar"] {
            background-color: #CD9C5C !important;
        }

        /* Texto del menú lateral */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Títulos en negrita */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            font-weight: bold;
        }

        /* Alinear mejor el contenido */
        [data-testid="stSidebarContent"] {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Configuración del menú lateral
menu_lateral = st.sidebar.radio("Selecciona una opción:", 
    ["Introducción", "Visión General", "Segmentación de Ventas", "Tendencias del Mercado", "Modelo predictivo","Conclusiones"]
)

# SOLO SE MUESTRA LA INTRODUCCIÓN CUANDO SE SELECCIONA "Introducción"
if menu_lateral == "Introducción":
    st.markdown('<h3 style="color: #A1753F; font-family: Cambria;">Nuestro objetivo</h3>', unsafe_allow_html=True)
    st.write(
        "Nuestro objetivo es proporcionar herramientas innovadoras basadas en datos "
        "que permitan a concesionarios y particulares maximizar el potencial económico "
        "de cada vehículo, impulsando decisiones más estratégicas y rentables."
    )

    st.write("""
    El presente informe tiene como finalidad asesorar a AutoMaster Select, un concesionario especializado en la venta 
    de vehículos de segunda mano, en la segmentación estratégica de sus ventas. Para ello, se ha llevado a cabo un 
    análisis exhaustivo de datos obtenidos mediante técnicas de web scraping.

    A través de este estudio, buscamos proporcionar a AutoMaster Select una visión clara y basada en datos que le
    permita optimizar su estrategia comercial, mejorar la rentabilidad y potenciar su posicionamiento competitivo en el 
    sector. Se presentarán hallazgos clave que permitirán definir segmentos de clientes, ajustar estrategias de precios 
    y maximizar el retorno de inversión en el inventario de vehículos.

    Este análisis será una herramienta fundamental para la toma de decisiones informadas, permitiendo a la empresa 
    ajustar su oferta a la demanda real del mercado y garantizar una ventaja competitiva sostenible.
    """)

    # Descripción de las variables
    st.markdown('<h3 style="color: #A1753F; font-family: Cambria;">Descripción de las variables analizadas</h3>', unsafe_allow_html=True)
    st.markdown("""
    El dataset proporcionado por AutoMaster Select contiene información detallada sobre las características de los vehículos, 
    entre las cuales se encuentran:
    - <span style="color: #AF6926; font-family: Cambria;"><b>Marca</b></span>: Marca del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Modelo</b></span>: Modelo del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Año</b></span>: Año de fabricación del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Kilometraje</b></span>: Kilometraje del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Tipo de combustible</b></span>: Tipo de combustible utilizado por el vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Tipo de transmisión</b></span>: Tipo de transmisión del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Potencia</b></span>: Potencia del vehículo en caballos de fuerza.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Precio</b></span>: Precio de venta del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Ubicación</b></span>: Ubicación del vehículo.
    """, unsafe_allow_html=True)

    st.write("""
    En el menú lateral se podrán visualizar diferentes secciones que contienen análisis detallados.""")

    st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
        <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
        con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
        documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
        limitado a los términos y condiciones acordados entre ambas partes.</i>
    </p>
""", unsafe_allow_html=True)


# VISIÓN GENERAL DE LOS DATOS
elif menu_lateral == "Visión General":
    st.markdown("## 📊 Visión General")
    st.write("Se realiza un análisis exploratorio de los datos para obtener una visión general de los datos obtenidos por la empresa.")

# SOLO SE MUESTRA SEGMENTACIÓN CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Segmentación de Ventas":
    st.markdown("## 📌 Segmentación de Ventas")
    st.write("Análisis detallado de la segmentación de clientes y ventas.")
    sub_option = st.sidebar.radio(
        "Selecciona una subcategoría:",
        ["Segmentación por comunidad autónoma", "Segmentación por marca", "Segmentación por potencia"]
    )
    if sub_option == "Segmentación por comunidad autónoma":
        st.write("🌍 **Análisis de ventas por comunidad autónoma**")
    elif sub_option == "Segmentación por marca":
        st.write("🚗 **Análisis de ventas por marca**")
    elif sub_option == "Segmentación por potencia":
        st.write("🏎️ **Análisis de ventas por potencia**")

# SOLO SE MUESTRA TENDENCIAS CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Tendencias del Mercado":
    st.markdown("## 📈 Tendencias del Mercado")
    st.write("Exploración de tendencias y patrones en el mercado automotriz.")

# SOLO SE MUESTRA CONCLUSIONES CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Conclusiones":
    st.markdown("## ✅ Conclusiones")
    st.write("Puntos clave y recomendaciones estratégicas.")

elif menu_lateral =="Modelo predictivo":

    #Variables de entrada para el modelo predictivo
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("## 📊 Modelo predictivo"
                )

    '''Para que la marca sea correlativa con el modelo a la hora de introducir el input en la aplicación, crearemos un diccionario en el que para cada marca
    introduzcamos los modelos que tiene. De esta forma, cuando el usuario introduzca una marca, podrá seleccionar el modelo correspondiente.'''
    makes_models_dict = (
    df.groupby("make")["model"]
      .unique()          # Devuelve los modelos únicos por marca
      .apply(list)       # Convierte el array de modelos en lista
      .to_dict() )        # Transforma el resultado en diccionario
    
    # Marcas de coches
    marca_seleccionada = st.selectbox("Selecciona la marca del vehículo", list(makes_models_dict.keys()))

    # Modelos de coches
    modelo_seleccionado = st.selectbox("Selecciona el modelo del vehículo", makes_models_dict[marca_seleccionada])

    #Tipo de combustible
    fuel = st.selectbox("Selecciona el tipo de combustible", df["fuel"].unique().tolist())

    # Año
    year = int(st.number_input("Introduce el año de fabricación", min_value=1967, max_value=2023, value=2000, step=1))

    # Kilometraje
    kms = int(st.number_input("Introduce el kilometraje", min_value=0, max_value=750000, value=20000, step=100))

    # Potencia
    power = int(st.number_input("Introduce la potencia en caballos de fuerza", min_value=5, max_value=999, value=100, step=20))
    
    # Transmisión
    transmission_dict = {"manual": "Manual", "automatic": "Automático"}
    transmission = st.selectbox("Selecciona el tipo de transmisión", [transmission_dict[t] for t in df["shift"].unique()])
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    #Inferencia del modelo
    if st.button("🔍 Predecir Precio del Vehículo"):

        def allowSelfSignedHttps(allowed):
        # bypass the server certificate verification on client side
            if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
                ssl._create_default_https_context = ssl._create_unverified_context


        allowSelfSignedHttps(True)  # Habilita certificados auto-firmados si es necesario

        # Datos en el formato requerido por la API
        data = {
            "Inputs": {
                "data": {
                    "make": [marca_seleccionada],
                    "model": [modelo_seleccionado],
                    "fuel": [fuel],
                    "year": [year],
                    "kms": [kms],
                    "power": [power],
                    "transmission": [transmission]
                }
            },
            "GlobalParameters": 1.0
        }

        body = str.encode(json.dumps(data))

        url = '' 
        api_key = ''  
        if not api_key:
            st.error("⚠️ No se ha proporcionado una clave API válida.")
        else:
            headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                result_json = json.loads(result)
                predicted_price = int(result_json["Results"][0])

                st.success(f"💰 Precio Estimado: **{predicted_price}€**")

            except urllib.error.HTTPError as error:
                st.error(f"⚠️ La solicitud falló con código de estado: {error.code}")
                st.text(error.info())
                st.text(error.read().decode("utf8", 'ignore'))

