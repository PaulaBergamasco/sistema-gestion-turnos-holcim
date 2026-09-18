import tkinter as tk
import tkinter.ttk as ttk


def mostrar_nuevo_turno(frame_contenido):

    titulo = tk.Label(
        frame_contenido,
        text="Nuevo Turno",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=(50, 10))

    descripcion = tk.Label(
        frame_contenido,
        text="Complete los datos para asignar un nuevo turno",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 11)
    )

    descripcion.pack(pady=(0, 30))

    formulario = tk.LabelFrame(
        frame_contenido,
        text="Datos del turno",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=30,
        pady=20
    )

    formulario.pack(padx=50, fill="x")

    label_chofer = tk.Label(
        formulario,
        text="Chofer:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_chofer.grid(
        row=0,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    combo_chofer = ttk.Combobox(
        formulario,
        state="readonly",
        width=40
    )

    combo_chofer.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )

    label_vehiculo = tk.Label(
        formulario,
        text="Vehículo:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_vehiculo.grid(
        row=1,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    combo_vehiculo = ttk.Combobox(
        formulario,
        state="readonly",
        width=40
    )

    combo_vehiculo.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )

    label_fecha = tk.Label(
        formulario,
        text="Fecha (dd/mm/aaaa):",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_fecha.grid(
        row=2,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    entrada_fecha = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 11),
        relief="groove",
        bg="#F5F5F5"
    )

    entrada_fecha.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )

    label_hora = tk.Label(
        formulario,
        text="Hora:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_hora.grid(
        row=3,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    combo_hora = ttk.Combobox(
        formulario,
        state="readonly",
        width=40
    )

    combo_hora.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
    )


    boton_guardar = tk.Button(
        frame_contenido,
        text="Guardar Turno",
        bg="#123B6D",
        fg="#FFFFFF",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
    )

    boton_guardar.pack(
        anchor="e",
        padx=50,
        pady=20
    )