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

# Función para obtener información Whois
def get_whois(domain):
    try:
        w = whois.whois(domain)
        if w.domain_name is None:  # Comprobar si se obtuvo información válida
            return "No se encontró información Whois para este dominio."
        return w
    except Exception as e:
        return f"Error al obtener información Whois: {str(e)}"

def main():
    st.title("Análisis Básico")
    url = st.text_input("Ingresa la URL del sitio:")
    if st.button("Analizar"):
        if not is_valid_url(url):
            st.error("La URL no es válida.")
        else:
            domain = url.split("//")[-1].split("/")[0]
            st.write(f"Analizando {domain}...")
            
            # Obtener dirección IP
            try:
                ip_address = socket.gethostbyname(domain)
            except Exception as e:
                ip_address = f"Error al obtener IP: {str(e)}"
            
            # Obtener información Whois
            whois_info = get_whois(domain)
            # Mostrar resultados
            st.write(f"Dirección IP: {ip_address}")
            st.write("Información Whois:")
            if isinstance(whois_info, str):  # Si hay un error
                st.write(whois_info)
            else:
                st.json(whois_info)