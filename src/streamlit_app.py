# streamlit run streamlit_app.py

import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Hello, Streamlit!")

# Texto de bienvenida
st.write("¡Hola, Mundo! Bienvenido a tu primera aplicación con Streamlit.")

# Entrada de texto
nombre = st.text_input("Escribe tu nombre:")

# Botón para mostrar saludo personalizado
if st.button("Saludar"):
    st.write(f"Hola, {nombre}!")

# Checkbox para mostrar un mensaje adicional
if st.checkbox("Mostrar mensaje adicional"):
    st.write("¡Streamlit es muy fácil de usar!")

# Crear un DataFrame ficticio
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Edad': [25, 30, 35, 40],
    'Ciudad': ['Lima', 'Arequipa', 'Cusco', 'Trujillo']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame en la aplicación
st.write("Aquí tienes un DataFrame con datos ficticios:")
st.dataframe(df)