import tkinter as tk

# Esta clase es para crear la ventana principal de Software FJ.
class SoftwareFJInterfaz:
    def __init__(self, ventana_principal): 
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Software FJ - Sistema de Gestion de Clientes, Servicios y Reservas")
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

        self.boton_inicio = tk.Button(self.menu, text="Inicio", font=("Arial", 14), bg="#0C1A34", fg="white")
        self.boton_inicio.pack(fill="x")

        self.boton_clientes = tk.Button(self.menu, text="Clientes", font=("Arial", 14), bg="#0C1A34", fg="white")
        self.boton_clientes.pack(fill="x")

        self.boton_servicios = tk.Button(self.menu, text="Servicios", font=("Arial", 14), bg="#0C1A34", fg="white")
        self.boton_servicios.pack(fill="x")

        self.boton_reservas = tk.Button(self.menu, text="Reservas", font=("Arial", 14), bg="#0C1A34", fg="white")
        self.boton_reservas.pack(fill="x")

        self.boton_logs = tk.Button(self.menu, text="Logs", font=("Arial", 14), bg="#0C1A34", fg="white")
        self.boton_logs.pack(fill="x")

    def lanzar_interfaz(self):
        self.ventana_principal.mainloop()       

   

      