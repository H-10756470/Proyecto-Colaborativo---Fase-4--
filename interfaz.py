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
            activebackground="#162B50",
            activeforeground="white"
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
            activebackground="#162B50",
            activeforeground="white",
            command=self.mostrar_clientes  # Este comando llama a la funcion mostrar_clientes cuando se presiona el boton Clientes.
        )
        self.boton_clientes.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_clientes)  # Configuro los efectos hover para el boton Clientes.

        self.boton_servicios = tk.Button(
            self.menu, text="Servicios", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20
        )
        self.boton_servicios.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_servicios)  # Configuro los efectos hover para el boton Servicios.

        self.boton_reservas = tk.Button(
            self.menu, text="Reservas", 
            font=("Arial", 14), 
            bg="#0C1A34", 
            fg="white", 
            anchor="w", 
            padx=20  
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
            padx=20
        )  
        self.boton_logs.pack(fill="x", pady=3)
        self.configurar_efectos_hover(self.boton_logs)  # Configuro los efectos hover para el boton Logs.

        # Aqui creo el label de la parte inferior para mostrar el logotipo de Software Fj.
        self.label_logotipo = tk.Label(self.barra_lateral_izquierda, text="Software FJ", font=("Arial", 12), bg="#0C1A34", fg="white")
        self.label_logotipo.pack(side="bottom", fill="x")

    def mostrar_clientes(self):
        self.titulo_clientes = tk.Label(self.frame_principal, text="Clientes", font=("Arial", 24), bg="#0C1A34", fg="white")
        self.titulo_clientes.pack(pady=20)
        
    def configurar_efectos_hover(self, boton):
        """Esta funcion configura los efectos hover para los botones de la barra lateral izquierda. Cuando el mouse pasa por encima del boton, el color de fondo cambia a un azul mas oscuro. Cuando el mouse sale del boton, el color de fondo vuelve a su color original."""
        boton.bind("<Enter>", lambda e: boton.config(bg="#162B50"))
        boton.bind("<Leave>", lambda e: boton.config(bg="#0C1A34"))

    def lanzar_interfaz(self):
        """Esta funcion lanza la interfaz grafica del software. Es la funcion que se llama desde el script principal main.py para iniciar el programa."""
        self.ventana_principal.mainloop()       

   

      