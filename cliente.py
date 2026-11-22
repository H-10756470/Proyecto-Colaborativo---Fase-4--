# 1. AGREGAMOS LAS IMPORTACIONES QUE FALTABAN
from modelos_base import EntidadBasica
from excepciones import ClienteIdentificacionError
from logger_config import logger


class Cliente(EntidadBasica):
    """Esta clase representa a un cliente del sistema Software FJ y hereda de EntidadBasica."""

    # 2. AGREGAMOS EL DICCIONARIO PARA GUARDAR LOS CLIENTES REGISTRADOS
    clientes_registrados = {}

    def __init__(self, identificador: str, nombre: str, telefono: str, correo: str = ""):
        # 3. AGREGAMOS TRY/EXCEPT Y VALIDACIÓN DE ID EN EL CONSTRUCTOR
        try:
            if not isinstance(identificador, str) or not identificador.strip().isdigit():
                raise ClienteIdentificacionError("La cédula/ID debe ser texto numérico y no estar vacía.")

            id_limpio = identificador.strip()
            if id_limpio in Cliente.clientes_registrados:
                raise ClienteIdentificacionError(f"Ya existe un cliente registrado con el ID {id_limpio}.")

            super().__init__(id_limpio)
            # Al asignar con self.nombre = nombre se ejecutan las validaciones de los setters
            self.nombre = nombre
            self.telefono = telefono
            self.correo = correo

            # Guardamos el cliente en el diccionario y dejamos registro en el log
            Cliente.clientes_registrados[self.identificador] = self
            logger.info(f"Cliente registrado: {self.identificador} - {self.nombre}")

        except ValueError as e:
            logger.error(f"Error al crear cliente {identificador}: {e}")
            raise ClienteIdentificacionError(f"Error en los datos del cliente: {e}") from e
        except ClienteIdentificacionError as e:
            logger.error(f"Error de validación en cliente: {e}")
            raise

    @property
    def nombre(self) -> str:
        """Getter que retorna el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Setter que valida y actualiza el nombre del cliente."""
        # Validamos que no esté vacío y tenga mínimo 3 caracteres
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteIdentificacionError("El nombre no puede estar vacío y debe tener al menos 3 letras.")
        self._nombre = valor.strip()

    @property
    def telefono(self) -> str:
        """Getter que retorna el teléfono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        """Setter que valida y actualiza el teléfono del cliente."""
        # Validamos que sean solo números
        if not isinstance(valor, str) or not valor.strip().isdigit():
            raise ClienteIdentificacionError("El teléfono debe contener solo números y no estar vacío.")
        self._telefono = valor.strip()

    @property
    def correo(self) -> str:
        """Getter que retorna el correo del cliente."""
        return self._correo

    @correo.setter
    def correo(self, valor: str):
        """Setter que valida y actualiza el correo del cliente."""
        # Si ingresan correo, verificamos que tenga @ y punto
        if valor and ("@" not in valor or "." not in valor):
            raise ClienteIdentificacionError("El formato del correo electrónico es inválido.")
        self._correo = valor.strip() if isinstance(valor, str) else ""

    # 4. AGREGAMOS EL MÉTODO PARA BUSCAR UN CLIENTE POR SU CÉDULA
    @classmethod
    def obtener_datos_cliente_especifico(cls, identificador: str):
        """Busca un cliente en el diccionario por su identificador o lanza error si no existe."""
        id_limpio = identificador.strip() if isinstance(identificador, str) else ""
        if id_limpio in cls.clientes_registrados:
            return cls.clientes_registrados[id_limpio]
        
        mensaje = f"Error: El cliente con ID '{identificador}' no se ha registrado aún."
        logger.error(mensaje)
        raise ClienteIdentificacionError(mensaje)

    def mostrar_informacion_entidad(self) -> str:
        """Implementación del método abstracto para mostrar los datos del cliente."""
        return f"Cliente [{self.identificador}]: {self.nombre} | Tel: {self.telefono} | Correo: {self.correo}"

    def actualizar_informacion_entidad(self, **kwargs):
        """Implementación del método abstracto para modificar los datos del cliente."""
        try:
            for clave, valor in kwargs.items():
                if hasattr(self, clave) and valor is not None:
                    setattr(self, clave, valor)
        except ClienteIdentificacionError as e:
            logger.error(f"Error al actualizar cliente {self.identificador}: {e}")
            raise
        else:
            logger.info(f"Cliente {self.identificador} actualizado correctamente.")
        finally:
            logger.debug(f"Fin de actualización para cliente {self.identificador}.")
