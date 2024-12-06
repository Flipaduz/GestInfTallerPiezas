import tkinter as tk
from frontend.utils import obtener_datos

class VentanaPiezas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Piezas")
        btn = tk.Button(root, text="Cargar Piezas", command=self.cargar_piezas)
        btn.pack()

    def cargar_piezas(self):
        piezas = obtener_datos("/piezas")
        print(piezas)