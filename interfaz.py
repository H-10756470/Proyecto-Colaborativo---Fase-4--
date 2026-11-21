import tkinter as tk

# Esta clase es para crear la ventana principal de Software FJ.
class SoftwareFJInterfaz:
    def __init__(self, ventana_principal): 
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Software FJ - Sistema de Gestion")
        self.ventana_principal.state('zoomed')  # Esto hace que la ventana sea de pantalla completa pero sin ocultar la barra de tareas.
        self.ventana_principal.minsize(800, 600)  # Tamaño mínimo de la ventana
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
        self.barra_lateral_izquierda = tk.Frame(self.ventana_principal, bg="#0C1A34", width=200)
        self.barra_lateral_izquierda.pack(side="left", fill="y")
        self.barra_lateral_izquierda.pack_propagate(False)  # Esto evita que la barra lateral se ajuste automáticamente al tamaño de sus widgets internos.

        # Aqui dentro del frame menu, creo los botones Inicio, Clientes, Servicios, Reservas y Logs. Estos botones seran los que permitan navegar entre las diferentes secciones del software.
        self.menu = tk.Frame(self.barra_lateral_izquierda, bg="#0C1A34")
        self.menu.pack(fill="both", expand=True)

        self.boton_inicio = tk.Button(
            self.menu, text="Inicio", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20,
            command= self.mostrar_pestaña_inicio  # Este comando llama a la funcion mostrar_inicio cuando se presiona el boton Inicio.
        )
        self.boton_inicio.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_inicio)  # Configuro los efectos hover para el boton Inicio.

        self.boton_clientes = tk.Button(
            self.menu, 
            text="Clientes", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20,
            command=self.mostrar_pestaña_clientes  # Este comando llama a la funcion mostrar_clientes cuando se presiona el boton Clientes.
        )
        self.boton_clientes.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_clientes)  # Configuro los efectos hover para el boton Clientes.

        self.boton_servicios = tk.Button(
            self.menu, text="Servicios", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20,
            command=self.mostrar_pestaña_servicios  # Este comando llama a la funcion mostrar_servicios cuando se presiona el boton Servicios.
        )
        self.boton_servicios.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_servicios)  # Configuro los efectos hover para el boton Servicios.

        self.boton_reservas = tk.Button(
            self.menu, text="Reservas", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20,
            command=self.mostrar_pestaña_reservas  # Este comando llama a la funcion mostrar_reservas cuando se presiona el boton Reservas.
        )
        self.boton_reservas.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_reservas)  # Configuro los efectos hover para el boton Reservas.

        self.boton_logs = tk.Button(
            self.menu, 
            text="Logs", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20,
            command=self.mostrar_pestaña_logs  # Este comando llama a la funcion mostrar_logs cuando se presiona el boton Logs.
        )  
        self.boton_logs.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_logs)  # Configuro los efectos hover para el boton Logs.

        # Aqui creo el label de la parte inferior para mostrar el logotipo de Software Fj.
        self.label_logotipo = tk.Label(self.barra_lateral_izquierda, text="Software FJ", font=("Arial", 12), bg="#0C1A34", fg="white")
        self.label_logotipo.pack(side="bottom", fill="x")

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
        H1_inicio = tk.Label(frame_encabezado_inicio, text="Panel Principal - Software FJ", font=("Arial", 24), bg="#0C1A34", fg="white")
        H1_inicio.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_inicio, text="Gestion de clientes, servicios y reservas", font=("Arial", 14), bg="#0C1A34", fg="white")
        subtitulo.pack()
        # Frame padre de los botones "Gestionar Clientes", "Gestionar Servicios", "Gestionar Reservas" y "Eventos y Logs"
        frame_botones = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_botones.pack(side="top", fill="x")
        # Boton "Gestionar Clientes"
        boton_gestionar_clientes = tk.Button(frame_botones, text="Gestionar Clientes", font=("Arial", 30), bg="#0060FD", fg="white", command=self.mostrar_pestaña_clientes)
        boton_gestionar_clientes.pack(side="left", padx=10, pady=20)
        # Boton "Gestionar Servicios"
        boton_gestionar_servicios = tk.Button(frame_botones, text="Gestionar Servicios", font=("Arial", 30), bg="#0BB158", fg="white", command=self.mostrar_pestaña_servicios)
        boton_gestionar_servicios.pack(side="left", padx=10, pady=20)
        # Boton "Gestionar Reservas"
        boton_gestionar_reservas = tk.Button(frame_botones, text="Gestionar Reservas", font=("Arial", 30), bg="#FAB903", fg="white", command=self.mostrar_pestaña_reservas)
        boton_gestionar_reservas.pack(side="left", padx=10, pady=20)
        # Boton "Eventos y Logs"
        boton_Eventos = tk.Button(frame_botones, text="Eventos y Logs", font=("Arial", 30), bg="#F72C2F", fg="white", command=self.mostrar_pestaña_logs)
        boton_Eventos.pack(side="left", padx=10, pady=20)

    def mostrar_pestaña_clientes(self):
        self.limpiar_frame_principal()
        # Aqui creo el encabezado de la pestaña Clientes, que incluye un H1 y un subtitulo.
        frame_encabezado_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_clientes.pack(side="top", fill="x")
        # Aqui creo el H1 y el subtitulo de la pestaña Clientes.
        H1_clientes = tk.Label(frame_encabezado_clientes, text="Clientes", font=("Arial", 24), bg="#0C1A34", fg="white")
        H1_clientes.pack(pady=20)
        subtitulo_clientes = tk.Label(frame_encabezado_clientes, text="Gestion de clientes", font=("Arial", 14), bg="#0C1A34", fg="white")
        subtitulo_clientes.pack() 
        # Aqui creo el frame de busqueda de clientes, que incluye un campo de texto, un boton de busqueda y un boton para registrar clientes.
        frame_busqueda_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_busqueda_clientes.pack(side="top", fill="x")
        # Aqui creo el campo para buscar a un cliente registrado, creo el boton "Buscar" y "registrar cliente".
        campo_buscar_cliente = tk.Entry(frame_busqueda_clientes, font=("Arial", 12), width=30)
        campo_buscar_cliente.pack(side="left", padx=20, pady=10)
        campo_buscar_cliente.insert(0, "Ingrese la identificacion del cliente...")  # Texto de ejemplo en el campo de búsqueda

        boton_buscar_cliente = tk.Button(frame_busqueda_clientes, text="Buscar", font=("Arial", 12), bg="#0C1A34", fg="white")
        boton_buscar_cliente.pack(side="left")

        registrar_nuevo_cliente = tk.Button(frame_busqueda_clientes, text="+ Registrar nuevo cliente", font=("Arial", 12), bg="#0C1A34", fg="white")
        registrar_nuevo_cliente.pack(side="left")

        # Aqui creo el frame que contendra la lista de registro de todos los clientes.
        frame_lista_clientes = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_lista_clientes.pack(side="top", fill="both", expand=True)
        # este es el titulo de la lista que muestra todos los clientes registrados en el sistema
        titulo_lista_clientes = tk.Label(frame_lista_clientes, text="Lista de Clientes Registrados", font=("Arial", 12), bg="#0C1A34", fg="white" )
        titulo_lista_clientes.pack(side="top", fill="x")


    def mostrar_pestaña_servicios(self):
        self.limpiar_frame_principal()
        # Este es el frame donde iran el H1 y el subtitulo de servicios.
        frame_encabezado_servicios = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_servicios.pack(side="top", fill="x")
        # H1
        H1_servicios = tk.Label(frame_encabezado_servicios, text="Servicios", font=("Arial", 24), bg="#0C1A34", fg="white")
        H1_servicios.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_servicios, text="Catalogo de servicios disponibles", font=("Arial", 14), bg="#0C1A34", fg="white")
        subtitulo.pack()


    def mostrar_pestaña_reservas(self):
        self.limpiar_frame_principal()
        frame_encabezado_reservas = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_reservas.pack(side="top", fill="x")
        # H1
        H1_reservas = tk.Label(frame_encabezado_reservas, text="Reservas", font=("Arial", 24), bg="#0C1A34", fg="white")
        H1_reservas.pack(pady=20)
        # subtitulo.
        subtitulo = tk.Label(frame_encabezado_reservas, text="Gestion de reservas", font=("Arial", 14), bg="#0C1A34", fg="white")
        subtitulo.pack()


    def mostrar_pestaña_logs(self):
        self.limpiar_frame_principal()
        frame_encabezado_logs = tk.Frame(self.frame_principal, bg="#0C1A34")
        frame_encabezado_logs.pack(side="top", fill="x")
        # H1
        H1_logs = tk.Label(frame_encabezado_logs, text="Logs", font=("Arial", 24), bg="#0C1A34", fg="white")
        H1_logs.pack(pady=20)
        # Subtitulo
        subtitulo = tk.Label(frame_encabezado_logs, text="Historial de eventos y errores", font=("Arial", 14), bg="#0C1A34", fg="white")
        subtitulo.pack()


    def configurar_efectos_hover(self, boton):
        """Esta funcion configura los efectos hover para los botones de la barra lateral izquierda. Cuando el mouse pasa por encima del boton, el color de fondo cambia a un azul mas oscuro. Cuando el mouse sale del boton, el color de fondo vuelve a su color original."""
        boton.bind("<Enter>", lambda e: boton.config(bg="#162B50"))
        boton.bind("<Leave>", lambda e: boton.config(bg="#0C1A34"))

    def lanzar_interfaz(self):
        """Esta funcion lanza la interfaz grafica del software. Es la funcion que se llama desde el script principal main.py para iniciar el programa."""
        self.ventana_principal.mainloop()       

   

      