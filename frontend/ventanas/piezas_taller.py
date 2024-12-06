import tkinter as tk
from tkinter import ttk, messagebox
import requests
from frontend.utils import obtener_datos

class VentanaPiezasTaller:
    def __init__(self, master):
        self.master = master
        self.master.title("Piezas Taller")
        self.master.geometry("600x450")

        self.master.grid_columnconfigure(0, weight=1)  # Columna para Labels
        self.master.grid_columnconfigure(1, weight=1)  # Columna para Listboxes
        self.master.grid_rowconfigure(0, weight=1)  # Espaciado vertical
        self.master.grid_rowconfigure(1, weight=1)  # Espaciado vertical

        # Label Materias
        self.label_tipos = tk.Label(self.master, text="Materia")
        self.label_tipos.grid(column=0, row=0, padx=10, pady=10, sticky="e")
        
        # Listbox Materias
        self.listbox_tipos = tk.Listbox(self.master, width=30, height=7)
        self.listbox_tipos.grid(column=1, row=0, padx=10, pady=10, sticky="w")
        self.listbox_tipos.bind("<<ListboxSelect>>", self.mostrar_piezas)
        
        # Treeview Piezas
        self.treeview_piezas = ttk.Treeview(self.master, columns=("id", "nombre", "fabricante", "id_tipo"), show="headings", height=9)
        self.treeview_piezas.grid(row=1, columnspan=2, padx=40, pady=40, sticky="we")

        # Columnas treeview
        self.treeview_piezas.heading("id", text="ID")
        self.treeview_piezas.heading("nombre", text="NOMBRE")
        self.treeview_piezas.heading("fabricante", text="FABRICANTE")
        self.treeview_piezas.heading("id_tipo", text="ID_TIPO")
        self.treeview_piezas.column("id", width=50, anchor="center")
        self.treeview_piezas.column("nombre", stretch=True)
        self.treeview_piezas.column("fabricante", width=100, anchor="center")
        self.treeview_piezas.column("id_tipo", width=50, anchor="center")

        # Cargar los tipos de piezas
        self.cargar_tipos_piezas()

    def cargar_tipos_piezas(self):
        # Obtener tipos de piezas desde la API
        url = "http://127.0.0.1:5000/id_tipo"  # Endpoint para obtener tipos de piezas
        try:
            response = requests.get(url)
            if response.status_code == 200:
                tipos = response.json()
                self.tipos_dict = {}
                for tipo in tipos:
                    self.listbox_tipos.insert(tk.END, tipo["Nombre"])
                    self.tipos_dict[tipo["Nombre"]] = tipo["Id_tipo"]
            else:
                tk.messagebox.showerror("Error", "No se pudieron cargar los tipos de piezas.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")

    def mostrar_piezas(self, event):
        # Limpiar el Treeview
        for item in self.treeview_piezas.get_children():
            self.treeview_piezas.delete(item)
        
        # Obtener el tipo seleccionado
        seleccion = self.listbox_tipos.curselection()
        if not seleccion:
            return

        nombre_seleccionado = self.listbox_tipos.get(seleccion[0])
        tipo_seleccionado = self.tipos_dict.get(nombre_seleccionado)
        print(tipo_seleccionado)
        
        # Obtener piezas del tipo seleccionado desde la API
        url = f"http://127.0.0.1:5000/piezas/{tipo_seleccionado}"  # Ajusta el endpoint según tu backend
        try:
            response = requests.get(url)
            if response.status_code == 200:
                piezas = response.json()
                for pieza in piezas:
                    # Agregar cada pieza como una fila en el Treeview
                    self.treeview_piezas.insert("", tk.END, values=(pieza["id"], pieza["nombre"], pieza["fabricante"], pieza["id_tipo"]))
            else:
                messagebox.showerror("Error", f"No se pudieron cargar piezas para el tipo {tipo_seleccionado}.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")