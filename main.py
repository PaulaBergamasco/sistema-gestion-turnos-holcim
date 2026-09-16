import tkinter as tk
from interfaz.inicio import mostrar_inicio
from interfaz.consultas import mostrar_consultas
from interfaz.gestion_turnos import mostrar_gestion_turnos
from interfaz.nuevo_turno import mostrar_nuevo_turno
from interfaz.registro_choferes import mostrar_registro_choferes
from interfaz.registro_vehiculos import mostrar_registro_vehiculos

def limpiar_pantalla():
    for widget in frame_contenido.winfo_children():
        widget.destroy()

def mostrar_pantalla_inicio():
    limpiar_pantalla()
    mostrar_inicio(frame_contenido)

def mostrar_pantalla_nuevo_turno():
    limpiar_pantalla()
    mostrar_nuevo_turno(frame_contenido)

def mostrar_pantalla_gestion_turnos():
    limpiar_pantalla()
    mostrar_gestion_turnos(frame_contenido)

def mostrar_pantalla_registro_vehiculos():
    limpiar_pantalla()
    mostrar_registro_vehiculos(frame_contenido)

def mostrar_pantalla_registro_choferes():
    limpiar_pantalla()
    mostrar_registro_choferes(frame_contenido)

def mostrar_pantalla_consultas():
    limpiar_pantalla()
    mostrar_consultas(frame_contenido)

ventana = tk.Tk()
ventana.title("Sistema de Gestión de Turnos - Holcim")
ventana.geometry("1200x700")

frame_menu = tk.Frame(
    ventana,
    bg="#E9EEF5",
    width=250
)

frame_menu.pack(
    side="left",
    fill="y"
)

frame_contenido = tk.Frame(
    ventana,
    bg="#FFFFFF",
)

frame_contenido.pack(
    side="right",
    fill="both",
    expand=True
)

titulo_menu = tk.Label(
    frame_menu,
    text="HOLCIM",
    bg="#E9EEF5",
    fg="#123B6D",
    font=("Arial", 22, "bold")
)

titulo_menu.pack(
    pady=(30, 30),
    padx=(60, 60)
)

mostrar_inicio(frame_contenido)

boton_inicio = tk.Button(
    frame_menu,
    text="Inicio",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_inicio
)

boton_inicio.pack(
    padx=15,
    pady=5
)

boton_nuevo_turno = tk.Button(
    frame_menu,
    text="Nuevo Turno",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_nuevo_turno
)

boton_nuevo_turno.pack(padx=15, pady=5)

boton_gestion_turnos = tk.Button(
    frame_menu,
    text="Gestión de Turnos",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_gestion_turnos
)

boton_gestion_turnos.pack(padx=15, pady=5)

boton_vehiculos = tk.Button(
    frame_menu,
    text="Registro de Vehículos",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_registro_vehiculos
)

boton_vehiculos.pack(padx=15, pady=5)

boton_choferes = tk.Button(
    frame_menu,
    text="Registro de Choferes",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_registro_choferes
)

boton_choferes.pack(padx=15, pady=5)

boton_consultas = tk.Button(
    frame_menu,
    text="Consultas",
    font=("Arial", 11),
    bg="#E9EEF5",
    width=22,
    height=2,
    command=mostrar_pantalla_consultas
)

boton_consultas.pack(padx=15, pady=5)


ventana.mainloop()
