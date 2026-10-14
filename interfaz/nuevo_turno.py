import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
import mysql.connector
from datos.choferes_db import listar_choferes
from datos.vehiculos_db import listar_vehiculos
from datos.turnos_db import horarios_ocupados, registrar_turno

HORARIOS = [f"{hora:02d}:00" for hora in range(8, 18)]


def mostrar_nuevo_turno(frame_contenido):
    tk.Label(frame_contenido, text="Nuevo Turno", bg="#FFFFFF", fg="#123B6D",
             font=("Arial", 24, "bold")).pack(anchor="w", padx=35, pady=(30, 10))
    tk.Label(frame_contenido, text="Complete los datos para asignar un nuevo turno",
             bg="#FFFFFF", fg="#555555", font=("Arial", 11)).pack(anchor="w", padx=35, pady=(0, 20))

    formulario = tk.LabelFrame(frame_contenido, text="Datos del turno", bg="#FFFFFF",
                              font=("Arial", 14, "bold"), padx=30, pady=20)
    formulario.pack(padx=35, fill="x")
    formulario.columnconfigure(1, weight=1)

    def campo_etiqueta(fila, texto):
        tk.Label(formulario, text=texto, bg="#FFFFFF", font=("Arial", 11)).grid(
            row=fila, column=0, sticky="w", padx=10, pady=10)

    campo_etiqueta(0, "Chofer:")
    combo_chofer = ttk.Combobox(formulario, state="readonly", width=40)
    combo_chofer.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    campo_etiqueta(1, "Vehículo:")
    combo_vehiculo = ttk.Combobox(formulario, state="readonly", width=40)
    combo_vehiculo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    campo_etiqueta(2, "Fecha (dd/mm/aaaa):")
    entrada_fecha = tk.Entry(formulario, font=("Arial", 11), relief="groove", bg="#F5F5F5")
    entrada_fecha.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    campo_etiqueta(3, "Hora:")
    combo_hora = ttk.Combobox(formulario, state="readonly", width=40)
    combo_hora.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

    choferes = {}
    vehiculos = {}

    def cargar_opciones():
        try:
            choferes.clear()
            vehiculos.clear()
            for dni, nombre, apellido, telefono, email in listar_choferes():
                choferes[f"{apellido}, {nombre} - {dni}"] = dni
            for patente, marca, modelo in listar_vehiculos():
                vehiculos[f"{patente} - {marca} {modelo}"] = patente
            combo_chofer["values"] = list(choferes)
            combo_vehiculo["values"] = list(vehiculos)
        except mysql.connector.Error as error:
            messagebox.showerror("Base de datos", f"No se pudieron cargar choferes y vehículos:\n{error}")

    def actualizar_horarios(event=None):
        combo_hora.set("")
        combo_hora["values"] = []
        texto = entrada_fecha.get().strip()
        try:
            fecha = datetime.strptime(texto, "%d/%m/%Y").date()
        except ValueError:
            return
        try:
            ocupados = horarios_ocupados(fecha)
            combo_hora["values"] = [hora for hora in HORARIOS if hora not in ocupados]
        except mysql.connector.Error as error:
            messagebox.showerror("Base de datos", f"No se pudo consultar disponibilidad:\n{error}")

    def guardar():
        try:
            fecha = datetime.strptime(entrada_fecha.get().strip(), "%d/%m/%Y").date()
        except ValueError:
            messagebox.showwarning("Datos inválidos", "Ingresá una fecha válida con formato dd/mm/aaaa.")
            return
        if fecha < date.today():
            messagebox.showwarning("Datos inválidos", "No se pueden reservar fechas anteriores a hoy.")
            return
        dni = choferes.get(combo_chofer.get())
        patente = vehiculos.get(combo_vehiculo.get())
        hora = combo_hora.get()
        if not dni or not patente or hora not in combo_hora["values"]:
            messagebox.showwarning("Datos incompletos", "Seleccioná chofer, vehículo y un horario disponible.")
            return
        try:
            identificador = registrar_turno(fecha, hora, dni, patente)
        except mysql.connector.IntegrityError as error:
            messagebox.showerror("Turno no disponible", "El horario ya está ocupado o los datos relacionados no son válidos.")
            actualizar_horarios()
            return
        except mysql.connector.Error as error:
            messagebox.showerror("Base de datos", f"No se pudo guardar el turno:\n{error}")
            return
        messagebox.showinfo("Turno registrado", f"Turno N.º {identificador} guardado correctamente.")
        combo_hora.set("")
        actualizar_horarios()

    entrada_fecha.bind("<FocusOut>", actualizar_horarios)
    entrada_fecha.bind("<Return>", actualizar_horarios)
    tk.Button(frame_contenido, text="Guardar Turno", command=guardar,
              bg="#123B6D", fg="#FFFFFF", font=("Arial", 11, "bold"),
              width=18, height=2).pack(anchor="e", padx=35, pady=20)
    cargar_opciones()
