# **Análisis de vehículos de segunda mano**
 ![opticar_logo](https://github.com/user-attachments/assets/120fa3c1-ab43-467b-a088-d1d483f10acd)

 ## ***Resumen***
En este proyecto, asumimos el rol de **Opticar**, una empresa ficticia especializada en **análisis de datos y asesoramiento estratégico** para el sector automotriz. Nuestro cliente, **Automaster Select**, nos ha proporcionado un conjunto de datos de **vehículos de segunda mano**, obtenido mediante **web scraping**, con el objetivo de analizar el mercado y optimizar su estrategia de precios.

Para ello, hemos llevado a cabo un **preprocesamiento exhaustivo de los datos**, corrigiendo valores nulos y realizando otras transformaciones en el notebook de *preprocesamiento*. Posteriormente, realizamos un **análisis exploratorio de datos (EDA)** en el notebook *EDA_car_price*, extrayendo diferentes **insights**.

Además, desarrollamos una aplicación interactiva en **Streamlit** (*car_price.py*) para la presentación de resultados de forma accesible y visual. Complementariamente, diseñamos dos **dashboards en Power BI**, proporcionando **visualizaciones dinámicas** para mejorar la toma de decisiones. Finalmente, implementamos un **modelo predictivo** de regresión para **estimar el precio** de los vehículos, desplegado en un servidor en la nube mediante **Azure Machine Learning**, garantizando accesibilidad y escalabilidad.

Este proyecto combina técnicas avanzadas de ciencia de datos, desarrollo web y visualización de información, ofreciendo a Automaster Select una solución integral basada en datos para optimizar su negocio. 


## ***Contenido de la aplicación de streamlit***
En la aplicación de streamlit se podrán visualizar los siguientes apartados:
* *Introducción*: breve introducción de quién somos y cual es nuestro objetivo.
* *Visión General*: visión general de los datos obtenidos sobre los que hemos realizado el estudio.
* *Tendencia de mercado*: Se analiza la tendencia del mercado de segunda mano, enfocándonos en las siguientes características: marcas, potencia, kilometraje y geografía.
* *Modelo predictivo*: se realiza mediante la plataforma azure un modelo predictivo con la finalidad de que la empresa pueda predecir el precio de un vehículo que desee poner a la venta en base a las características de: marca, modelo, tipo de combustible, año de fabricación, kilometraje, potencia y tipo de transmisión.
* *Panel de control | PowerBI*: se realiza un panel de control en powerBI en el que se ven como afectan las distintas características a los precios de los coches y un buscador de vehículos en base a las necesidades del cliente.
* *Conclusiones*: se detallan las conclusiones encontradas durante el análisis.

## ***Herramientas utilizadas***
Se ha utilizado el lenguaje de programación ***Python*** con las siguientes librerías:
* *Pandas*
* Herramientas de visualización de datos: *Matplotlib, Seaborn, PlotlyExpress*.
* *Streamlit*
Se ha utilizado la siguiente herramienta de visualización de datos:
* *PowerBI*
Se ha utilizado la siguiente plataforma para el desarrollo del modelo predictivo:
* *Azure Machine Learning*
