import tkinter as tk
from tkinter import ttk
class SoftwareFJInterfaz:
    def __init__(self, ventana_principal): 
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Software FJ")
        self.ventana_principal.state('zoomed')  # Esto hace que la ventana sea de pantalla completa, sin ocultar la barra de tareas
        self.ventana_principal.minsize(800, 600)  # Tamaño mínimo de la ventana
        self.ventana_principal.config(bg="#1e1e1e")  # Este es el color de fondo oscuro.

        # Esto permite que la ventana y sus widgets se ajusten al tamaño de pantalla del dispositivo donde se ejecute el programa, haciendo que la interfaz sea responsiva.
        self.ventana_principal.rowconfigure(0, weight=1)
        self.ventana_principal.columnconfigure(0, weight=1)

        # Contenedor principal adaptable
        main_frame = tk.Frame(self.ventana_principal, bg="#1e1e1e")
        main_frame.grid(row=0, column=0, sticky="nsew") # Esto hace que el contenedor principal se expanda para llenar toda la ventana.

        # Aqui se configuran las filas del contenedor principal para que se ajusten al tamaño de la ventana.
        main_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=0)
        main_frame.columnconfigure(0, weight=1)

        titulo = tk.Label(main_frame, text="Panel Adaptable - Software FJ", bg="#1e1e1e", fg="white", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, pady=20)
        
        

if __name__ == "__main__":
    root = tk.Tk()
    app = SoftwareFJInterfaz(root)
    root.mainloop()   


      