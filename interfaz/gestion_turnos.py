import tkinter as tk
import tkinter.ttk as ttk


def mostrar_gestion_turnos(frame_contenido):
    titulo = tk.Label(
        frame_contenido,
        text="Gestión de Turnos",
        bg="#FFFFFF",
        fg="#6D1265",
        font=("Arial", 24, "bold")
    )
    titulo.pack(anchor="w", padx=35, pady=(30, 0))

    descripcion = tk.Label(
        frame_contenido,
        text="Seleccione un turno para modificar, cambiar su estado o eliminarlo.",
        bg="#FFFFFF",
        fg="#6D1212",
        font=("Arial", 11)
    )
    descripcion.pack(anchor="w", padx=35, pady=(0, 20))

    frame_tabla = tk.LabelFrame(
        frame_contenido,
        text="Turnos registrados",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 13, "bold"),
        padx=10,
        pady=10
    )
    frame_tabla.pack(fill="both", expand=True, padx=35, pady=(0, 15))

    columnas = ("ID", "Fecha", "Hora", "Chofer", "Vehículo", "Estado")

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=10
    )

    for columna in columnas:
        tabla.heading(columna, text=columna)

    tabla.column("ID", width=50, anchor="center")
    tabla.column("Fecha", width=110, anchor="center")
    tabla.column("Hora", width=90, anchor="center")
    tabla.column("Chofer", width=180, anchor="center")
    tabla.column("Vehículo", width=150, anchor="center")
    tabla.column("Estado", width=130, anchor="center")

    turnos_de_ejemplo = [
        (1, "10/10/2024", "08:00", "Chofer A", "Vehículo 1", "Programado"),
        (2, "10/10/2024", "10:00", "Chofer B", "Vehículo 2", "En proceso"),
        (3, "10/10/2024", "12:00", "Chofer C", "Vehículo 3", "Finalizado"),
        (4, "11/10/2024", "08:00", "Chofer D", "Vehículo 4", "Cancelado"),
        (5, "11/10/2024", "14:00", "Chofer E", "Vehículo 5", "Programado"),
        (6, "12/10/2024", "09:00", "Chofer F", "Vehículo 6", "En proceso")
    ]

    for turno in turnos_de_ejemplo:
        tabla.insert("", "end", values=turno)

    barra_vertical = ttk.Scrollbar(
        frame_tabla,
        orient="vertical",
        command=tabla.yview
    )
    tabla.configure(yscrollcommand=barra_vertical.set)

    tabla.pack(side="left", fill="both", expand=True)
    barra_vertical.pack(side="right", fill="y")

    frame_acciones = tk.LabelFrame(
        frame_contenido,
        text="Acciones",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 13, "bold"),
        padx=20,
        pady=15
    )
    frame_acciones.pack(fill="x", padx=35, pady=(0, 30))

    contenedor_botones = tk.Frame(frame_acciones, bg="#FFFFFF")
    contenedor_botones.pack()

    boton_modificar = tk.Button(
        contenedor_botones,
        text="Modificar",
        bg="#EAF3FF",
        fg="#123B6D",
        font=("Arial", 11),
        width=18,
        height=2
    )
    boton_modificar.pack(side="left", padx=8)

    boton_cambiar_estado = tk.Button(
        contenedor_botones,
        text="Cambiar Estado",
        bg="#F5F5F5",
        fg="#123B6D",
        font=("Arial", 11),
        width=18,
        height=2
    )
    boton_cambiar_estado.pack(side="left", padx=8)

    boton_eliminar = tk.Button(
        contenedor_botones,
        text="Eliminar",
        bg="#FFE7E7",
        fg="#A91D22",
        font=("Arial", 11),
        width=18,
        height=2
    )
    boton_eliminar.pack(side="left", padx=8)
