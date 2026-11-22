
<<<<<<< HEAD
# =====================================================
# PARTE C - MODULO DE SERVICIOS
# Proyecto Software FJ
#
# En este archivo se crean las clases relacionadas
# con los servicios que ofrece la empresa.
#
# Se utiliza:
# - Herencia
# - Clases abstractas
# - Encapsulamiento
# - Excepciones personalizadas
# - Logger
# - Metodos heredados de EntidadBasica
# =====================================================

# Importamos abstractmethod para poder crear metodos abstractos
from abc import abstractmethod

=======
# PARTE C - MODULO DE SERVICIOS Proyecto Software FJ
# En este archivo cree las clases de servicios que ofrece la empresa.
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
# Importamos la clase base creada en la Parte A
from modelos_base import EntidadBasica
# Importamos las excepciones personalizadas del proyecto
import excepciones
# Importamos la configuracion del logger
import logger_config
# CLASE SERVICIO
<<<<<<< HEAD
# =====================================================
# Esta clase sirve como clase base para todos los
# los servicios ofrecidos por Software FJ.
#
# Hereda de EntidadBasica porque todo servicio
# tiene un identificador unico.
#
# Ahora es abstracta porque tiene metodos abstractos
# (calcular_costo y describir_servicio) que cada
# servicio hijo esta obligado a implementar.
# =====================================================

=======
# Esta clase sirve para clase base en todos los servicios ofrecidos por Software FJ.
# Hereda de EntidadBasica porque todo servicio tiene un id unico.
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
class Servicio(EntidadBasica):

    # este es el constructor de la clase, Aqui recibimos el identificador, nombre, descripcion y precio del servicio.
    def __init__(self, identificador, nombre, descripcion, precio):
        # Llamamos al constructor de la clase padre
        super().__init__(identificador)

        try:
            # Verificamos que en nombre no este vacio
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

            # Todo servicio nuevo empieza disponible
            self._disponible = True

        except Exception as error:
            # Guardamos el error en el archivo de logs "logger"
            logger_config.logger.error(
                f"Error creando servicio: {error}"
            )

            raise
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
<<<<<<< HEAD

    # Getter para saber si el servicio esta disponible
    @property
    def disponible(self):
        return self._disponible

    # Setter para cambiar la disponibilidad del servicio
    @disponible.setter
    def disponible(self, valor):

        # Solo se acepta True o False
        if not isinstance(valor, bool):

            logger_config.logger.error(
                "Se intento asignar una disponibilidad que no es True o False."
            )

            raise excepciones.DatoInvalidoError(
                "La disponibilidad debe ser True o False."
            )

        self._disponible = valor

    # ==========================================
    # METODOS ABSTRACTOS
    # ==========================================

    # Cada servicio calcula su costo a su manera (polimorfismo)
    @abstractmethod
    def calcular_costo(self):
        pass

    # Cada servicio se describe a su manera (polimorfismo)
    @abstractmethod
    def describir_servicio(self):
        pass

    # ==========================================
    # METODOS DE APOYO
    # ==========================================

    # Este metodo revisa que un dato numerico sea mayor a 0.
    # Lo usan los servicios hijos para validar sus parametros.
    def validar_numero_positivo(self, valor, nombre_campo):

        if not isinstance(valor, (int, float)) or valor <= 0:

            logger_config.logger.error(
                f"Parametro invalido en el servicio: {nombre_campo} = {valor}"
            )

            raise excepciones.DatoInvalidoError(
                f"El campo {nombre_campo} debe ser un numero mayor a 0."
            )

        return valor

    # Este metodo hace de 'sobrecarga': se puede llamar sin parametros,
    # solo con descuento, o con descuento e impuesto.
    def calcular_costo_final(self, descuento=0, impuesto=0):

        costo = self.calcular_costo()

        # Revisamos que el descuento y el impuesto tengan sentido
        if descuento < 0 or descuento > 1:
            logger_config.logger.error("Descuento fuera de rango en calcular_costo_final.")
            raise excepciones.CalculoError("El descuento debe estar entre 0 y 1.")

        if impuesto < 0 or impuesto > 1:
            logger_config.logger.error("Impuesto fuera de rango en calcular_costo_final.")
            raise excepciones.CalculoError("El impuesto debe estar entre 0 y 1.")

        costo = costo - (costo * descuento)
        costo = costo + (costo * impuesto)

        return round(costo, 2)

    # ==========================================
    # METODOS HEREDADOS DE ENTIDADBASICA
    # ==========================================

    # Este metodo muestra la informacion
    # principal del servicio.
