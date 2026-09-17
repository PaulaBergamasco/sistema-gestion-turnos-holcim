import tkinter as tk


def mostrar_registro_choferes(frame_contenido):

    import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


def mostrar_registro_choferes(frame_contenido):

    
    titulo = tk.Label(
        frame_contenido,
        text="Registro de Choferes",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )

    titulo.pack(pady=(30, 10))

    descripcion = tk.Label(
        frame_contenido,
        text="Cargue los datos del chofer y consulte los vehículos que puede utilizar.",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 11)
    )

    descripcion.pack(pady=(0, 20))


    formulario = tk.LabelFrame(
        frame_contenido,
        text="Datos del chofer",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=30,
        pady=20
    )

    formulario.pack(
        padx=50,
        fill="x"
    )
    label_dni = tk.Label(
        formulario,
        text="DNI:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_dni.grid(
        row=0,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    entrada_dni = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 11),
        relief="groove",
        bg="#F5F5F5"
    )

    entrada_dni.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    label_nombre = tk.Label(
        formulario,
        text="Nombre:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_nombre.grid(
        row=1,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    entrada_nombre = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 11),
        relief="groove",
        bg="#F5F5F5"
    )

    entrada_nombre.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    label_apellido = tk.Label(
        formulario,
        text="Apellido:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_apellido.grid(
        row=2,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    entrada_apellido = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 11),
        relief="groove",
        bg="#F5F5F5"
    )

    entrada_apellido.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )
    label_telefono = tk.Label(
        formulario,
        text="Teléfono:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_telefono.grid(
        row=3,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    entrada_telefono = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 11),
        relief="groove",
        bg="#F5F5F5"
    )

    entrada_telefono.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
    )
    label_estado = tk.Label(
        formulario,
        text="Estado:",
        bg="#FFFFFF",
        font=("Arial", 11)
    )

    label_estado.grid(
        row=4,
        column=0,
        sticky="w",
        padx=10,
        pady=10
    )

    combo_estado = ttk.Combobox(
        formulario,
        values=[
            "Activo",
            "Inactivo"
        ],
        state="readonly",
        width=37,
        font=("Arial", 11)
    )

    combo_estado.grid(
        row=4,
        column=1,
        padx=10,
        pady=10
    )

    combo_estado.set("Activo")

    def limpiar_campos():

        entrada_dni.delete(
            0,
            tk.END
        )

        entrada_nombre.delete(
            0,
            tk.END
        )

        entrada_apellido.delete(
            0,
            tk.END
        )

        entrada_telefono.delete(
            0,
            tk.END
        )

        combo_estado.set("Activo")

        entrada_dni.focus()
    def guardar_chofer():

        dni = entrada_dni.get().strip()
        nombre = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        telefono = entrada_telefono.get().strip()
        estado = combo_estado.get()

        # Verificar campos obligatorios
        if not dni or not nombre or not apellido:

            messagebox.showwarning(
                "Campos incompletos",
                "Complete DNI, nombre y apellido del chofer."
            )

            return

        # Verificar DNI duplicado
        for item in tabla_choferes.get_children():

            valores = tabla_choferes.item(
                item,
                "values"
            )

            if valores and valores[0] == dni:

                messagebox.showwarning(
                    "DNI duplicado",
                    f"El DNI {dni} ya se encuentra registrado."
                )

                return

        # Insertar chofer
        tabla_choferes.insert(
            "",
            "end",
            values=(
                dni,
                nombre,
                apellido,
                telefono,
                estado
            )
        )

        limpiar_campos()

        messagebox.showinfo(
            "Chofer registrado",
            f"El chofer {nombre} {apellido} fue registrado correctamente."
        )
    frame_tabla = tk.LabelFrame(
        frame_contenido,
        text="Choferes registrados",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=20,
        pady=10
    )

    frame_tabla.pack(
        padx=50,
        fill="both",
        expand=True,
        pady=(20, 10)
    )

    columnas = (
        "DNI",
        "Nombre",
        "Apellido",
        "Teléfono",
        "Estado"
    )

    tabla_choferes = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=6
    )

    # Configurar columnas
    for columna in columnas:

        tabla_choferes.heading(
            columna,
            text=columna
        )

        tabla_choferes.column(
            columna,
            anchor="center",
            width=130
        )

    tabla_choferes.pack(
        side="left",
        fill="both",
        expand=True
    )

    def eliminar_chofer():

        seleccion = tabla_choferes.selection()

        if not seleccion:

            messagebox.showwarning(
                "Atención",
                "Seleccione un chofer de la lista para eliminar."
            )

            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Desea eliminar el chofer seleccionado?"
        )

        if confirmar:

            for item in seleccion:

                tabla_choferes.delete(item)

            messagebox.showinfo(
                "Eliminado",
                "Chofer eliminado correctamente."
            )

    # ==========================================================
    # BOTONES
    # ==========================================================

    frame_botones = tk.Frame(
        frame_contenido,
        bg="#FFFFFF"
    )

    frame_botones.pack(
        fill="x",
        padx=50,
        pady=(0, 20)
    )

    # Botón guardar
    boton_guardar = tk.Button(
        frame_botones,
        text="Guardar Chofer",
        bg="#123B6D",
        fg="white",
        activebackground="#0D2D52",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        relief="flat",
        cursor="hand2",
        command=guardar_chofer
    )

    boton_guardar.pack(
        side="left",
        padx=(0, 10)
    )

    # Botón limpiar
    boton_limpiar = tk.Button(
        frame_botones,
        text="Limpiar",
        bg="#E9EEF5",
        fg="#123B6D",
        activebackground="#D3DEEC",
        font=("Arial", 11, "bold"),
        width=15,
        height=2,
        relief="flat",
        cursor="hand2",
        command=limpiar_campos
    )

    boton_limpiar.pack(
        side="left",
        padx=10
    )

    # Botón eliminar
    boton_eliminar = tk.Button(
        frame_botones,
        text="Eliminar Seleccionado",
        bg="#A91D22",
        fg="white",
        activebackground="#80161A",
        activeforeground="white",
        font=("Arial", 10, "bold"),
        width=20,
        height=2,
        relief="flat",
        cursor="hand2",
        command=eliminar_chofer
    )

    boton_eliminar.pack(
        side="right"
    )
    informacion = tk.Label(
        frame_contenido,
        text="Nota: los vehículos no se asignan de manera permanente al chofer. "
             "La relación Chofer - Vehículo se establece al generar un turno.",
        bg="#FFFFFF",
        fg="#666666",
        font=("Arial", 9, "italic"),
        wraplength=900,
        justify="center"
    )

    informacion.pack(
        pady=(0, 10)
    )

