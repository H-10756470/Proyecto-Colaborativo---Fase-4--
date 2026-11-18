from modelos_base import EntidadBasica


class Cliente(EntidadBasica):
    """Clase que representa a un cliente en Software FJ con encapsulación básica."""

    def __init__(self, identificador: str, nombre: str, telefono: str, correo: str = ""):
        # Inicializamos la clase padre y los atributos encapsulados
        super().__init__(identificador)
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo

#---ENCAPSULACIÓN
