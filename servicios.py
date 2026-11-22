
# =====================================================
# PARTE C - MODULO DE SERVICIOS
# Proyecto Software FJ
#
# En este archivo se crean las clases relacionadas
# con los servicios que ofrece la empresa.
#
# Se utiliza:
# - Herencia
# - Encapsulamiento
# - Excepciones personalizadas
# - Logger
# - Metodos heredados de EntidadBasica
# =====================================================

# Importamos la clase base creada en la Parte A
from modelos_base import EntidadBasica

# Importamos las excepciones personalizadas del proyecto
import excepciones

# Importamos la configuracion del logger
import logger_config


# =====================================================
# CLASE SERVICIO
# =====================================================
# Esta clase sirve como clase base para todos los
# los servicios ofrecidos por Software FJ.
#
# Hereda de EntidadBasica porque todo servicio
# tiene un identificador unico.
# =====================================================

class Servicio(EntidadBasica):

    # Constructor de la clase
    # Aqui recibimos el identificador, nombre,
    # descripcion y precio del servicio.
    def __init__(self, identificador, nombre, descripcion, precio):

        # Llamamos al constructor de la clase padre
        super().__init__(identificador)

        try:

            # Verificamos que el nombre no este vacio
            if not nombre.strip():
                raise excepciones.DatoInvalidoError(
                    "El nombre del servicio no puede estar vacio."
                )

            # Verificamos que el precio no sea negativo
            if precio < 0:
                raise excepciones.OperacionNoPermitidaError(
                    "No se puede asignar un precio negativo."
                )

            # Guardamos los atributos de forma privada
            self._nombre = nombre
            self._descripcion = descripcion
            self._precio = precio

        except Exception as error:

            # Guardamos el error en el archivo de logs
            logger_config.logger.error(
                f"Error creando servicio: {error}"
            )

            raise

    # ==========================================
    # GETTERS Y SETTERS
    # ==========================================

    # Getter para obtener el nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para modificar el nombre
    @nombre.setter
    def nombre(self, valor):

        if not valor.strip():

            logger_config.logger.error(
                "Se intento asignar un nombre vacio."
            )

            raise excepciones.DatoInvalidoError(
                "El nombre no puede estar vacio."
            )

        self._nombre = valor

    # Getter para obtener la descripcion
    @property
    def descripcion(self):
        return self._descripcion

    # Setter para modificar la descripcion
    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    # Getter para obtener el precio
    @property
    def precio(self):
        return self._precio

    # Setter para modificar el precio
    @precio.setter
    def precio(self, valor):

        if valor < 0:

            logger_config.logger.error(
                "Se intento asignar un precio negativo."
            )

            raise excepciones.OperacionNoPermitidaError(
                "El precio no puede ser negativo."
            )

        self._precio = valor

    # ==========================================
    # METODOS HEREDADOS DE ENTIDADBASICA
    # ==========================================

    # Este metodo muestra la informacion
    # principal del servicio.
    def mostrar_informacion_entidad(self):

        return (
            f"Codigo: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Descripcion: {self.descripcion}\n"
            f"Precio: ${self.precio}"
        )

    # Este metodo permite actualizar uno
    # o varios atributos usando kwargs.
    def actualizar_informacion_entidad(self, **kwargs):

        if "nombre" in kwargs:
            self.nombre = kwargs["nombre"]

        if "descripcion" in kwargs:
            self.descripcion = kwargs["descripcion"]

        if "precio" in kwargs:
            self.precio = kwargs["precio"]


# =====================================================
# CLASE RESERVA DE SALAS
# =====================================================
# Esta clase representa el servicio de reserva
# de salas para reuniones o capacitaciones.
# =====================================================

class ReservaDeSalas(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        precio,
        capacidad,
        horas
    ):

        # Heredamos los datos generales
        super().__init__(
            identificador,
            nombre,
            descripcion,
            precio
        )

        # Datos propios de las salas
        self.capacidad = capacidad
        self.horas = horas

    # El costo depende de la tarifa y las horas
    def calcular_costo(self):

        return self.precio * self.horas

    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nCapacidad: {self.capacidad}"
            + f"\nHoras reservadas: {self.horas}"
        )


# =====================================================
# CLASE ALQUILER DE EQUIPOS
# =====================================================
# Esta clase representa el alquiler de equipos
# tecnologicos como computadores, tablets,
# proyectores o equipos especializados.
# =====================================================

class AlquilerDeEquipos(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        precio,
        cantidad,
        dias
    ):

        super().__init__(
            identificador,
            nombre,
            descripcion,
            precio
        )

        # Cantidad de equipos solicitados
        self.cantidad = cantidad

        # Dias de alquiler
        self.dias = dias

    # El costo depende de cantidad y dias
    def calcular_costo(self):

        return self.precio * self.cantidad * self.dias

    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nCantidad de equipos: {self.cantidad}"
            + f"\nDias de alquiler: {self.dias}"
        )


# =====================================================
# CLASE ASESORIAS ESPECIALIZADAS
# =====================================================
# Esta clase representa las asesorias que
# presta la empresa en diferentes areas.
# =====================================================

class AsesoriasEspecializadas(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        descripcion,
        precio,
        horas
    ):

        super().__init__(
            identificador,
            nombre,
            descripcion,
            precio
        )

        # Horas contratadas por el cliente
        self.horas = horas

    # El costo depende de las horas de asesoria
    def calcular_costo(self):

        return self.precio * self.horas

    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nHoras de asesoria: {self.horas}"
        )
