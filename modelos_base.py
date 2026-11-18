from abc import ABC, abstractmethod

class EntidadBasica(ABC): 
    """Esta clase abstracta sirve como base para todas las entidades del sistema, entidades como la clase Cliente, La clase Reserva y la clase Servicio."""
    # Este constructor permite dar un identificador unico en casos en que sea nesesario. 
    # Por ejemplo, en la clase Cliente, el identificador unico es la cedula del cliente. 
    # En la clase Servicio, el identificador unico es el nombre del servicio o un codigo alfanumerico que lo represente. 
    # En la clase Reserva, el identificador unico es un numero de reserva generado automaticamente.
    def __init__(self, identificador: str):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador debe ser una cadena de texto.")
        else:
            self._identificador = identificador

    @property
    def identificador(self) -> str:
        """Este es un getter que retorna el identificador de la entidad."""
        return self._identificador

    @identificador.setter
    def identificador(self, id_nuevo: str):
        """Este es un setter que permite cambiar el identificador de la entidad."""
        if not isinstance(id_nuevo, str) or not id_nuevo.strip():
            raise ValueError("El identificador debe ser una cadena de texto.")
        self._identificador = id_nuevo

    @abstractmethod
    def mostrar_informacion_entidad(self):
        """Este metodo abstracto debe ser implementado por todas las clases hijas que hereden de EntidadBasica. Su funcion es mostrar la informacion de la entidad (clientes, servicios o reservas)."""
        pass

    @abstractmethod
    def actualizar_informacion_entidad(self, **kwargs):
        """Este metodo abstracto debe ser implementado por todas las clases hijas que hereden de EntidadBasica. Su funcion es actualizar la informacion de la entidad."""
        pass