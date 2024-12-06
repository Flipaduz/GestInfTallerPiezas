
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Crear widgets
label = tk.Label(ventana, text="Este es un label")
entry = tk.Entry(ventana)
button = tk.Button(ventana, text="Aceptar")

# Posicionar los widgets con grid
label.grid(row=3, column=4)
entry.grid(row=1, column=0)
button.grid(row=2, column=0)

# Ejecutar la ventana
ventana.mainloop()