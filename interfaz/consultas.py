import tkinter as tk
from tkinter import ttk

def mostrar_consultas(frame_contenido):
    for widget in frame_contenido.winfo_children():
        widget.destroy()

    
    frame_main = tk.Frame(frame_contenido, bg="#FFFFFF")
    frame_main.pack(fill=tk.BOTH, expand=True, padx=35, pady=(30, 20))

    
    lbl_titulo = tk.Label(
        frame_main, 
        text="Consultas", 
        font=("Arial", 24, "bold"), 
        bg="#FFFFFF", 
        fg="#123B6D"
    )
    lbl_titulo.pack(anchor="w", pady=(0, 10))

    descripcion = tk.Label(
        frame_main, text="Consulte los turnos registrados utilizando los filtros",
        bg="#FFFFFF", fg="#555555", font=("Arial", 11)
    )
    descripcion.pack(anchor="w", pady=(0, 20))

   
    frame_filtros = tk.LabelFrame(
        frame_main, 
        text="Filtros de búsqueda", 
        font=("Arial", 14, "bold"), 
        bg="#FFFFFF", 
        fg="#123B6D", 
        padx=20, 
        pady=15
    )
    frame_filtros.pack(fill=tk.X, pady=(0, 15))

    tk.Label(frame_filtros, text="Buscar por:", bg="#FFFFFF", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    combo_criterio = ttk.Combobox(
        frame_filtros, 
        values=["Patente / Vehículo", "DNI / Chofer", "Número de Turno", "Estado"], 
        state="readonly",
        width=18
    )
    combo_criterio.grid(row=0, column=1, padx=5, pady=5)
    combo_criterio.current(0)

    tk.Label(frame_filtros, text="Término:", bg="#FFFFFF", font=("Arial", 11)).grid(row=0, column=2, padx=5, pady=5, sticky="w")
    txt_busqueda = tk.Entry(frame_filtros, width=25, font=("Arial", 11), relief="groove", bg="#F5F5F5")
    txt_busqueda.grid(row=0, column=3, padx=5, pady=5)

   
    def buscar():
        criterio = combo_criterio.get()
        valor = txt_busqueda.get().strip().lower()
        
        for item in tabla.get_children():
            tabla.delete(item)
            
        
        datos_ejemplo = [
            (1, "AB123CD", "35123456", "Juan Pérez", "20/10/2026 08:00", "Programado"),
            (2, "CD456EF", "28987654", "Carlos Gómez", "20/10/2026 10:00", "En proceso"),
            (3, "FG789HI", "40111222", "María Rodríguez", "20/10/2026 12:00", "Finalizado"),
            (4, "JK123LM", "32123456", "Chofer D", "21/10/2026 08:00", "Cancelado"),
            (5, "NO456PQ", "33123456", "Chofer E", "21/10/2026 14:00", "Programado"),
            (6, "RS789TU", "34123456", "Chofer F", "22/10/2026 09:00", "En proceso"),
        ]

        for registro in datos_ejemplo:
            if not valor:
                tabla.insert("", tk.END, values=registro)
            else:
                if (criterio == "Patente / Vehículo" and valor in registro[1].lower()) or \
                   (criterio == "DNI / Chofer" and (valor in registro[2].lower() or valor in registro[3].lower())) or \
                   (criterio == "Número de Turno" and valor in str(registro[0]).lower()) or \
                   (criterio == "Estado" and valor in registro[5].lower()):
                    tabla.insert("", tk.END, values=registro)

    def limpiar():
        txt_busqueda.delete(0, tk.END)
        buscar()

    
    btn_buscar = tk.Button(frame_filtros, text="Buscar", command=buscar, bg="#123B6D", fg="white", width=12, height=2, font=("Arial", 11, "bold"), relief=tk.FLAT)
    btn_buscar.grid(row=0, column=4, padx=10, pady=5)

    btn_limpiar = tk.Button(frame_filtros, text="Limpiar", command=limpiar, bg="#E9EEF5", fg="#123B6D", width=12, height=2, font=("Arial", 11, "bold"), relief=tk.FLAT)
    btn_limpiar.grid(row=0, column=5, padx=5, pady=5)

    
    frame_tabla = tk.LabelFrame(frame_main, text="Resultados de la consulta", bg="#FFFFFF", fg="#123B6D", font=("Arial", 14, "bold"), padx=10, pady=10)
    frame_tabla.pack(fill=tk.BOTH, expand=True)

    columnas = ("Turno", "Patente", "DNI Chofer", "Nombre Chofer", "Fecha / Hora", "Estado")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

    tabla.heading("Turno", text="N° Turno")
    tabla.heading("Patente", text="Patente")
    tabla.heading("DNI Chofer", text="DNI Chofer")
    tabla.heading("Nombre Chofer", text="Nombre Chofer")
    tabla.heading("Fecha / Hora", text="Fecha / Hora")
    tabla.heading("Estado", text="Estado")

    tabla.column("Turno", width=80, anchor="center")
    tabla.column("Patente", width=100, anchor="center")
    tabla.column("DNI Chofer", width=100, anchor="center")
    tabla.column("Nombre Chofer", width=180, anchor="w")
    tabla.column("Fecha / Hora", width=130, anchor="center")
    tabla.column("Estado", width=100, anchor="center")

    
    scrollbar_y = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tabla.yview)
    scrollbar_x = ttk.Scrollbar(frame_tabla, orient=tk.HORIZONTAL, command=tabla.xview)
    tabla.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    tabla.grid(row=0, column=0, sticky="nsew")
    scrollbar_y.grid(row=0, column=1, sticky="ns")
    scrollbar_x.grid(row=1, column=0, sticky="ew")

    frame_tabla.grid_rowconfigure(0, weight=1)
    frame_tabla.grid_columnconfigure(0, weight=1)

    
    buscar()
   

    pass
