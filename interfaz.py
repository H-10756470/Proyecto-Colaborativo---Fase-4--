import tkinter as tk
from tkinter import ttk, messagebox

import excepciones
import servicios
from cliente import Cliente
from logger_config import logger, logger_configuracion

# Importamos la clase Reserva de la Parte D
from reserva import Reserva


# Esta clase es para crear la ventana principal de Software FJ.
class SoftwareFJInterfaz:
    def __init__(self, ventana_principal): 
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Software FJ - Sistema de Gestion")
        self.ventana_principal.geometry("1080x650") # tamano de la ventana
        self.ventana_principal.minsize(1080, 650)  # Tamaño mínimo de la ventana
        self.ventana_principal.config(bg="#1e1e1e")  # Este es el color de fondo oscuro.

        # Esto permite que la ventana y sus widgets se ajusten al tamaño de pantalla del dispositivo donde se ejecute el programa, haciendo que la interfaz sea responsiva.
        self.ventana_principal.rowconfigure(0, weight=1)
        self.ventana_principal.columnconfigure(0, weight=1)

        # Aqui creo el frame principal y la barra lateral izquierda. El frame principal es donde se mostrara la informacion de los clientes, servicios y reservas. 
        self.frame_principal = tk.Frame(self.ventana_principal, bg="#0C1A34")  # Este es el color de fondo azul oscuro.
        self.frame_principal.pack(side="right", fill="both", expand=True)

        # Aqui creo los widgets hijos del frame principal. Estos widgets son los que se mostraran en la parte derecha de la ventana, donde se mostrara la informacion de los clientes, servicios y reservas.
        # Mas adelante desarrollare esta parte.

        # La barra lateral izquierda es donde estaran los botones para navegar entre las diferentes secciones del software.
        self.barra_lateral_izquierda = tk.Frame(self.ventana_principal, bg="#10264E", width=200)
        self.barra_lateral_izquierda.pack(side="left", fill="y")
        self.barra_lateral_izquierda.pack_propagate(False)  # Esto evita que la barra lateral se ajuste automáticamente al tamaño de sus widgets internos.

        # Aqui dentro del frame menu, creo los botones Inicio, Clientes, Servicios, Reservas y Logs. Estos botones seran los que permitan navegar entre las diferentes secciones del software.
        self.menu = tk.Frame(self.barra_lateral_izquierda, bg="#10264E")
        self.menu.pack(fill="both", expand=True)

        self.boton_inicio = tk.Button(
            self.menu, 
            text="🏠  Inicio", 
            font=("Segoe UI", 17), 
            bg="#10264E", 
            fg="white", 
            anchor="w", 
            padx=35,
            command= self.mostrar_pestaña_inicio  # Este comando llama a la funcion mostrar_inicio cuando se presiona el boton Inicio.
        )
        self.boton_inicio.pack(fill="x", pady=6)
        self.configurar_efectos_hover(self.boton_inicio)  # Configuro los efectos hover para el boton Inicio.
        self.quitar_bordes_botones(self.boton_inicio)

        self.boton_clientes = tk.Button(
            self.menu, 
            text="👤 Clientes", 
            font=("Segoe UI", 17), 
            bg="#10264E", 
            fg="white", 
            anchor="w", 
            padx=35,
            activeforeground="#0064E9",
            command=self.mostrar_pestaña_clientes  # Este comando llama a la funcion mostrar_clientes cuando se presiona el boton Clientes.
        )
        self.boton_clientes.pack(fill="x", pady=6)
        self.configurar_efectos_hover(self.boton_clientes)  # Configuro los efectos hover para el boton Clientes.
        self.quitar_bordes_botones(self.boton_clientes)

        self.boton_servicios = tk.Button(
            self.menu, text="⚙️ Servicios", 
            font=("Segoe UI", 17), 
            bg="#10264E", 
            fg="white", 
            anchor="w", 
            padx=35,
            command=self.mostrar_pestaña_servicios  # Este comando llama a la funcion mostrar_servicios cuando se presiona el boton Servicios.
        )
        self.boton_servicios.pack(fill="x", pady=6)
        self.configurar_efectos_hover(self.boton_servicios)  # Configuro los efectos hover para el boton Servicios.
        self.quitar_bordes_botones(self.boton_servicios)

        self.boton_reservas = tk.Button(
            self.menu, text="📅 Reservas", 
            font=("Segoe UI", 17), 
            bg="#10264E", 
            fg="white", 
            anchor="w", 
            padx=35,
            command=self.mostrar_pestaña_reservas  # Este comando llama a la funcion mostrar_reservas cuando se presiona el boton Reservas.
        )
        self.boton_reservas.pack(fill="x", pady=6)
        self.configurar_efectos_hover(self.boton_reservas)  # Configuro los efectos hover para el boton Reservas.
        self.quitar_bordes_botones(self.boton_reservas)

        self.boton_logs = tk.Button(
            self.menu, 
            text="📄 Logs", 
            font=("Segoe UI", 17), 
            bg="#10264E", 
            fg="white", 
            anchor="w", 
            padx=35,
            command=self.mostrar_pestaña_logs  # Este comando llama a la funcion mostrar_logs cuando se presiona el boton Logs.
        )  
        self.boton_logs.pack(fill="x", pady=6)
        self.configurar_efectos_hover(self.boton_logs)  # Configuro los efectos hover para el boton Logs.
        self.quitar_bordes_botones(self.boton_logs)

        # Aqui creo el label de la parte inferior para mostrar el logotipo de Software Fj.
        self.label_logotipo = tk.Label(self.barra_lateral_izquierda, text="   FJ♟️", font=("Courier New", 25), bg="#10264E", fg="white")
        self.label_logotipo.pack(side="bottom", fill="x")
        # Aqui pongo el nombre de la empresa
        self.label_nombre_empresa = tk.Label(self.barra_lateral_izquierda, text="Software", font=("Courier New", 25), bg="#10264E", fg="white")
        self.label_nombre_empresa.pack(side="bottom", fill="x")

        # Los clientes ya se guardan en Cliente.clientes_registrados. Aqui creo las listas internas para los servicios y las reservas, ya que no se usan bases de datos.
        self.lista_servicios = []
        self.lista_reservas = []
        logger.info("Se inicio la interfaz de Software FJ")

        # Hace que se muestre al iniciar la pestaña Inicio
        self.mostrar_pestaña_inicio()

    def limpiar_frame_principal(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def mostrar_pestaña_inicio(self):
        self.limpiar_frame_principal()
        frame_encabezado_inicio = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_inicio.pack(side="top", fill="x")
        # H1
        H1_inicio = tk.Label(frame_encabezado_inicio, text="Panel Principal - Software FJ", font=("Segoe UI", 28), bg="#0C1A34", fg="white")
        H1_inicio.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_inicio, text="Gestion de clientes, servicios y reservas", font=("Segoe UI", 14), bg="#0C1A34", fg="#DDE8FF")
        subtitulo.pack()
        # Frame padre de los botones "Gestionar Clientes", "Gestionar Servicios"
        frame_botones_fila1 = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_botones_fila1.pack(side="top", fill="x")
        # Boton "Gestionar Clientes"
        boton_gestionar_clientes = tk.Button(frame_botones_fila1, text="👤 | Gestionar Clientes", font=("Segoe UI", 27), bg="#0060FD", fg="white", width=20, height=2, command=self.mostrar_pestaña_clientes, activebackground="#2CC8F7", activeforeground="#022211")
        boton_gestionar_clientes.pack(side="left", padx=10, pady=20)
        self.quitar_bordes_botones(boton_gestionar_clientes)
        # Boton "Gestionar Servicios"
        boton_gestionar_servicios = tk.Button(frame_botones_fila1, text="⚙️ | Gestionar Servicios", font=("Segoe UI", 27), bg="#0BB158", fg="white", width=20, height=2, command=self.mostrar_pestaña_servicios, activebackground="#2CF769", activeforeground="#022211")
        boton_gestionar_servicios.pack(side="left", padx=10, pady=20)
        self.quitar_bordes_botones(boton_gestionar_servicios)
        # Este frame es padre de "Gestionar Reservas" y "Eventos y Logs"
        frame_botones_fila2 = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_botones_fila2.pack(side="top", fill="x")
        # Boton "Gestionar Reservas"
        boton_gestionar_reservas = tk.Button(frame_botones_fila2, text="📅 | Gestionar Reservas", font=("Segoe UI", 27), bg="#FAB903", fg="white", width=20, height=2, command=self.mostrar_pestaña_reservas, activebackground="#EEFF00", activeforeground="#090A00")
        boton_gestionar_reservas.pack(side="left", padx=10, pady=20)
        self.quitar_bordes_botones(boton_gestionar_reservas)
        # Boton "Eventos y Logs"
        boton_Eventos = tk.Button(frame_botones_fila2, text="📄 | Eventos y Logs", font=("Segoe UI", 27), bg="#F72C2F", fg="white", width=20, height=2, command=self.mostrar_pestaña_logs, activebackground="#740505", activeforeground="#FCFCFC")
        boton_Eventos.pack(side="left", padx=10, pady=20)
        self.quitar_bordes_botones(boton_Eventos)

        # Este es el frame que contendra los labels que mostraran un resumen del sistema.
        frame_resumen = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_resumen.pack(fill="both", expand=True)

        # Aqui muestro cuantos clientes, servicios y reservas hay registrados.
        texto_resumen = "Clientes: " + str(len(Cliente.clientes_registrados)) + "   |   Servicios: " + str(len(self.lista_servicios)) + "   |   Reservas: " + str(len(self.lista_reservas))
        etiqueta_resumen = tk.Label(frame_resumen, text=texto_resumen, font=("Segoe UI", 16), bg="#0C1A34", fg="#DDE8FF")
        etiqueta_resumen.pack(pady=10)


    def mostrar_pestaña_clientes(self):
        self.limpiar_frame_principal()
        # Aqui creo el encabezado de la pestaña Clientes, que incluye un H1 y un subtitulo.
        frame_encabezado_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_clientes.pack(side="top", fill="x")
        # Aqui creo el H1 y el subtitulo de la pestaña Clientes.
        H1_clientes = tk.Label(frame_encabezado_clientes, text="Clientes", font=("Segoe UI", 28), bg="#0C1A34", fg="white")
        H1_clientes.pack(pady=20)
        subtitulo_clientes = tk.Label(frame_encabezado_clientes, text="Gestion de clientes", font=("Segoe UI", 14), bg="#0C1A34", fg="#DDE8FF")
        subtitulo_clientes.pack() 
        # Aqui creo el frame de busqueda de clientes, que incluye un campo de texto, un boton de busqueda y un boton para registrar clientes.
        frame_busqueda_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_busqueda_clientes.pack(side="top", fill="x")
        # Aqui creo el campo para buscar a un cliente registrado, creo el boton "Buscar" y "registrar cliente".
        campo_buscar_cliente = tk.Entry(frame_busqueda_clientes, font=("Segoe UI", 17), fg="#5770A3", )
        campo_buscar_cliente.pack(side="left", fill="x", padx=20, pady=50, expand=True)
        campo_buscar_cliente.insert(0, "Ingrese documento de identidad...")  # Texto de ejemplo en el campo de búsqueda
        campo_buscar_cliente.bind("<FocusIn>", lambda e: campo_buscar_cliente.delete(0, "end"))

        # Este es el boton "Buscar", llama a la funcion buscar_cliente con lo que se escribio en el campo.
        boton_buscar_cliente = tk.Button(frame_busqueda_clientes, text="🔍 Buscar", font=("Segoe UI", 16), bg="#0060FD", fg="white", activebackground="#2CC8F7", activeforeground="#022211", command=lambda: self.buscar_cliente(campo_buscar_cliente.get()))
        boton_buscar_cliente.pack(side="left", padx=(0, 20), pady=50)
        self.quitar_bordes_botones(boton_buscar_cliente)

        registrar_nuevo_cliente = tk.Button(frame_busqueda_clientes, text="➕ Registrar nuevo cliente ", font=("Segoe UI", 16), bg="#0AA552", fg="white", activebackground="#2CF769", activeforeground="#022211", command=self.abrir_formulario_cliente)
        registrar_nuevo_cliente.pack(side="left", fill="x", expand=True, pady=50)
        self.quitar_bordes_botones(registrar_nuevo_cliente)

        # Aqui creo el frame que contendra la lista de registro de todos los clientes.
        self.frame_lista_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        self.frame_lista_clientes.pack(side="top", fill="both", expand=True)
        # este es el titulo de la lista que muestra todos los clientes registrados en el sistema
        titulo_lista_clientes = tk.Label(self.frame_lista_clientes, text="📋 Lista de Clientes Registrados", font=("Segoe UI", 16), bg="#0060FD", fg="white" )
        titulo_lista_clientes.pack(side="top", fill="x")
        # Aqui creo la tabla para mostrar los datos de cada cliente registrado.
        # ERROR CORREGIDO: antes la columna se llamaba "correo electronico" pero en heading y column se usaba "correo", eso daba TclError al abrir la pestaña.
        columnas = ("identificador", "nombre", "telefono", "correo")
        tabla = ttk.Treeview(self.frame_lista_clientes, columns=columnas, show="headings")

        tabla.heading("identificador", text="Identificador")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("telefono", text="Teléfono")
        tabla.heading("correo", text="Correo")

        tabla.column("identificador", width=150)
        tabla.column("nombre", width=200)
        tabla.column("telefono", width=150)
        tabla.column("correo", width=250)

        tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )
        # Guardo la tabla en self para poder actualizarla desde otras funciones.
        self.tabla_clientes = tabla
        # Aqui lleno la tabla con los clientes registrados en la clase Cliente.
        self.actualizar_tabla_clientes()

    def actualizar_tabla_clientes(self, lista_clientes=None):
        """Esta funcion borra la tabla de clientes y la llena otra vez. Si no recibe una lista, muestra todos los clientes registrados."""
        if lista_clientes is None:
            lista_clientes = list(Cliente.clientes_registrados.values())
        for fila in self.tabla_clientes.get_children():
            self.tabla_clientes.delete(fila)
        for cliente in lista_clientes:
            self.tabla_clientes.insert("", "end", values=(cliente.identificador, cliente.nombre, cliente.telefono, cliente.correo))

    def buscar_cliente(self, texto):
        """Esta funcion busca un cliente por su documento usando el metodo de la clase Cliente."""
        texto = texto.strip()
        # Si dejo el texto de ejemplo o el campo vacio, muestro todos los clientes.
        if texto == "" or texto == "Ingrese documento de identidad...":
            self.actualizar_tabla_clientes()
            return
        try:
            cliente_encontrado = Cliente.obtener_datos_cliente_especifico(texto)
        except Exception as error:
            self.manejar_error(error)
        else:
            self.actualizar_tabla_clientes([cliente_encontrado])

    def abrir_formulario_cliente(self):
        """Esta funcion abre una ventana pequena con el formulario para registrar un cliente."""
        formulario = tk.Toplevel(self.ventana_principal)
        formulario.title("Registrar nuevo cliente")
        formulario.geometry("450x470")
        formulario.config(bg="#0C1A34")
        formulario.transient(self.ventana_principal)
        formulario.grab_set()  # Esto bloquea la ventana principal mientras el formulario este abierto.

        # Aqui creo los labels y los campos de texto del formulario.
        campos = ["Documento", "Nombre completo", "Telefono", "Correo electronico"]
        entradas = []
        for nombre_campo in campos:
            etiqueta = tk.Label(formulario, text=nombre_campo, font=("Segoe UI", 13), bg="#0C1A34", fg="white")
            etiqueta.pack(pady=(15, 0))
            entrada = tk.Entry(formulario, font=("Segoe UI", 14))
            entrada.pack(padx=40, fill="x")
            entradas.append(entrada)

        # Esta funcion se ejecuta cuando se presiona el boton Guardar.
        def guardar_cliente():
            try:
                # La clase Cliente hace todas las validaciones y lo guarda en su diccionario.
                Cliente(entradas[0].get(), entradas[1].get(), entradas[2].get(), entradas[3].get())
            except Exception as error:
                self.manejar_error(error)
            else:
                messagebox.showinfo("Cliente registrado", "El cliente se registro correctamente")
                formulario.destroy()
                self.actualizar_tabla_clientes()

        boton_guardar = tk.Button(formulario, text="💾 Guardar cliente", font=("Segoe UI", 15), bg="#0AA552", fg="white", activebackground="#2CF769", activeforeground="#022211", command=guardar_cliente)
        boton_guardar.pack(pady=25)
        self.quitar_bordes_botones(boton_guardar)

    def mostrar_pestaña_servicios(self):
        self.limpiar_frame_principal()
        # Este es el frame donde iran el H1 y el subtitulo de servicios.
        frame_encabezado_servicios = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_servicios.pack(side="top", fill="x")
        # H1
        H1_servicios = tk.Label(frame_encabezado_servicios, text="Servicios", font=("Segoe UI", 28), bg="#0C1A34", fg="white")
        H1_servicios.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_servicios, text="Catalogo de servicios disponibles", font=("Segoe UI", 14), bg="#0C1A34", fg="#DDE8FF")
        subtitulo.pack()

        # Aqui creo el frame con los botones para crear un servicio y ver su detalle.
        frame_botones_servicios = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_botones_servicios.pack(side="top", fill="x", pady=25)
        boton_crear_servicio = tk.Button(frame_botones_servicios, text="➕ Crear nuevo servicio", font=("Segoe UI", 16), bg="#0AA552", fg="white", activebackground="#2CF769", activeforeground="#022211", command=self.abrir_formulario_servicio)
        boton_crear_servicio.pack(side="left", padx=20)
        self.quitar_bordes_botones(boton_crear_servicio)
        boton_detalle = tk.Button(frame_botones_servicios, text="🔎 Ver detalle", font=("Segoe UI", 16), bg="#0060FD", fg="white", activebackground="#2CC8F7", activeforeground="#022211", command=self.ver_detalle_servicio)
        boton_detalle.pack(side="left", padx=10)
        self.quitar_bordes_botones(boton_detalle)

        # Aqui creo el frame que contiene la tabla de servicios.
        frame_lista_servicios = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_lista_servicios.pack(side="top", fill="both", expand=True)
        titulo_lista_servicios = tk.Label(frame_lista_servicios, text="📋 Lista de Servicios", font=("Segoe UI", 16), bg="#0060FD", fg="white")
        titulo_lista_servicios.pack(side="top", fill="x")
        columnas = ("id", "tipo", "nombre", "descripcion", "precio", "costo")
        self.tabla_servicios = ttk.Treeview(frame_lista_servicios, columns=columnas, show="headings")

        self.tabla_servicios.heading("id", text="ID")
        self.tabla_servicios.heading("tipo", text="Tipo")
        self.tabla_servicios.heading("nombre", text="Nombre")
        self.tabla_servicios.heading("descripcion", text="Descripción")
        self.tabla_servicios.heading("precio", text="Precio")
        self.tabla_servicios.heading("costo", text="Costo calculado")

        self.tabla_servicios.column("id", width=50)
        self.tabla_servicios.column("tipo", width=150)
        self.tabla_servicios.column("nombre", width=150)
        self.tabla_servicios.column("descripcion", width=230)
        self.tabla_servicios.column("precio", width=100)
        self.tabla_servicios.column("costo", width=120)

        self.tabla_servicios.pack(fill="both", expand=True, padx=20, pady=10)
        self.actualizar_tabla_servicios()

    def actualizar_tabla_servicios(self):
        """Esta funcion borra la tabla de servicios y la llena otra vez con la lista de servicios."""
        for fila in self.tabla_servicios.get_children():
            self.tabla_servicios.delete(fila)
        for servicio in self.lista_servicios:
            # El costo lo calcula cada servicio con su propio metodo calcular_costo.
            try:
                costo = "$" + f"{servicio.calcular_costo():,.0f}"
            except Exception:
                costo = "Error"
            self.tabla_servicios.insert("", "end", iid=servicio.identificador, values=(servicio.identificador, type(servicio).__name__, servicio.nombre, servicio.descripcion, "$" + f"{servicio.precio:,.0f}", costo))

    def ver_detalle_servicio(self):
        """Esta funcion muestra la informacion completa del servicio seleccionado usando mostrar_informacion_entidad."""
        seleccion = self.tabla_servicios.selection()
        if len(seleccion) == 0:
            messagebox.showwarning("Aviso", "Primero seleccione un servicio de la tabla")
            return
        for servicio in self.lista_servicios:
            if servicio.identificador == seleccion[0]:
                messagebox.showinfo("Detalle del servicio", servicio.mostrar_informacion_entidad())

    def abrir_formulario_servicio(self):
        """Esta funcion abre una ventana pequena con el formulario para crear un servicio."""
        formulario = tk.Toplevel(self.ventana_principal)
        formulario.title("Crear nuevo servicio")
        formulario.geometry("450x640")
        formulario.config(bg="#0C1A34")
        formulario.transient(self.ventana_principal)
        formulario.grab_set()

        # Lista desplegable para escoger el tipo de servicio.
        etiqueta_tipo = tk.Label(formulario, text="Tipo de servicio", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_tipo.pack(pady=(15, 0))
        combo_tipo = ttk.Combobox(formulario, values=["Reserva de sala", "Alquiler de equipo", "Asesoria especializada"], state="readonly", font=("Segoe UI", 14))
        combo_tipo.pack(padx=40, fill="x")
        combo_tipo.current(0)

        etiqueta_nombre = tk.Label(formulario, text="Nombre del servicio", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_nombre.pack(pady=(15, 0))
        entrada_nombre = tk.Entry(formulario, font=("Segoe UI", 14))
        entrada_nombre.pack(padx=40, fill="x")

        etiqueta_descripcion = tk.Label(formulario, text="Descripcion", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_descripcion.pack(pady=(15, 0))
        entrada_descripcion = tk.Entry(formulario, font=("Segoe UI", 14))
        entrada_descripcion.pack(padx=40, fill="x")

        etiqueta_precio = tk.Label(formulario, text="Precio", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_precio.pack(pady=(15, 0))
        entrada_precio = tk.Entry(formulario, font=("Segoe UI", 14))
        entrada_precio.pack(padx=40, fill="x")

        # Estos dos campos cambian segun el tipo de servicio.
        etiqueta_dato1 = tk.Label(formulario, text="Capacidad de personas", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_dato1.pack(pady=(15, 0))
        entrada_dato1 = tk.Entry(formulario, font=("Segoe UI", 14))
        entrada_dato1.pack(padx=40, fill="x")

        etiqueta_dato2 = tk.Label(formulario, text="Horas de la sala", font=("Segoe UI", 13), bg="#0C1A34", fg="white")
        etiqueta_dato2.pack(pady=(15, 0))
        entrada_dato2 = tk.Entry(formulario, font=("Segoe UI", 14))
        entrada_dato2.pack(padx=40, fill="x")

        def cambiar_etiquetas(evento):
            tipo = combo_tipo.get()
            entrada_dato2.config(state="normal")
            if tipo == "Reserva de sala":
                etiqueta_dato1.config(text="Capacidad de personas")
                etiqueta_dato2.config(text="Horas de la sala")
            elif tipo == "Alquiler de equipo":
                etiqueta_dato1.config(text="Cantidad de equipos")
                etiqueta_dato2.config(text="Dias de alquiler")
            else:
                # La asesoria solo necesita un dato (las horas), el otro campo se bloquea.
                etiqueta_dato1.config(text="Horas de asesoria")
                etiqueta_dato2.config(text="(No aplica)")
                entrada_dato2.delete(0, "end")
                entrada_dato2.config(state="disabled")
        combo_tipo.bind("<<ComboboxSelected>>", cambiar_etiquetas)

        def guardar_servicio():
            try:
                self.crear_servicio(combo_tipo.get(), entrada_nombre.get(), entrada_descripcion.get(), entrada_precio.get(), entrada_dato1.get(), entrada_dato2.get())
            except Exception as error:
                self.manejar_error(error)
            else:
                messagebox.showinfo("Servicio creado", "El servicio se creo correctamente")
                formulario.destroy()
                self.actualizar_tabla_servicios()

        boton_guardar = tk.Button(formulario, text="💾 Guardar servicio", font=("Segoe UI", 15), bg="#0AA552", fg="white", activebackground="#2CF769", activeforeground="#022211", command=guardar_servicio)
        boton_guardar.pack(pady=25)
        self.quitar_bordes_botones(boton_guardar)

    def mostrar_pestaña_reservas(self):
        self.limpiar_frame_principal()
        frame_encabezado_reservas = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_reservas.pack(side="top", fill="x")
        # H1
        H1_reservas = tk.Label(frame_encabezado_reservas, text="Reservas", font=("Segoe UI", 28), bg="#0C1A34", fg="white")
        H1_reservas.pack(pady=20)
        # subtitulo.
        subtitulo = tk.Label(frame_encabezado_reservas, text="Gestion de reservas", font=("Segoe UI", 14), bg="#0C1A34", fg="#DDE8FF")
        subtitulo.pack()

        # Aqui creo el frame de la primera fila del formulario: cliente, servicio y duracion.
        frame_formulario_fila1 = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_formulario_fila1.pack(side="top", fill="x", pady=(20, 5))

        label_cliente = tk.Label(frame_formulario_fila1, text="Cliente:", font=("Segoe UI", 14), bg="#0C1A34", fg="white")
        label_cliente.pack(side="left", padx=(20, 5))
        # Aqui lleno la lista desplegable con los clientes registrados.
        self.clientes_para_reserva = list(Cliente.clientes_registrados.values())
        nombres_clientes = []
        for cliente in self.clientes_para_reserva:
            nombres_clientes.append(cliente.identificador + " - " + cliente.nombre)
        self.combo_cliente_reserva = ttk.Combobox(frame_formulario_fila1, values=nombres_clientes, state="readonly", font=("Segoe UI", 13), width=20)
        self.combo_cliente_reserva.pack(side="left", padx=5)

        label_servicio = tk.Label(frame_formulario_fila1, text="Servicio:", font=("Segoe UI", 14), bg="#0C1A34", fg="white")
        label_servicio.pack(side="left", padx=(15, 5))
        # Aqui lleno la lista desplegable con los servicios creados.
        nombres_servicios = []
        for servicio in self.lista_servicios:
            nombres_servicios.append(servicio.identificador + " - " + servicio.nombre)
        self.combo_servicio_reserva = ttk.Combobox(frame_formulario_fila1, values=nombres_servicios, state="readonly", font=("Segoe UI", 13), width=20)
        self.combo_servicio_reserva.pack(side="left", padx=5)

        label_duracion = tk.Label(frame_formulario_fila1, text="Horas:", font=("Segoe UI", 14), bg="#0C1A34", fg="white")
        label_duracion.pack(side="left", padx=(15, 5))
        self.entrada_duracion_reserva = tk.Entry(frame_formulario_fila1, font=("Segoe UI", 14), width=5)
        self.entrada_duracion_reserva.pack(side="left", padx=5)

        # Aqui creo la segunda fila con los botones de crear, confirmar, procesar y cancelar.
        frame_formulario_fila2 = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_formulario_fila2.pack(side="top", fill="x", pady=(5, 15))

        boton_crear_reserva = tk.Button(frame_formulario_fila2, text="➕ Crear", font=("Segoe UI", 14), bg="#0AA552", fg="white", activebackground="#2CF769", activeforeground="#022211", command=self.crear_reserva_desde_pestaña)
        boton_crear_reserva.pack(side="left", padx=(20, 10))
        self.quitar_bordes_botones(boton_crear_reserva)
        boton_confirmar_reserva = tk.Button(frame_formulario_fila2, text="✅ Confirmar", font=("Segoe UI", 14), bg="#0060FD", fg="white", activebackground="#2CC8F7", activeforeground="#022211", command=lambda: self.accion_reserva_seleccionada("confirmar"))
        boton_confirmar_reserva.pack(side="left", padx=10)
        self.quitar_bordes_botones(boton_confirmar_reserva)
        boton_procesar_reserva = tk.Button(frame_formulario_fila2, text="⚙️ Procesar", font=("Segoe UI", 14), bg="#FAB903", fg="white", activebackground="#EEFF00", activeforeground="#090A00", command=lambda: self.accion_reserva_seleccionada("procesar"))
        boton_procesar_reserva.pack(side="left", padx=10)
        self.quitar_bordes_botones(boton_procesar_reserva)
        boton_cancelar_reserva = tk.Button(frame_formulario_fila2, text="❌ Cancelar", font=("Segoe UI", 14), bg="#F72C2F", fg="white", activebackground="#740505", activeforeground="#FCFCFC", command=lambda: self.accion_reserva_seleccionada("cancelar"))
        boton_cancelar_reserva.pack(side="left", padx=10)
        self.quitar_bordes_botones(boton_cancelar_reserva)

        # Aqui se crea la tabla con la lista de reservas.
        self.crear_tabla_reservas()

    def crear_tabla_reservas(self):
        # Este es el frame que contiene el titulo y la tabla de reservas.
        frame_lista_reservas = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_lista_reservas.pack(side="top", fill="both", expand=True)
        titulo_lista_reservas = tk.Label(frame_lista_reservas, text="📋 Lista de Reservas", font=("Segoe UI", 16), bg="#0060FD", fg="white")
        titulo_lista_reservas.pack(side="top", fill="x")
        columnas = ("id", "cliente", "servicio", "duracion", "estado")
        self.tabla_reservas = ttk.Treeview(frame_lista_reservas, columns=columnas, show="headings")

        self.tabla_reservas.heading("id", text="ID")
        self.tabla_reservas.heading("cliente", text="Cliente")
        self.tabla_reservas.heading("servicio", text="Servicio")
        self.tabla_reservas.heading("duracion", text="Horas")
        self.tabla_reservas.heading("estado", text="Estado")

        self.tabla_reservas.column("id", width=60)
        self.tabla_reservas.column("cliente", width=200)
        self.tabla_reservas.column("servicio", width=200)
        self.tabla_reservas.column("duracion", width=80)
        self.tabla_reservas.column("estado", width=130)

        self.tabla_reservas.pack(fill="both", expand=True, padx=20, pady=10)
        self.actualizar_tabla_reservas()

    def actualizar_tabla_reservas(self):
        """Esta funcion borra la tabla de reservas y la llena otra vez con la lista de reservas."""
        for fila in self.tabla_reservas.get_children():
            self.tabla_reservas.delete(fila)
        for reserva in self.lista_reservas:
            self.tabla_reservas.insert("", "end", iid=reserva.identificador, values=(reserva.identificador, reserva.cliente.nombre, reserva.servicio.nombre, reserva.duracion, reserva.estado))

    def crear_reserva_desde_pestaña(self):
        """Esta funcion toma los datos del formulario de reservas y crea la reserva."""
        try:
            if self.combo_cliente_reserva.current() == -1 or self.combo_servicio_reserva.current() == -1:
                raise excepciones.ReservaInvalidaError("Debe seleccionar un cliente y un servicio")
            cliente = self.clientes_para_reserva[self.combo_cliente_reserva.current()]
            servicio = self.lista_servicios[self.combo_servicio_reserva.current()]
            self.crear_reserva(cliente, servicio, self.entrada_duracion_reserva.get())
        except Exception as error:
            self.manejar_error(error)
        else:
            messagebox.showinfo("Reserva creada", "La reserva se creo correctamente")
            self.entrada_duracion_reserva.delete(0, "end")
        finally:
            self.actualizar_tabla_reservas()

    def accion_reserva_seleccionada(self, accion):
        """Esta funcion confirma, procesa o cancela la reserva que este seleccionada en la tabla."""
        seleccion = self.tabla_reservas.selection()
        if len(seleccion) == 0:
            messagebox.showwarning("Aviso", "Primero seleccione una reserva de la tabla")
            return
        try:
            for reserva in self.lista_reservas:
                if reserva.identificador == seleccion[0]:
                    if accion == "confirmar":
                        reserva.confirmar()
                    elif accion == "procesar":
                        reserva.procesar()
                    elif accion == "cancelar":
                        reserva.cancelar()
        except Exception as error:
            self.manejar_error(error)
        else:
            messagebox.showinfo("Reserva", "La accion '" + accion + "' se realizo correctamente")
        finally:
            self.actualizar_tabla_reservas()


    def mostrar_pestaña_logs(self):
        self.limpiar_frame_principal()
        frame_encabezado_logs = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_logs.pack(side="top", fill="x")
        # H1
        H1_logs = tk.Label(frame_encabezado_logs, text="Logs", font=("Segoe UI", 28), bg="#0C1A34", fg="white")
        H1_logs.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_logs, text="Historial de eventos y errores", font=("Segoe UI", 14), bg="#0C1A34", fg="#DDE8FF")
        subtitulo.pack()
        # Este boton vuelve a cargar el archivo de logs para ver los eventos nuevos.
        boton_actualizar_logs = tk.Button(self.frame_principal, text="🔄 Actualizar logs", font=("Segoe UI", 14), bg="#0060FD", fg="white", activebackground="#2CC8F7", activeforeground="#022211", command=self.mostrar_pestaña_logs)
        boton_actualizar_logs.pack(side="top", pady=10)
        self.quitar_bordes_botones(boton_actualizar_logs)
        # Aqui se crea el cuadro donde se muestra el contenido del archivo de logs.
        self.crear_tabla_logs()

    def crear_tabla_logs(self):
        # Este frame contiene el cuadro de texto y la barra de desplazamiento.
        frame_texto_logs = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_texto_logs.pack(side="top", fill="both", expand=True, padx=20, pady=10)
        barra_scroll = tk.Scrollbar(frame_texto_logs)
        barra_scroll.pack(side="right", fill="y")
        texto_logs = tk.Text(frame_texto_logs, font=("Consolas", 11), bg="#10264E", fg="white", wrap="none", yscrollcommand=barra_scroll.set)
        texto_logs.pack(side="left", fill="both", expand=True)
        barra_scroll.config(command=texto_logs.yview)
        # Estos son los colores para los errores, las advertencias y los mensajes debug.
        texto_logs.tag_config("error", foreground="#FF6B6B")
        texto_logs.tag_config("warning", foreground="#FAB903")
        texto_logs.tag_config("debug", foreground="#8FA3C7")

        # Aqui leo el archivo de logs que configuro logger_config, si no se puede leer muestro un mensaje.
        archivo = None
        lineas = []
        try:
            archivo = open(logger_configuracion.nombre_archivo_log, "r", encoding="utf-8")
            lineas = archivo.readlines()
        except OSError:
            lineas = ["Todavia no hay eventos registrados.\n"]
        finally:
            if archivo is not None:
                archivo.close()

        for linea in lineas:
            if " - ERROR - " in linea:
                texto_logs.insert("end", linea, "error")
            elif " - WARNING - " in linea:
                texto_logs.insert("end", linea, "warning")
            elif " - DEBUG - " in linea:
                texto_logs.insert("end", linea, "debug")
            else:
                texto_logs.insert("end", linea)
        texto_logs.see("end")
        texto_logs.config(state="disabled")  # Asi el usuario no puede escribir en el cuadro.

    # Estas funciones son de apoyo
    def manejar_error(self, error, mostrar=True):
        """Esta funcion guarda el error en el log y, si mostrar es True, avisa al usuario con una ventana. El programa nunca se cierra."""
        mensaje = type(error).__name__ + ": " + str(error)
        if error.__cause__ is not None:
            mensaje = mensaje + " | Causa: " + type(error.__cause__).__name__ + ": " + str(error.__cause__)
        logger.error("[Interfaz] " + mensaje)
        if mostrar:
            if isinstance(error, excepciones.SoftwareFJError):
                texto = str(error)
                if error.__cause__ is not None:
                    texto = texto + "\nMotivo: " + str(error.__cause__)
            else:
                texto = "Ocurrio un error inesperado: " + str(error)
            messagebox.showerror("Error", texto)

    def convertir_numero(self, texto, nombre_campo, entero=True, solo_positivo=True):
        """Esta funcion convierte el texto de un campo a numero. Si no se puede lanza DatoInvalidoError encadenado con el error original."""
        try:
            if entero:
                numero = int(texto)
            else:
                numero = float(texto)
        except (ValueError, TypeError) as error:
            raise excepciones.DatoInvalidoError("El campo " + nombre_campo + " debe ser un numero valido") from error
        if solo_positivo and numero <= 0:
            raise excepciones.DatoInvalidoError("El campo " + nombre_campo + " debe ser mayor a 0")
        return numero

    def crear_servicio(self, tipo, nombre, descripcion, precio, dato1, dato2):
        """Esta funcion crea un servicio del tipo que se pida y lo guarda en la lista de servicios."""
        # El precio negativo no lo reviso aqui, lo revisa la clase Servicio.
        precio = self.convertir_numero(precio, "precio", False, False)
        identificador = "S" + str(len(self.lista_servicios) + 1)
        if tipo == "Reserva de sala":
            capacidad = self.convertir_numero(dato1, "capacidad")
            horas = self.convertir_numero(dato2, "horas")
            nuevo_servicio = servicios.ReservaDeSalas(identificador, nombre, descripcion, precio, capacidad, horas)
        elif tipo == "Alquiler de equipo":
            cantidad = self.convertir_numero(dato1, "cantidad de equipos")
            dias = self.convertir_numero(dato2, "dias de alquiler")
            nuevo_servicio = servicios.AlquilerDeEquipos(identificador, nombre, descripcion, precio, cantidad, dias)
        elif tipo == "Asesoria especializada":
            horas = self.convertir_numero(dato1, "horas de asesoria")
            nuevo_servicio = servicios.AsesoriasEspecializadas(identificador, nombre, descripcion, precio, horas)
        else:
            raise excepciones.ServicioNoEncontradoError("El tipo de servicio no existe")
        self.lista_servicios.append(nuevo_servicio)
        logger.info("Servicio creado: " + identificador + " - " + nuevo_servicio.nombre + " (" + tipo + ")")
        return nuevo_servicio

    def crear_reserva(self, cliente, servicio, duracion):
        """Esta funcion crea una reserva y la guarda en la lista de reservas."""
        duracion = self.convertir_numero(duracion, "duracion (horas)")
        identificador = "R" + str(len(self.lista_reservas) + 1)
        nueva_reserva = Reserva(identificador, cliente, servicio, duracion)
        self.lista_reservas.append(nueva_reserva)
        logger.info("Reserva creada: " + identificador)
        return nueva_reserva

    def quitar_bordes_botones(self, boton):
        """Esta funcion quita los bordes a los botones"""
        boton.config(bd=0, highlightthickness=0, relief="flat")

    def configurar_efectos_hover(self, boton):
        """Esta funcion configura los efectos hover para los botones de la barra lateral izquierda. Cuando el mouse pasa por encima del boton, el color de fondo cambia a un azul mas oscuro. Cuando el mouse sale del boton, el color de fondo vuelve a su color original."""
        boton.bind("<Enter>", lambda e: boton.config(bg="#1F3C6E"))
        boton.bind("<Leave>", lambda e: boton.config(bg="#10264E"))

    def lanzar_interfaz(self):
        """Esta funcion lanza la interfaz grafica del software. Es la funcion que se llama desde el script principal main.py para iniciar el programa."""
        self.ventana_principal.mainloop()

      