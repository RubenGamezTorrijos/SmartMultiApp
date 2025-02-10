import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title("Auditoría SEO")
    url = st.text_input("Ingresa la URL del sitio:")
    if st.button("Analizar SEO"):
        if not is_valid_url(url):
            st.error("La URL no es válida.")
        else:
            try:
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.content, "html.parser")
                
                # Extraer título
                title = soup.title.string.strip() if soup.title else "Sin título"
                
                # Extraer descripción meta
                meta_description = soup.find("meta", attrs={"name": "description"})
                description = meta_description["content"].strip() if meta_description else "Sin descripción"
                
                # Mostrar resultados
                st.write(f"Título: {title}")
                st.write(f"Descripción Meta: {description}")
            except Exception as e:
                st.error(f"Error al analizar SEO: {str(e)}")