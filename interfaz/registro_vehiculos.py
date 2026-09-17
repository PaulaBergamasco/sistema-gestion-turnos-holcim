import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

def mostrar_registro_vehiculos(frame_contenido):

    titulo = tk.Label(
        frame_contenido,
        text="Registro de Vehículos",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=(30, 10))

    descripcion = tk.Label(
        frame_contenido,
        text="Cargue los datos para registrar un nuevo vehículo en el sistema",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 11)
    )
    descripcion.pack(pady=(0, 20))

    
    formulario = tk.LabelFrame(
        frame_contenido,
        text="Datos del vehículo",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=30,
        pady=20
    )
    formulario.pack(padx=50, fill="x")

   
    label_patente = tk.Label(
        formulario, text="Patente:", bg="#FFFFFF", font=("Arial", 11)
    )
    label_patente.grid(row=0, column=0, sticky="w", padx=10, pady=10)

    entrada_patente = tk.Entry(
        formulario, width=40, font=("Arial", 11), relief="groove", bg="#F5F5F5"
    )
    entrada_patente.grid(row=0, column=1, padx=10, pady=10)

    
    label_marca = tk.Label(
        formulario, text="Marca:", bg="#FFFFFF", font=("Arial", 11)
    )
    label_marca.grid(row=1, column=0, sticky="w", padx=10, pady=10)

    entrada_marca = tk.Entry(
        formulario, width=40, font=("Arial", 11), relief="groove", bg="#F5F5F5"
    )
    entrada_marca.grid(row=1, column=1, padx=10, pady=10)

    
    label_modelo = tk.Label(
        formulario, text="Modelo:", bg="#FFFFFF", font=("Arial", 11)
    )
    label_modelo.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    entrada_modelo = tk.Entry(
        formulario, width=40, font=("Arial", 11), relief="groove", bg="#F5F5F5"
    )
    entrada_modelo.grid(row=2, column=1, padx=10, pady=10)

    
    def guardar_vehiculo():
        patente = entrada_patente.get().strip().upper()
        marca = entrada_marca.get().strip()
        modelo = entrada_modelo.get().strip()

        if not patente or not marca or not modelo:
            messagebox.showwarning(
                "Campos Incompletos",
                "Por favor complete todos los datos del vehículo."
            )
            return

        tabla.insert("", "end", values=(patente, marca, modelo))
        limpiar_campos()
        messagebox.showinfo(
            "Éxito", f"Vehículo patente {patente} guardado correctamente."
        )

    def limpiar_campos():
        entrada_patente.delete(0, tk.END)
        entrada_marca.delete(0, tk.END)
        entrada_modelo.delete(0, tk.END)

    def eliminar_vehiculo():
        seleccion = tabla.selection()
        if not seleccion:
            messagebox.showwarning(
                "Atención",
                "Seleccione un vehículo de la lista para eliminar."
            )
            return

        if messagebox.askyesno(
            "Confirmar", "¿Desea eliminar el vehículo seleccionado?"
        ):
            tabla.delete(seleccion)
            messagebox.showinfo("Eliminado", "Vehículo eliminado con éxito.")

    
    boton_guardar = tk.Button(
        frame_contenido,
        text="Guardar Vehículo",
        bg="#123B6D",
        fg="white",
        font=("Arial", 11, "bold"),
        width=18,
        command=guardar_vehiculo
    )
    boton_guardar.pack(anchor="e", padx=50, pady=(15, 20))

    
    frame_tabla = tk.LabelFrame(
        frame_contenido,
        text="Vehículos registrados",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=20,
        pady=10
    )
    frame_tabla.pack(padx=50, fill="both", expand=True, pady=(0, 10))

    columnas = ("Patente", "Marca", "Modelo")
    tabla = ttk.Treeview(
        frame_tabla, columns=columnas, show="headings", height=5
    )

    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=150)

    tabla.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(
        frame_tabla, orient="vertical", command=tabla.yview
    )
    tabla.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    
    boton_eliminar = tk.Button(
        frame_contenido,
        text="Eliminar Seleccionado",
        bg="#A91D22",
        fg="white",
        font=("Arial", 10, "bold"),
        command=eliminar_vehiculo
    )
    boton_eliminar.pack(anchor="e", padx=50, pady=(0, 20))