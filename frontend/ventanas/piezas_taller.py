import tkinter as tk
from tkinter import ttk, messagebox
import requests
from frontend.utils import obtener_datos
from backend.models.tPiezas import TPiezas


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
        #self.label_tipos.grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.label_tipos.place(x=100, y=32)
        
        # Label Nombre
        self.label_nombre = tk.Label(self.master, text="Nombre")
        #self.label_nombre.grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.label_nombre.place(x=40, y=360)

        # Label Fabriacante
        self.label_fabricante = tk.Label(self.master, text="Fabricante")
        #self.label_fabricante.grid(column=0, row=0, padx=10, pady=10, sticky="e")
        self.label_fabricante.place(x=40, y=330)        

        # Listbox Materias
        self.listbox_tipos = tk.Listbox(self.master, width=30, height=7)
        #self.listbox_tipos.grid(column=1, row=0, padx=10, pady=10, sticky="w")
        self.listbox_tipos.place(x=200, y=40, height= 40)
        self.listbox_tipos.bind("<<ListboxSelect>>", self.mostrar_piezas)

        # Crear la Scrollbar: EN PROGRESO
        
        #scrollbar = tk.Scrollbar(self.master)
        #scrollbar.pack(side="right", fill="y")

        #Vinculamos scrollbar a la lista
        #self.listbox_tipos.config(yscrollcommand=scrollbar.set)
        #scrollbar.config(command=self.listbox_tipos.yview)
        
        # Treeview Piezas
        self.treeview_piezas = ttk.Treeview(self.master, columns=("id", "nombre", "fabricante", "id_tipo"), show="headings", height=9)
        #self.treeview_piezas.grid(row=1, columnspan=2, padx=40, pady=40, sticky="we")
        self.treeview_piezas.place(x=50, y=115, width= 500)
        self.treeview_piezas.bind("<<TreeviewSelect>>", self.mostrar_pieza_seleccionada)

        # Columnas treeview
        self.treeview_piezas.heading("id", text="ID")
        self.treeview_piezas.heading("nombre", text="NOMBRE")
        self.treeview_piezas.heading("fabricante", text="FABRICANTE")
        self.treeview_piezas.heading("id_tipo", text="ID_TIPO")
        self.treeview_piezas.column("id", width=50, anchor="center")
        self.treeview_piezas.column("nombre", stretch=True)
        self.treeview_piezas.column("fabricante", width=100, anchor="center")
        self.treeview_piezas.column("id_tipo", width=50, anchor="center")

        # Caja de texto correspondiente al nombre de la pieza
        self.nombre_pieza = tk.Entry(self.master)
        #self.nombre_pieza.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.nombre_pieza.place(x=110, y=330, width= 400)

        # Caja de texto correspondiente al nombre del fabricante
        self.fabricante_pieza = tk.Entry(self.master)
        #self.fabricante_pieza.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.fabricante_pieza.place(x=110, y=360, width= 400)

        # Botón Insertar
        self.insert_button = tk.Button(self.master, text="Insertar", command= self.addPieza)
        #self.insert_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        self.insert_button.place(x=90, y=410, width= 50)
        
        # Botón Borrar
        self.delete_button = tk.Button(self.master, text="Borrar")
        #self.delete_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        self.delete_button.place(x= 200, y=410, width= 50)


        # Botón Actualizar
        self.actualizar_button = tk.Button(self.master, text="Actualizar")
        #self.actualizar_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        self.actualizar_button.place(x= 310, y=410, width= 70)
        
        # Botón Salir
        self.salir_button = tk.Button(self.master, text="Salir", command= self.master.quit)
        #self.salir_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        self.salir_button.place(x= 420, y=410, width= 50)
        
        # Botón Limpiar
        self.salir_button = tk.Button(self.master, text="Limpiar", command= self.limpiar_seleccion)
        #self.salir_button.grid(row=3, column=0, padx=40, pady=40, sticky="ew")
        self.salir_button.place(x= 510, y=410, width= 50)        
        
    
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

    def mostrar_pieza_seleccionada(self, event):
        # Si hay un elemento seleccionado, mostramos su información
        item_id = self.treeview_piezas.focus()
        if item_id != "":
          valores = self.treeview_piezas.item(item_id, "values")          
          self.nombre_pieza.delete(0, 'end')
          self.nombre_pieza.insert(0, valores[2])
          self.fabricante_pieza.delete(0, 'end')
          self.fabricante_pieza.insert(0, valores[1])

    def limpiar_seleccion(self):        
        self.treeview_piezas.selection_remove(self.treeview_piezas.selection())       
        self.nombre_pieza.delete(0, 'end')
        self.fabricante_pieza.delete(0, 'end')
    
    #Función para añadir pieza a la base de datos

    def addPieza(self):
     
     nombre = self.nombre_pieza.get()
     fabricante = self.fabricante_pieza.get()

     url = "http://127.0.0.1:5000/piezas"
     data = {"nombre": nombre, "fabricante": fabricante}
     try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            self.mostrar_piezas()
        else:
            messagebox.showerror("Error", response.json().get("message", "Error desconocido"))
     except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"No se puedo conectar al servidor: {e}")





            
