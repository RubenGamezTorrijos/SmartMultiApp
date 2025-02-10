import streamlit as st
import requests
from bs4 import BeautifulSoup
import whois
import socket
import time

# Función para validar la URL
def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    st.title("Análisis de Seguridad")
    url = st.text_input("Ingresa la URL del sitio:")
    if st.button("Analizar Seguridad"):
        if not is_valid_url(url):
            st.error("La URL no es válida.")
        else:
            try:
                response = requests.get(url, timeout=5)
                headers = response.headers
                
                # Convertir cabeceras HTTP a un diccionario serializable
                serializable_headers = {key: str(value) for key, value in headers.items()}
                
                # Verificar HTTPS
                is_https = url.startswith("https://")
                
                # Mostrar resultados
                st.write("Cabeceras HTTP:")
                st.json(serializable_headers)
                st.write(f"¿Usa HTTPS?: {'Sí' if is_https else 'No'}")
            except Exception as e:
                st.error(f"Error al analizar seguridad: {str(e)}")

                import streamlit as st
import requests
from bs4 import BeautifulSoup
import whois
import socket
from utils.common_functions import is_valid_url, get_whois

# Modelo (Model)
class SecurityModel:
    def __init__(self, url):
        self.url = url
        self.headers = {}
        self.is_https = False

    def fetch_data(self):
        try:
            response = requests.get(self.url, timeout=5)
            self.headers = {key: str(value) for key, value in response.headers.items()}
            self.is_https = self.url.startswith("https://")
        except Exception as e:
            return f"Error al analizar seguridad: {str(e)}"

# Vista (View)
def view(model):
    st.title("Análisis de Seguridad")

    st.write("Cabeceras HTTP:")
    st.json(model.headers)
    st.write(f"¿Usa HTTPS?: {'Sí' if model.is_https else 'No'}")

# Controlador (Controller)
def controller():
    url = st.text_input("Ingresa la URL del sitio:")
    if st.button("Analizar Seguridad"):
        if not is_valid_url(url):
            st.error("La URL no es válida.")
        else:
            model = SecurityModel(url)
            error = model.fetch_data()
            if error:
                st.error(error)
            else:
                view(model)