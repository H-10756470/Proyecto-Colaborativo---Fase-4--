import tkinter as tk
from tkinter import ttk, messagebox
import os
from logger_config import logger
from excepciones import ClienteIdentificacionError

class AppSoftwareFJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión - Software FJ (Fase 4)")
        self.root.geometry("750x500")
        self.root.config(bg="#f0f2f5")

        # Configurar estilo general
        self.style = ttk.Style()
        self.style.theme_use("clam")

        logger.info("Interfaz gráfica Tkinter iniciada correctamente.")

        # Construir componentes visuales
        self.crear_encabezado()
        self.crear_pestanas()

    def crear_encabezado(self):
        """Crea un título superior elegante para el sistema."""
        header_frame = tk.Frame(self.root, bg="#1e293b", height=60)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        titulo = tk.Label(
            header_frame, 
            text="SISTEMA DE GESTIÓN INTELIGENTE - SOFTWARE FJ", 
            bg="#1e293b", 
            fg="white", 
            font=("Arial", 14, "bold")
        )
        titulo.pack(pady=15)

    def crear_pestanas(self):
        """Crea un sistema de pestañas organizado para cada módulo."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Pestañas individuales
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_reservas = ttk.Frame(self.notebook)
        self.tab_logs = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_clientes, text="👤 Clientes")
        self.notebook.add(self.tab_servicios, text="🛠️ Servicios")
        self.notebook.add(self.tab_reservas, text="📅 Reservas")
        self.notebook.add(self.tab_logs, text="📋 Bitácora (Logs)")

        # Inicializar contenido de cada pestaña
        self.cargar_seccion_clientes()
        self.cargar_seccion_servicios()
        self.cargar_seccion_reservas()
        self.cargar_seccion_logs()

    def cargar_seccion_clientes(self):
        """Diseño del módulo de gestión de clientes."""
        label = tk.Label(self.tab_clientes, text="Registro y Control de Clientes", font=("Arial", 12, "bold"), fg="#333")
        label.pack(pady=10)

        form_frame = tk.Frame(self.tab_clientes, bg="white", padx=20, pady=20)
        form_frame.pack(padx=20, pady=10, fill=tk.X)

        tk.Label(form_frame, text="Cédula / Identificador:", bg="white", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.txt_cedula = ttk.Entry(form_frame, width=30)
        self.txt_cedula.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(form_frame, text="Nombre Completo:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.txt_nombre = ttk.Entry(form_frame, width=30)
        self.txt_nombre.grid(row=1, column=1, padx=10, pady=5)

        btn_guardar = tk.Button(
            form_frame, 
            text="Registrar Cliente", 
            bg="#2563eb", 
            fg="white", 
            font=("Arial", 10, "bold"),
            command=self.registrar_cliente_accion
        )
        btn_guardar.grid(row=2, column=0, columnspan=2, pady=15)

    def registrar_cliente_accion(self):
        """Acción simulada para registrar cliente usando validación y logs."""
        cedula = self.txt_cedula.get().strip()
        nombre = self.txt_nombre.get().strip()

        try:
            if not cedula or not nombre:
                raise ClienteInvalidoError("Los campos de cédula y nombre no pueden estar vacíos.")
            
            logger.info(f"Cliente registrado con éxito vía GUI: {nombre} (ID: {cedula})")
            messagebox.showinfo("Éxito", f"Cliente {nombre} registrado correctamente.")
            
            # Limpiar campos
            self.txt_cedula.delete(0, tk.END)
            self.txt_nombre.delete(0, tk.END)

        except ClienteIdentificacionError as e:
            logger.warning(f"Fallo en registro de cliente: {e}")
            messagebox.showerror("Error de Validación", str(e))

    def cargar_seccion_servicios(self):
        """Diseño del módulo de servicios."""
        tk.Label(self.tab_servicios, text="Catálogo de Servicios Disponibles", font=("Arial", 12, "bold"), fg="#333").pack(pady=20)
        tk.Label(self.tab_servicios, text="Aquí se listarán los servicios especializados del sistema.", font=("Arial", 10), fg="#666").pack()

    def cargar_seccion_reservas(self):
        """Diseño del módulo de reservas."""
        tk.Label(self.tab_reservas, text="Gestión de Reservas y Operaciones", font=("Arial", 12, "bold"), fg="#333").pack(pady=20)
        tk.Label(self.tab_reservas, text="Módulo para procesar y confirmar reservas.", font=("Arial", 10), fg="#666").pack()

    def cargar_seccion_logs(self):
        """Diseño del visor de logs del sistema."""
        frame_logs = tk.Frame(self.tab_logs, padx=10, pady=10)
        frame_logs.pack(fill=tk.BOTH, expand=True)

        btn_actualizar = tk.Button(frame_logs, text="🔄 Actualizar Vista de Logs", command=self.actualizar_texto_logs)
        btn_actualizar.pack(anchor="w", pady=5)

        self.txt_logs = tk.Text(frame_logs, wrap=tk.WORD, height=15, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9))
        self.txt_logs.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.actualizar_texto_logs()

    def actualizar_texto_logs(self):
        """Lee el archivo sistema.log y lo muestra en tiempo real en la interfaz."""
        self.txt_logs.delete("1.0", tk.END)
        if os.path.exists("sistema.log"):
            with open("sistema.log", "r", encoding="utf-8") as f:
                contenido = f.read()
                self.txt_logs.insert(tk.END, contenido if contenido else "El archivo de log está vacío.")
        else:
            self.txt_logs.insert(tk.END, "Aún no se ha generado ningún registro en sistema.log.")

# Código de ejecución principal de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = AppSoftwareFJ(root)
    root.mainloop()