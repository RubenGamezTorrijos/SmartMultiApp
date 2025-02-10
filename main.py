import streamlit as st

# Importa las aplicaciones individuales
from apps import app1, app2  # Añade más importaciones según el número de aplicaciones

# Configuración inicial de Streamlit
st.set_page_config(page_title="Multi-App Example", layout="wide")

# Sidebar: Menú desplegable para seleccionar la aplicación
def main():
    st.sidebar.title("Menú de Aplicaciones")
    
    # Lista de aplicaciones disponibles
    apps = {
        "App 1": app1,
        "App 2": app2,
        # Agrega más aplicaciones aquí
    }
    
    # Selecciona la aplicación actual desde el estado de sesión
    selected_app = st.sidebar.selectbox("Selecciona una aplicación:", list(apps.keys()))
    
    # Almacena la selección en el estado de sesión para mantenerla persistente
    if "selected_app" not in st.session_state:
        st.session_state.selected_app = selected_app
    if selected_app != st.session_state.selected_app:
        st.session_state.selected_app = selected_app
    
    # Muestra el contenido de la aplicación seleccionada
    apps[st.session_state.selected_app].main()

if __name__ == "__main__":
    main()
