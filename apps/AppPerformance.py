import streamlit as st
import requests
import time

def main():
    st.title("Análisis de Rendimiento")
    url = st.text_input("Ingresa la URL del sitio:")
    if st.button("Analizar Rendimiento"):
        if not is_valid_url(url):
            st.error("La URL no es válida.")
        else:
            try:
                start_time = time.time()
                response = requests.get(url, timeout=10)
                end_time = time.time()
                load_time = end_time - start_time
                
                # Mostrar resultados
                st.write(f"Tiempo de carga: {load_time:.2f} segundos")
                st.write(f"Tamaño de la página: {len(response.content)} bytes")
            except Exception as e:
                st.error(f"Error al analizar rendimiento: {str(e)}")