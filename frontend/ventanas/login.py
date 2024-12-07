import tkinter as tk
from tkinter import messagebox
import requests
from frontend.ventanas.piezas_taller import VentanaPiezasTaller  # Aquí se importa la ventana de piezas

class VentanaLogin:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        
        self.master.geometry("400x300")

        self.master.grid_columnconfigure(0, weight=1, minsize=100)
        self.master.grid_columnconfigure(1, weight=2, minsize=100)
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)

        #Label Welcome
        self.welcome_label = tk.Label(self.master, text = "Welcome", font = ("Arial", 24))
        self.welcome_label.grid(row=0, column=0, columnspan=2, padx=10, pady=20)

        # Label User
        self.user_label = tk.Label(self.master, text="User:")
        self.user_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        # Entry User
        self.user_entry = tk.Entry(self.master)
        self.user_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        
        # Label Password
        self.pass_label = tk.Label(self.master, text="Password:")
        self.pass_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        
        # Entry Password
        self.pass_entry = tk.Entry(self.master, show="*")
        self.pass_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)   

        # Button OK
        self.ok_button = tk.Button(self.master, text="OK", command=self.iniciar_sesion)
        self.ok_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        
        # Button Cancel
        self.cancel_button = tk.Button(self.master, text="Cancel", command=self.master.quit)
        self.cancel_button.grid(row=3, column=1, padx=40, pady=40, sticky="ew")

    def iniciar_login(self):
        # Este método solo está llamando a la lógica del login
        self.master.mainloop()

    def iniciar_sesion(self):
        # Lógica de validacion del login
        usuario = self.user_entry.get()
        password = self.pass_entry.get()

        url = "http://127.0.0.1:5000/login"
        data = {"usuario": usuario, "password": password, "pantalla": "PIEZAS"}
        
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
<<<<<<< Updated upstream
                self.usuario= usuario #Guardamos nombre del usuario en esta sesion
=======
                permisos = response.json()
>>>>>>> Stashed changes
                self.master.destroy()
                self.abrir_ventana_piezas(permisos)
                self.master.quit()
            else:
                messagebox.showerror("Error", response.json().get("message", "Error desconocido"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se puedo conectar al servidor: {e}")

    def abrir_ventana_piezas(self, permisos):
        # Esta función maneja la creación de la ventana de piezas
        root_piezas = tk.Tk()  # Crear nueva ventana
<<<<<<< Updated upstream
        VentanaPiezasTaller(root_piezas, self.usuario)  # Crear la instancia de la ventana de piezas
=======
        VentanaPiezasTaller(root_piezas, permisos)  # Pasar permisos a la ventana de piezas
>>>>>>> Stashed changes
        root_piezas.mainloop()  # Ejecutar la ventana de piezas