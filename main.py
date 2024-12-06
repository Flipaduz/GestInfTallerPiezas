from tkinter import Tk
from frontend.ventanas.login import VentanaLogin

def iniciar_app():
    # Crear la ventana principal
    root = Tk()
    
    # Iniciar la ventana de login
    login = VentanaLogin(root)
    
    # Ejecutar la ventana de login y esperar si es correcto
    login.iniciar_login()  # El flujo de la ventana de login se maneja desde aquí

# Iniciar la aplicación
iniciar_app()