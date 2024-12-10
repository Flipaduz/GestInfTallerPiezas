import tkinter as tk
from tkinter import ttk, messagebox
import requests
from frontend.utils import obtener_datos
from backend.models.tPiezas import TPiezas


class VentanaPiezasTaller:
    def __init__(self, master, permisos):
        self.master = master
        self.permisos = permisos

        self.master.title("Piezas Taller")
        self.master.geometry("800x600")  # Ventana más grande

        # Label Materias
        self.label_tipos = tk.Label(self.master, text="Materia")
        self.label_tipos.place(x=200, y=40)

        # Listbox Materias
        self.listbox_tipos = tk.Listbox(self.master, width=40, height=10)
        self.listbox_tipos.place(x=300, y=40, height=150)
        #Selecciono el elemento, llamo seleccion_listbox
        self.listbox_tipos.bind("<<ListboxSelect>>", self.seleccion_listbox)

        # Treeview Piezas
        self.treeview_piezas = ttk.Treeview(self.master, columns=("id", "nombre", "fabricante", "id_tipo"), show="headings", height=10)
        self.treeview_piezas.place(x=50, y=220, width=700)
        #Selecciono el elemento del Treeview se llama seleccion_treeview
        self.treeview_piezas.bind("<<TreeviewSelect>>", self.seleccion_treeview)

        # Columnas treeview

        #Creamos columnas con sus nombres
        self.treeview_piezas.heading("id", text="ID")
        self.treeview_piezas.heading("nombre", text="NOMBRE")
        self.treeview_piezas.heading("fabricante", text="FABRICANTE")
        self.treeview_piezas.heading("id_tipo", text="ID_TIPO")

        #Configuramos coolumnas
        self.treeview_piezas.column("id", width=50, anchor="center")
        self.treeview_piezas.column("nombre", stretch=True)  #Que se extire la columna de nombre
        self.treeview_piezas.column("fabricante", width=150, anchor="center")
        self.treeview_piezas.column("id_tipo", width=50, anchor="center")

        #Strings que se asocian a las cajas del texto (nombre y fabricante)
        self.nombre_var = tk.StringVar()     
        self.fabricante_var = tk.StringVar() 

        # Label Nombre
        self.label_nombre = tk.Label(self.master, text="Nombre")
        self.label_nombre.place(x=40, y=460)

        # Label Fabricante
        self.label_fabricante = tk.Label(self.master, text="Fabricante")
        self.label_fabricante.place(x=40, y=500)

        # Caja de texto correspondiente al nombre de la pieza
        self.entry_nombre = tk.Entry(self.master, textvariable=self.fabricante_var)
        self.entry_nombre.place(x=110, y=460, width=600)

        # Caja de texto correspondiente al nombre del fabricante
        self.entry_fabricante = tk.Entry(self.master, textvariable=self.nombre_var)
        self.entry_fabricante.place(x=110, y=500, width=600)

        if not self.permisos.get("modificacion"):
            self.entry_nombre.config(state="readonly")
            self.entry_fabricante.config(state="readonly")

        # Botón Insertar
        self.insert_button = tk.Button(self.master, text="Insertar", command=self.insertar_pieza)
        self.insert_button.place(x=90, y=550, width=70)

        # Botón Borrar
        self.delete_button = tk.Button(self.master, text="Borrar", command=self.borrar_pieza)
        self.delete_button.place(x=230, y=550, width=70)

        # Botón Actualizar
        self.actualizar_button = tk.Button(self.master, text="Actualizar", command=self.actualizar_pieza)
        self.actualizar_button.place(x=360, y=550, width=90)

        # Botón Salir
        self.salir_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.salir_button.place(x=520, y=550, width=70)

        # Botón Limpiar
        self.limpiar_button = tk.Button(self.master, text="Limpiar", command=self.limpiar_seleccion)
        self.limpiar_button.place(x=650, y=550, width=70)

        self.cargar_tipos_piezas()
        self.configurar_botones()



    def bloquear_seleccion(self, event):
        return "break"



    def configurar_botones(self):
        if not self.permisos.get("modificacion"):
            self.insert_button.config(state="disabled")
            self.delete_button.config(state="disabled")
            self.actualizar_button.config(state="disabled")
        else:
            self.insert_button.config(state="normal")
            self.delete_button.config(state="normal")
            self.actualizar_button.config(state="normal")



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
                if not self.permisos.get("acceso"):
                    self.listbox_tipos.config(state="disabled")
            else:
                tk.messagebox.showerror("Error", "No se pudieron cargar los tipos de piezas.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo conectar al servidor: {e}")



    def seleccion_listbox(self, event):
        self.mostrar_piezas()



    def mostrar_piezas(self):
        # Limpiar el Treeview
        self.limpiar_seleccion()
        for item in self.treeview_piezas.get_children():
            self.treeview_piezas.delete(item)
        # Obtener el tipo seleccionado
        seleccion = self.listbox_tipos.curselection()
        if not seleccion:
            return
        nombre_seleccionado = self.listbox_tipos.get(seleccion[0])
        tipo_seleccionado = self.tipos_dict.get(nombre_seleccionado)
        # Obtener piezas del tipo seleccionado desde la API
        url = f"http://127.0.0.1:5000/piezas/{tipo_seleccionado}"
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



    def seleccion_treeview(self, event):
        self.mostrar_pieza_seleccionada()



    def mostrar_pieza_seleccionada(self):
        # Si hay un elemento seleccionado, mostramos su información
        item_id = self.treeview_piezas.focus()
        if item_id != "":
            valores = self.treeview_piezas.item(item_id, "values")
            self.nombre_var.set(valores[2])
            self.fabricante_var.set(valores[1])



    def limpiar_seleccion(self):        
        # Limpiar selección del Treeview
        self.treeview_piezas.selection_remove(self.treeview_piezas.selection())
        self.treeview_piezas.focus("")
        # Limpiar los Textboxes
        self.nombre_var.set("")
        self.fabricante_var.set("")



    #Función para añadir pieza a la base de datos
    def insertar_pieza(self):
        nombre = self.entry_nombre.get()
        fabricante = self.entry_fabricante.get()
        # Verificar si se seleccionó un tipo de pieza
        seleccion = self.listbox_tipos.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un tipo de pieza.")
            return
        # Acceder a la API e insertar la nueva pieza
        url = "http://127.0.0.1:5000/piezas/insertar"
        data = {"nombre": nombre, "fabricante": fabricante, "id_tipo": self.tipos_dict.get(self.listbox_tipos.get(seleccion[0]))}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                self.limpiar_seleccion()
                self.mostrar_piezas()
            else:
                messagebox.showerror("Error", response.json().get("message", "Error desconocido"))
        except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"No se puedo conectar al servidor: {e}")



    # Funcion para actualizar los datos de una pieza ya existente
    def actualizar_pieza(self):
        # Verificar si se selecciono un tipo de pieza
        seleccion = self.listbox_tipos.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un tipo de pieza.")
            return
        # Obtener el id de la pieza a actualizar y los nuevos datos (nombre y fabricante)
        item_id = self.treeview_piezas.focus()
        if item_id != "":
            valores = self.treeview_piezas.item(item_id, "values")
            id = valores[0]
            nombre = self.entry_nombre.get()
            fabricante = self.entry_fabricante.get()
            # Acceder a la API y actualizar la pieza
            url = f"http://127.0.0.1:5000/piezas/actualizar/{id}"
            data = {"nombre": nombre, "fabricante": fabricante}
            try:
                response = requests.put(url, json=data)
                if response.status_code == 201:
                    self.limpiar_seleccion()
                    self.mostrar_piezas()
                else:
                    messagebox.showerror("Error", response.json().get("message", "Error desconocido"))
            except requests.exceptions.RequestException as e:
                    messagebox.showerror("Error", f"No se puedo conectar al servidor: {e}")



    # Funcion para borrar una pieza de la base de datos
    def borrar_pieza(self):
        # Verificar si se selecciono un tipo de pieza
        seleccion = self.listbox_tipos.curselection()
        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un tipo de pieza.")
            return
        # Obtener el id de la pieza que se quiere borrar
        item_id = self.treeview_piezas.focus()
        if item_id != "":
            valores = self.treeview_piezas.item(item_id, "values")
            id = valores[0]
            # Acceder a la API y borrar la pieza
            url = f"http://127.0.0.1:5000/piezas/borrar/{id}"
            try:
                response = requests.delete(url)
                if response.status_code == 201:
                    self.limpiar_seleccion()
                    self.mostrar_piezas()
                else:
                    messagebox.showerror("Error", response.json().get("message", "Error desconocido"))
            except requests.exceptions.RequestException as e:
                    messagebox.showerror("Error", f"No se puedo conectar al servidor: {e}")