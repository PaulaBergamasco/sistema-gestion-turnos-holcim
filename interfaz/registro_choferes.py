import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datos.choferes_db import listar_choferes, registrar_chofer, eliminar_chofer as eliminar_en_bd


def mostrar_registro_choferes(frame_contenido):
    
    titulo = tk.Label(
        frame_contenido,
        text="Registro de Choferes",
        bg="#FFFFFF",
        fg="#123B6D",
        font=("Arial", 24, "bold")
    )

    titulo.pack(anchor="w", padx=35, pady=(30, 10))

    descripcion = tk.Label(
        frame_contenido,
        text="Cargue los datos del chofer y consulte los vehículos que puede utilizar.",
        bg="#FFFFFF",
        fg="#555555",
        font=("Arial", 11)
    )

    descripcion.pack(anchor="w", padx=35, pady=(0, 20))


    formulario = tk.LabelFrame(
        frame_contenido,
        text="Datos del chofer",
        bg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=30,
        pady=20
    )

    formulario.pack(
        padx=35,
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

    label_email = tk.Label(formulario, text="Email:", bg="#FFFFFF", font=("Arial", 11))
    label_email.grid(row=4, column=0, sticky="w", padx=10, pady=10)
    entrada_email = tk.Entry(formulario, width=40, font=("Arial", 11), relief="groove", bg="#F5F5F5")
    entrada_email.grid(row=4, column=1, padx=10, pady=10)

    def cargar_tabla():
        """Carga en la grilla los choferes almacenados en la BD."""
        for item in tabla_choferes.get_children():
            tabla_choferes.delete(item)
        try:
            choferes = listar_choferes()
            for c in choferes:
                tabla_choferes.insert("", "end", values=c)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los choferes: {e}")

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

        entrada_email.delete(0, tk.END)
        entrada_dni.focus()

    def guardar_chofer():

        dni = entrada_dni.get().strip()
        nombre = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        telefono = entrada_telefono.get().strip()
        email = entrada_email.get().strip()

        
        if not dni or not nombre or not apellido or not telefono or not email:

            messagebox.showwarning(
                "Campos incompletos",
                "Complete todos los campos del chofer."
            )

            return

        if "@" not in email or "." not in email.split("@")[-1] or email.count("@") != 1:
            messagebox.showwarning("Email inválido", "Ingrese un email válido.")
            return

        try:
            registrar_chofer(dni, nombre, apellido, telefono, email)
            limpiar_campos()
            cargar_tabla()
            messagebox.showinfo(
                "Chofer registrado",
                f"El chofer {nombre} {apellido} fue registrado correctamente."
            )
        except Exception:
            messagebox.showerror(
                "DNI duplicado o error",
                f"No se pudo registrar. Verifique si el DNI {dni} ya existe."
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
        padx=35,
        fill="both",
        expand=True,
        pady=(20, 10)
    )

    columnas = (
        "DNI",
        "Nombre",
        "Apellido",
        "Teléfono",
        "Email"
    )

    tabla_choferes = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=6
    )

    
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
            dni = tabla_choferes.item(seleccion[0], "values")[0]
            try:
                eliminar_en_bd(dni)
                cargar_tabla()
                messagebox.showinfo("Eliminado", "Chofer eliminado correctamente.")
            except Exception:
                messagebox.showerror("Error", "No se puede eliminar el chofer si tiene turnos asociados.")

    frame_botones = tk.Frame(
        frame_contenido,
        bg="#FFFFFF"
    )

    frame_botones.pack(
        fill="x",
        padx=35,
        pady=(0, 20)
    )

    
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
        side="right"
    )

    
    boton_limpiar = tk.Button(
        frame_botones,
        text="Limpiar",
        bg="#E9EEF5",
        fg="#123B6D",
        activebackground="#D3DEEC",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        relief="flat",
        cursor="hand2",
        command=limpiar_campos
    )

    boton_limpiar.pack(
        side="right",
        padx=(0, 10)
    )

    # Botón eliminar
    boton_eliminar = tk.Button(
        frame_botones,
        text="Eliminar Seleccionado",
        bg="#A91D22",
        fg="white",
        activebackground="#80161A",
        activeforeground="white",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        relief="flat",
        cursor="hand2",
        command=eliminar_chofer
    )

    boton_eliminar.pack(
        side="right",
        padx=(0, 10)
    )

    
    cargar_tabla()