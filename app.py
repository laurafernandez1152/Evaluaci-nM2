import pandas as pd
import streamlit as st
data= pd.read_csv('historico_resultados_pruebas_saber_11.csv')
data

# #limpieza
# data = data.dropna()

#esta por cuestiones de conflicto con los filtros


 #filtro 1
st.header("Filtro 1")
st.write ("Mostrar todos los puntajes de matematicas")
filtro1 = data["puntaje_matematicas"]
st.dataframe(filtro1)

# #filtro 2
st.header("Filtro 2")
st.write ("Mostrar todos los promedios de lenguaje")
filtro2 = data["puntaje_lectura"] 
st.dataframe(filtro2)

#filtro 3
def prom(ponderado_global):
    return ponderado_global < 250
st.header("Filtro 3")
st.write ("Mostrar todos los ponderados globales mayores a 17000")
filtro3 = data[(data["ponderado_global"] <17000)]
st.dataframe(filtro3)

#filtro 4
def prom(puntaje_naturales):
    return puntaje_naturales > 40
st.header("Filtro 4")
st.write ("Mostrar todos los puntajes de ciencias naturales mayores a 40")
filtro4 = data[(data["puntaje_naturales"] >40)]
st.dataframe(filtro4)

#filtro 5
def prom(puntaje_global):
    return puntaje_global < 170
st.header("Filtro 5")
st.write ("Mostrar todos los puntajes globales menores a 170")
filtro5 = data[(data["puntaje_global"] >170)]
st.dataframe(filtro5)
