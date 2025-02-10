import requests
import whois
import socket
import time

def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def get_whois(domain):
    try:
        w = whois.whois(domain)
        if w.domain_name is None:  # Comprobar si se obtuvo información válida
            return "No se encontró información Whois para este dominio."
        return w
    except Exception as e:
        return f"Error al obtener información Whois: {str(e)}"