# Importamos la clase abstracta base creada en la Parte A
from modelos_base import EntidadBasica


class Cliente(EntidadBasica):
    """Esta clase representa a un cliente del sistema Software FJ y hereda de EntidadBasica."""

    def __init__(self, identificador: str, nombre: str, telefono: str, correo: str = ""):
        # Llamamos al constructor de la clase padre para guardar el identificador
        super().__init__(identificador)
        # Guardamos los datos personales de forma encapsulada
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