=======
    # Este metodo muestra la informacion principal del servicio.
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
    def mostrar_informacion_entidad(self):

        return (
            f"Codigo: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Descripcion: {self.descripcion}\n"
            f"Precio: ${self.precio}"
        )

    # Este metodo permite actualizar uno o varios atributos
    def actualizar_informacion_entidad(self, **kwargs):

        if "nombre" in kwargs:
            self.nombre = kwargs["nombre"]

        if "descripcion" in kwargs:
            self.descripcion = kwargs["descripcion"]

        if "precio" in kwargs:
            self.precio = kwargs["precio"]

# Esta clase representa el tipo de reserva de salas para reuniones o capacitaciones.
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
<<<<<<< HEAD

        # Datos propios de las salas (se validan antes de guardarlos)
        self.capacidad = self.validar_numero_positivo(capacidad, "capacidad")
        self.horas = self.validar_numero_positivo(horas, "horas")

=======
        # aqui los datos propios de las salas
        self.capacidad = capacidad
        self.horas = horas
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
    # El costo depende de la tarifa y las horas
    def calcular_costo(self):

        return self.precio * self.horas
<<<<<<< HEAD

    # Describimos el servicio con sus datos propios
    def describir_servicio(self):

        return (
            f"Sala '{self.nombre}' para {self.capacidad} personas "
            f"durante {self.horas} horas."
        )

=======
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nCapacidad: {self.capacidad}"
            + f"\nHoras reservadas: {self.horas}"
        )
# Esta clase representa el alquiler de equipos tecnologicos como computadores, tablets,
# proyectores o equipos especializados.
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

<<<<<<< HEAD
        # Cantidad de equipos solicitados
        self.cantidad = self.validar_numero_positivo(cantidad, "cantidad")

        # Dias de alquiler
        self.dias = self.validar_numero_positivo(dias, "dias")
=======
        # aqui la cantidad de equipos solicitados
        self.cantidad = cantidad

        # aqui los dias de alquiler
        self.dias = dias
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3

    # El costo depende de cantidad y dias de alquiler
    def calcular_costo(self):

        return self.precio * self.cantidad * self.dias
<<<<<<< HEAD

    # Describimos el servicio con sus datos propios
    def describir_servicio(self):

        return (
            f"Alquiler de {self.cantidad} equipo(s) '{self.nombre}' "
            f"por {self.dias} dia(s)."
        )

=======
>>>>>>> e7323ba8551a3a63ef0b6cd8aa01192513faa1b3
    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nCantidad de equipos: {self.cantidad}"
            + f"\nDias de alquiler: {self.dias}"
        )
# Esta clase representa las asesorias que presta la empresa en diferentes areas.

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
        self.horas = self.validar_numero_positivo(horas, "horas")

    # El costo depende de las horas de asesoria
    def calcular_costo(self):

        return self.precio * self.horas

    # Describimos el servicio con sus datos propios
    def describir_servicio(self):

        return (
            f"Asesoria '{self.nombre}' de {self.horas} hora(s)."
        )

    # Mostramos la informacion completa
    def mostrar_informacion_entidad(self):

        return (
            super().mostrar_informacion_entidad()
            + f"\nHoras de asesoria: {self.horas}"
        )

