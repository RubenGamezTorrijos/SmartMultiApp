import streamlit as st
from streamlit.components.v1 import html

# Configuración del menú lateral
st.set_page_config(page_title="Multi-App Streamlit", layout="wide")

# Lista de aplicaciones disponibles
APPS = {
    "Inicio": "index",
    "Análisis Básico": "apps.AppBasicAnalysis",
    "Seguridad": "apps.AppSecurity",
    "SEO": "apps.AppSEO",
    "Rendimiento": "apps.AppPerformance",
}

# Guardar la selección del usuario en el cache
if "selected_app" not in st.session_state:
    st.session_state.selected_app = "index"

# Menú lateral
st.sidebar.title("Menú Aplicaciones")
selected_app = st.sidebar.radio(
    "Seleccione una aplicación",
    list(APPS.keys()),
    index=list(APPS.keys()).index(st.session_state.selected_app),
    key="app_selector"
)

# Cargar la aplicación seleccionada
if selected_app != "Inicio":
    st.session_state.selected_app = selected_app
    app_path = APPS[selected_app]
    if app_path == "apps.AppBasicAnalytics":
        from apps.AppBasicAnalytics import main as app_main
    elif app_path == "apps.AppSEO":
        from apps.AppSEO import main as app_main
    elif app_path == "apps.AppSecurity":
        from apps.AppSecurity import main as app_main
    elif app_path == "apps.AppPerformance":
        from apps.AppPerformance import main as app_main
    app_main()
else:
    st.title("Multi-App Streamlit")
    st.write("Seleccione una aplicación del menú lateral para comenzar.")