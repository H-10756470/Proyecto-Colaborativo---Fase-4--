from abc import ABC, abstractmethod

class EntidadBasica(ABC): 
    """Esta clase abstracta sirve de base para todas las entidades del sistema, entidades como la clase Cliente, La clase Reserva y la clase Servicio."""

    def __init__(self, identificador):
        self.identificador = identificador

    @property
    def identificador(self) -> str:
        """Este es un getter que retorna el identificador de la entidad."""
        return self._identificador

    @identificador.setter
    def identificador(self, id_nuevo: str):
        """Este es un setter que permite cambiar el identificador de la entidad."""
        if not isinstance(id_nuevo, str):
            raise ValueError("El identificador debe ser una cadena de texto.")
        self._identificador = id_nuevo

    @abstractmethod
    def mostrar_informacion_entidad(self):
        """Este metodo abstracto debe ser implementado por todas las clases hijas que hereden de EntidadBasica. Su funcion es mostrar la informacion de la entidad."""
        pass

    @abstractmethod
    def actualizar_informacion_entidad(self, **kwargs):
        """Este metodo abstracto debe ser implementado por todas las clases hijas que hereden de EntidadBasica. Su funcion es actualizar la informacion de la entidad."""
        pass