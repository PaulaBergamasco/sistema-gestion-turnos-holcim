import tkinter as tk


def mostrar_inicio(frame_contenido):

    titulo = tk.Label(
        frame_contenido,
        text="Sistema de Gestión de Turnos",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=(100, 10))

    subtitulo = tk.Label(
        frame_contenido,
        text="Playa de operaciones Holcim",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 14, "bold")
    )

    subtitulo.pack(pady=(10, 10))

    ubicacion = tk.Label(
        frame_contenido,
        text="Planta Malagueño - Córdoba",
        bg="#FFFFFF",
        font=("Arial", 12)
    )

    ubicacion.pack()

    bienvenida = tk.Label(
        frame_contenido,
        text="Bienvenido al Sistema de Gestión de Turnos",
        bg="#FFFFFF",
        font=("Arial", 16, "bold")
    )

    bienvenida.pack(pady=(80, 10))

    indicacion = tk.Label(
        frame_contenido,
        text="Seleccione una opción del menú lateral para comenzar.",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 12)
    )

    indicacion.pack()

    logo = tk.PhotoImage(file="imagenes/1626213854995.png")

    imagen_logo = tk.Label(
        frame_contenido,
        image=logo,
        bg="#FFFFFF"
    )

    imagen_logo.image = logo
    imagen_logo.pack(side="bottom", pady=100)