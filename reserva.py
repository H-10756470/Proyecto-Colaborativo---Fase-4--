from modelos_base import EntidadBasica
import excepciones
from logger_config import logger

# Importamos las clases Cliente y Servicio para poder validar que lo que llega a la reserva si es un cliente y un servicio
from cliente import Cliente
from servicios import Servicio


class Reserva(EntidadBasica):
    """Esta clase representa una reserva de Software FJ. Junta un cliente, un servicio, la duracion en horas y el estado de la reserva. Hereda de EntidadBasica."""

    def __init__(self, identificador, cliente, servicio, duracion):
        # Aqui uso try/except para controlar los errores al crear la reserva.
        try:
            # El constructor de EntidadBasica valida el identificador (si esta vacio lanza ValueError)
            super().__init__(identificador)

            # Verificamos que el cliente sea un objeto Cliente y que este registrado
            if not isinstance(cliente, Cliente) or cliente.identificador not in Cliente.clientes_registrados:
                raise excepciones.ClienteNoEncontradoError("La reserva necesita un cliente registrado.")

            # Verificamos que el servicio sea un objeto Servicio
            if not isinstance(servicio, Servicio):
                raise excepciones.ServicioNoEncontradoError("La reserva necesita un servicio valido.")

            # Si el servicio tiene el atributo disponible y esta en False, no se puede reservar
            if hasattr(servicio, "disponible") and not servicio.disponible:
                raise excepciones.ServicioNoDisponibleError("El servicio " + servicio.nombre + " no esta disponible.")

            # Guardamos los atributos de forma privada
            self._cliente = cliente
            self._servicio = servicio
            self._duracion = self.validar_duracion(duracion)
            # Toda reserva nueva empieza en estado Pendiente
            self._estado = "Pendiente"
            self._costo_total = 0

        except ValueError as error:
            logger.error(f"Error al crear la reserva {identificador}: {error}")
            raise excepciones.ReservaInvalidaError(f"Error en los datos de la reserva: {error}") from error
        except excepciones.SoftwareFJError as error:
            logger.error(f"Error de validacion en la reserva {identificador}: {error}")
            raise


    @property
    def cliente(self):
        """Getter que retorna el cliente de la reserva."""
        return self._cliente

    @property
    def servicio(self):
        """Getter que retorna el servicio de la reserva."""
        return self._servicio

    @property
    def estado(self):
        """Getter que retorna el estado de la reserva (Pendiente, Confirmada, Procesada o Cancelada)."""
        return self._estado

    @property
    def costo_total(self):
        """Getter que retorna el costo total, solo tiene valor cuando la reserva ya fue procesada."""
        return self._costo_total

    @property
    def duracion(self):
        """Getter que retorna la duracion de la reserva en horas."""
        return self._duracion

    @duracion.setter
    def duracion(self, valor):
        """Setter que valida y cambia la duracion. Solo se puede cambiar si la reserva esta Pendiente."""
        if self._estado != "Pendiente":
            logger.error(f"Se intento cambiar la duracion de la reserva {self.identificador} que esta {self._estado}.")
            raise excepciones.OperacionNoPermitidaError("Solo se puede cambiar la duracion de una reserva pendiente.")
        self._duracion = self.validar_duracion(valor)

    def validar_duracion(self, valor):
        """Esta funcion revisa que la duracion sea un numero entero entre 1 y 12 horas y la devuelve ya convertida."""
        # Aqui convierto el valor a entero, si falla encadeno el error original con "from"
        try:
            duracion = int(valor)
        except (ValueError, TypeError) as error:
            raise excepciones.DatoInvalidoError("La duracion debe ser un numero entero de horas.") from error
        if duracion <= 0 or duracion > 12:
            raise excepciones.ReservaInvalidaError("La duracion debe estar entre 1 y 12 horas.")
        return duracion

    # Aqui hago la confirmacion

    def confirmar(self):
        """Esta funcion confirma la reserva. Solo se puede confirmar si esta Pendiente."""
        try:
            if self._estado != "Pendiente":
                raise excepciones.OperacionNoPermitidaError(f"No se puede confirmar una reserva que esta {self._estado}.")
            self._estado = "Confirmada"
        except excepciones.OperacionNoPermitidaError as error:
            logger.error(f"Error al confirmar la reserva {self.identificador}: {error}")
            raise
        else:
            logger.info(f"Reserva {self.identificador} confirmada correctamente.")
        finally:
            logger.debug(f"Fin del intento de confirmacion de la reserva {self.identificador}.")

    def cancelar(self):
        """Esta funcion cancela la reserva. No se puede cancelar si ya esta cancelada o ya fue procesada."""
        try:
            if self._estado == "Cancelada":
                raise excepciones.OperacionNoPermitidaError(f"La reserva {self.identificador} ya esta cancelada.")
            if self._estado == "Procesada":
                raise excepciones.OperacionNoPermitidaError("No se puede cancelar una reserva que ya fue procesada.")
            self._estado = "Cancelada"
            self._costo_total = 0
        except excepciones.OperacionNoPermitidaError as error:
            logger.error(f"Error al cancelar la reserva {self.identificador}: {error}")
            raise
        else:
            logger.info(f"Reserva {self.identificador} cancelada correctamente.")
        finally:
            logger.debug(f"Fin del intento de cancelacion de la reserva {self.identificador}.")

    def procesar(self):
        """Esta funcion procesa la reserva: calcula el costo total y la deja en estado Procesada. Solo se pueden procesar reservas Confirmadas."""
        costo = 0
        try:
            if self._estado != "Confirmada":
                raise excepciones.OperacionNoPermitidaError(f"Solo se pueden procesar reservas confirmadas, esta reserva esta {self._estado}.")

            # Las reservas de 6 horas o mas tienen un descuento del 10%
            descuento = 0
            if self._duracion >= 6:
                descuento = 0.10

            # Se calcula el costo con el descuento y el IVA del 19%
            costo = self.calcular_costo_total(descuento, 0.19)

        except excepciones.SoftwareFJError as error:
            # Aqui encadeno el error original con un error nuevo de reserva
            logger.error(f"Error al procesar la reserva {self.identificador}: {error}")
            raise excepciones.ReservaInvalidaError(f"No se pudo procesar la reserva {self.identificador}.") from error
        else:
            # Si no hubo errores guardamos el costo y cambiamos el estado
            self._costo_total = costo
            self._estado = "Procesada"
            logger.info(f"Reserva {self.identificador} procesada. Costo total: ${costo}")
        finally:
            logger.debug(f"Fin del procesamiento de la reserva {self.identificador}.")

    def calcular_costo_total(self, descuento=0, impuesto=0):
        """Este metodo hace de 'sobrecarga': se puede llamar sin parametros, solo con descuento, o con descuento e impuesto."""
        # Primero pido el costo base al servicio. Cada servicio lo calcula a su manera (polimorfismo).
        try:
            costo_base = self._servicio.calcular_costo()
        except Exception as error:
            raise excepciones.CalculoError("No se pudo calcular el costo base del servicio.") from error

        # Revisamos que los valores del calculo tengan sentido
        if costo_base <= 0:
            raise excepciones.CalculoError("El costo base calculado no es valido.")
        if descuento < 0 or descuento > 1:
            raise excepciones.CalculoError("El descuento debe estar entre 0 y 1.")
        if impuesto < 0 or impuesto > 1:
            raise excepciones.CalculoError("El impuesto debe estar entre 0 y 1.")

        costo = costo_base - (costo_base * descuento)
        costo = costo + (costo * impuesto)
        return round(costo, 2)

    # Estos son los metodos abstractos que Reserva hereda de EntidadBasica

    def mostrar_informacion_entidad(self):
        """Implementacion del metodo abstracto para mostrar los datos de la reserva."""
        return (
            f"Reserva [{self.identificador}]\n"
            f"Cliente: {self._cliente.nombre} ({self._cliente.identificador})\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duracion: {self._duracion} horas\n"
            f"Estado: {self._estado}\n"
            f"Costo total: ${self._costo_total}"
        )

    def actualizar_informacion_entidad(self, **kwargs):
        """Implementacion del metodo abstracto para modificar los datos de la reserva. Solo se puede cambiar la duracion."""
        try:
            if "duracion" in kwargs:
                self.duracion = kwargs["duracion"]
        except excepciones.SoftwareFJError as error:
            logger.error(f"Error al actualizar la reserva {self.identificador}: {error}")
            raise
        else:
            logger.info(f"Reserva {self.identificador} actualizada correctamente.")
        finally:
            logger.debug(f"Fin de actualizacion para la reserva {self.identificador}.")
