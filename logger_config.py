import logging
import os

class ConfiguradorLogger:
    """En esta clase se configura el logger para Software FJ. Aqui defino el formato de los logs, el nivel de log y creo el archivo donde se guardaran los logs."""

    def __init__(self, nombre_archivo_log='software_fj.log', nivel_log=logging.DEBUG):
        self.nombre_archivo_log = nombre_archivo_log
        self.nivel_log = nivel_log

    def configurar_logger(self):
        """Configura el logger con el formato y nivel especificados."""
        # Aqui creo el logger
        self.logger = logging.getLogger('SoftwareFJ')
        self.logger.setLevel(self.nivel_log)

        # Aqui creo el manejador de archivo para guardar los logs en un archivo.
        # Si el archivo de log ya existe, se sobreescribe.
        file_handler = logging.FileHandler(self.nombre_archivo_log)
        file_handler.setLevel(self.nivel_log)

        # Aqui defino el formato de los logs.
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Aqui agrego el manejador al logger.
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """Este metodo devuelve el logger que configuré y creé."""
        return self.logger

logger_configuracion = ConfiguradorLogger()
logger_configuracion.configurar_logger()
logger = logger_configuracion.get_logger()