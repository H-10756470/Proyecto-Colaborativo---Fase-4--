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

    @property
    def nombre(self) -> str:
        """Getter que retorna el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Setter que permite actualizar el nombre del cliente."""
        self._nombre = valor

    @property
    def telefono(self) -> str:
        """Getter que retorna el teléfono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        """Setter que permite actualizar el teléfono del cliente."""
        self._telefono = valor

    @property
    def correo(self) -> str:
        """Getter que retorna el correo del cliente."""
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        """Setter que permite actualizar el correo del cliente."""
        self._correo = valor

    def mostrar_informacion_entidad(self) -> str:
        """Implementación del método abstracto para mostrar los datos del cliente."""
        return f"Cliente [{self.identificador}]: {self.nombre} | Tel: {self.telefono} | Correo: {self.correo}"

    def actualizar_informacion_entidad(self, **kwargs):
        """Implementación del método abstracto para modificar los datos del cliente."""
        for clave, valor in kwargs.items():
            # Verificamos que el atributo exista en el cliente y no sea nulo antes de actualizar
            if hasattr(self, clave) and valor is not None:
                setattr(self, clave, valor)
