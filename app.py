import streamlit as st
import pandas as pd
import plotly_express as plt

car_data = pd.read_csv(r"C:\Users\USUARIO\Desktop\ESCRITORIO\CURSO DE TRIPLETEN\PROYECTO PYTHON SPRINT 6\PROJECT6\vehicles_us.csv")

st.header("Proyecto 6 - Sprint 6")

casilla1 = st.checkbox("Dibujar Histograma")

if casilla1:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = plt.histogram(car_data, x="odometer")
    st.plotly_chart(fig,use_container_width=True)

casilla2 = st.checkbox("Dibujar grafico de dispersion")

if casilla2:
    st.write("Grafico de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig2 = plt.scatter(car_data,x="odometer")
    st.plotly_chart(fig2,use_container_width=True)
