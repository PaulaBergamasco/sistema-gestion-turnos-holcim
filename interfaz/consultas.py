import tkinter as tk
from tkinter import ttk

class VentanaConsultas(tk.Frame):
    def __init__(self, parent, lista_turnos=None):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=10, pady=10)
        
        if lista_turnos is not None:
            self.lista_turnos = lista_turnos
        else:
            self.lista_turnos = [
                {"id": 1, "fecha": "2026-09-17", "hora": "08:30", "patente": "AB123CD", "chofer": "Carlos Gómez", "dni": "35123456", "estado": "Pendiente"},
                {"id": 2, "fecha": "2026-09-17", "hora": "09:15", "patente": "CD456EF", "chofer": "María Fernández", "dni": "38987654", "estado": "En Proceso"},
                {"id": 3, "fecha": "2026-09-16", "hora": "14:00", "patente": "GH789IJ", "chofer": "Juan Pérez", "dni": "30456789", "estado": "Completado"},
                {"id": 4, "fecha": "2026-09-16", "hora": "16:45", "patente": "KL012MN", "chofer": "Ana López", "dni": "41234567", "estado": "Cancelado"},
                {"id": 5, "fecha": "2026-09-15", "hora": "11:00", "patente": "AB123CD", "chofer": "Carlos Gómez", "dni": "35123456", "estado": "Completado"},
            ]

        self.crear_interfaz()

    def crear_interfaz(self):
        frame_filtros = tk.LabelFrame(self, text=" Filtros de Búsqueda ", padx=10, pady=10)
        frame_filtros.pack(fill="x", pady=5)

        tk.Label(frame_filtros, text="DNI / Nombre Chofer / Patente:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.ent_criterio = tk.Entry(frame_filtros, width=25)
        self.ent_criterio.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_filtros, text="Estado del Turno:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.combo_estado = ttk.Combobox(
            frame_filtros, 
            values=["Todos", "Pendiente", "En Proceso", "Completado", "Cancelado"], 
            state="readonly"
        )
        self.combo_estado.current(0)
        self.combo_estado.grid(row=0, column=3, padx=5, pady=5)

        btn_buscar = tk.Button(frame_filtros, text="Buscar", bg="#005A9C", fg="white", command=self.ejecutar_consulta)
        btn_buscar.grid(row=0, column=4, padx=10, pady=5)

        btn_limpiar = tk.Button(frame_filtros, text="Limpiar", command=self.limpiar_filtros)
        btn_limpiar.grid(row=0, column=5, padx=5, pady=5)

        frame_tabla = tk.Frame(self)
        frame_tabla.pack(fill="both", expand=True, pady=10)

        columnas = ("ID", "Fecha", "Hora", "Patente", "Chofer", "Estado")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", selectmode="browse")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=120)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.ejecutar_consulta()

    def ejecutar_consulta(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        criterio = self.ent_criterio.get().strip().lower()
        estado = self.combo_estado.get()

        resultados = []
        for turno in self.lista_turnos:
            coincide_texto = (
                criterio == "" or
                criterio in turno["patente"].lower() or
                criterio in turno["chofer"].lower() or
                criterio in turno["dni"].lower()
            )

            coincide_estado = (
                estado == "Todos" or
                turno["estado"].lower() == estado.lower()
            )

            if coincide_texto and coincide_estado:
                resultados.append(turno)

        for reg in resultados:
            self.tabla.insert("", "end", values=(
                reg["id"],
                reg["fecha"],
                reg["hora"],
                reg["patente"],
                reg["chofer"],
                reg["estado"]
            ))

    def limpiar_filtros(self):
        self.ent_criterio.delete(0, tk.END)
        self.combo_estado.current(0)
        self.ejecutar_consulta()