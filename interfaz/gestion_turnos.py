import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import datetime

from datos.gestion_turnos_db import (
    listar_turnos,
    modificar_turno,
    cambiar_estado,
    eliminar_turno
)


def mostrar_gestion_turnos(frame_contenido):

    titulo = tk.Label(
        frame_contenido,
        text="Gestión de Turnos",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )
    titulo.pack(anchor="w", padx=35, pady=(30, 10))

    descripcion = tk.Label(
        frame_contenido,
        text="Seleccione un turno para modificar, cambiar su estado o eliminarlo.",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 11)
    )
    descripcion.pack(anchor="w", padx=35, pady=(0, 20))

    frame_tabla = tk.LabelFrame(
        frame_contenido,
        text="Turnos registrados",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 14, "bold"),
        padx=10,
        pady=10
    )

    frame_tabla.pack(
        fill="both",
        expand=True,
        padx=35,
        pady=(0, 15)
    )

    columnas = (
        "ID",
        "Fecha",
        "Hora",
        "Chofer",
        "Vehículo",
        "Estado"
    )

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=10
    )

    for columna in columnas:
        tabla.heading(
            columna,
            text=columna
        )

    tabla.column("ID", width=50, anchor="center")
    tabla.column("Fecha", width=110, anchor="center")
    tabla.column("Hora", width=90, anchor="center")
    tabla.column("Chofer", width=180, anchor="center")
    tabla.column("Vehículo", width=220, anchor="center")
    tabla.column("Estado", width=130, anchor="center")

    barra_vertical = ttk.Scrollbar(
        frame_tabla,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=barra_vertical.set
    )

    tabla.pack(
        side="left",
        fill="both",
        expand=True
    )

    barra_vertical.pack(
        side="right",
        fill="y"
    )

    # -----------------------------------------
    # CARGAR / RECARGAR TURNOS
    # -----------------------------------------

    def cargar_turnos():

        for item in tabla.get_children():
            tabla.delete(item)

        try:
            turnos = listar_turnos()

            for turno in turnos:
                tabla.insert(
                    "",
                    "end",
                    values=turno
                )

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se pudieron cargar los turnos.\n{error}"
            )

    cargar_turnos()

    # -----------------------------------------
    # MODIFICAR TURNO
    # -----------------------------------------

    def accion_modificar():

        seleccionado = tabla.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Atención",
                "Seleccione un turno para modificar."
            )
            return

        item = tabla.item(seleccionado[0])
        valores = item["values"]

        id_turno = valores[0]
        fecha_actual = valores[1]
        hora_actual = valores[2]

        ventana = tk.Toplevel()
        ventana.title("Modificar Turno")
        ventana.geometry("380x250")
        ventana.resizable(False, False)

        tk.Label(
            ventana,
            text=f"Modificar turno ID {id_turno}",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(
            ventana,
            text="Fecha (DD/MM/AAAA)"
        ).pack()

        entrada_fecha = tk.Entry(
            ventana,
            width=25
        )
        entrada_fecha.pack(pady=5)
        entrada_fecha.insert(0, fecha_actual)

        tk.Label(
            ventana,
            text="Hora (HH:MM)"
        ).pack()

        entrada_hora = tk.Entry(
            ventana,
            width=25
        )
        entrada_hora.pack(pady=5)
        entrada_hora.insert(0, hora_actual)

        def guardar_modificacion():

            fecha = entrada_fecha.get().strip()
            hora = entrada_hora.get().strip()

            try:
                fecha_mysql = datetime.strptime(
                    fecha,
                    "%d/%m/%Y"
                ).strftime("%Y-%m-%d")

                datetime.strptime(
                    hora,
                    "%H:%M"
                )

            except ValueError:
                messagebox.showwarning(
                    "Datos incorrectos",
                    "Ingrese la fecha como DD/MM/AAAA y la hora como HH:MM."
                )
                return

            try:
                modificar_turno(
                    id_turno,
                    fecha_mysql,
                    hora
                )

                messagebox.showinfo(
                    "Éxito",
                    "Turno modificado correctamente."
                )

                ventana.destroy()
                cargar_turnos()

            except Exception as error:
                messagebox.showerror(
                    "Error",
                    f"No se pudo modificar el turno.\n{error}"
                )

        boton_guardar = tk.Button(
            ventana,
            text="Guardar cambios",
            command=guardar_modificacion,
            width=18
        )

        boton_guardar.pack(pady=15)

    # -----------------------------------------
    # CAMBIAR ESTADO
    # -----------------------------------------

    def accion_cambiar_estado():

        seleccionado = tabla.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Atención",
                "Seleccione un turno."
            )
            return

        item = tabla.item(seleccionado[0])
        valores = item["values"]

        id_turno = valores[0]
        estado_actual = valores[5]

        ventana = tk.Toplevel()
        ventana.title("Cambiar Estado")
        ventana.geometry("350x220")
        ventana.resizable(False, False)

        tk.Label(
            ventana,
            text=f"Turno ID {id_turno}",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Label(
            ventana,
            text="Seleccione el nuevo estado:"
        ).pack(pady=5)

        estados = [
            "Programado",
            "Demorado",
            "En proceso",
            "Finalizado",
            "Cancelado"
        ]

        combo_estado = ttk.Combobox(
            ventana,
            values=estados,
            state="readonly",
            width=25
        )

        combo_estado.pack(pady=10)
        combo_estado.set(estado_actual)

        def guardar_estado():

            nuevo_estado = combo_estado.get()

            try:
                cambiar_estado(
                    id_turno,
                    nuevo_estado
                )

                messagebox.showinfo(
                    "Éxito",
                    "Estado actualizado correctamente."
                )

                ventana.destroy()
                cargar_turnos()

            except Exception as error:
                messagebox.showerror(
                    "Error",
                    f"No se pudo cambiar el estado.\n{error}"
                )

        boton_guardar = tk.Button(
            ventana,
            text="Guardar Estado",
            command=guardar_estado,
            width=18
        )

        boton_guardar.pack(pady=10)

    # -----------------------------------------
    # ELIMINAR TURNO
    # -----------------------------------------

    def accion_eliminar():

        seleccionado = tabla.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Atención",
                "Seleccione un turno para eliminar."
            )
            return

        item = tabla.item(seleccionado[0])
        valores = item["values"]

        id_turno = valores[0]

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Seguro que desea eliminar el turno ID {id_turno}?"
        )

        if not confirmar:
            return

        try:
            eliminar_turno(id_turno)

            messagebox.showinfo(
                "Éxito",
                "Turno eliminado correctamente."
            )

            cargar_turnos()

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"No se pudo eliminar el turno.\n{error}"
            )

    # -----------------------------------------
    # BOTONES
    # -----------------------------------------

    frame_acciones = tk.LabelFrame(
        frame_contenido,
        text="Acciones",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 14, "bold"),
        padx=20,
        pady=15
    )

    frame_acciones.pack(
        fill="x",
        padx=35,
        pady=(0, 30)
    )

    contenedor_botones = tk.Frame(
        frame_acciones,
        bg="#FFFFFF"
    )

    contenedor_botones.pack()

    boton_modificar = tk.Button(
        contenedor_botones,
        text="Modificar",
        bg="#123B6D",
        fg="#EAF3FF",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=accion_modificar
    )

    boton_modificar.pack(
        side="left",
        padx=8
    )

    boton_cambiar_estado = tk.Button(
        contenedor_botones,
        text="Cambiar Estado",
        bg="#F5F5F5",
        fg="#123B6D",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=accion_cambiar_estado
    )

    boton_cambiar_estado.pack(
        side="left",
        padx=8
    )

    boton_eliminar = tk.Button(
        contenedor_botones,
        text="Eliminar",
        bg="#A91D22",
        fg="#EAF3FF",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=accion_eliminar
    )

    boton_eliminar.pack(
        side="left",
        padx=8
    )
