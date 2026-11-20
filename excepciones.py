class SoftwareFJError(Exception):
    """Esta clase sirve de clase padre para todas las demas excepciones personalizadas del sistema"""

class ClienteIdentificacionError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente no ingresa todos los datos pedidos o los ingresa mal."""
   
class ClienteNoEncontradoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente no se encuentra registrado y se trata de hacer una reserva con el."""
  
class DatoInvalidoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente ingresa un dato invalido, como un numero de telefono con letras, un correo electronico sin @, etc."""
    
class ClienteYaRegistradoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente intenta registrarse con un identificador que ya esta registrado."""

class ServicioNoDisponibleError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente solicita un servicio que no esta disponible o esta fuera de horario."""
    
class ServicioNoEncontradoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente solicita un servicio que no provee Software FJ o lo solicita mal"""
    
class ReservaInvalidaError(SoftwareFJError):
    """Esta excepcion se usa cuando se hace una reserva invalida."""
    
class ReservaNoDisponibleError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente solicita una reserva que no esta disponible o esta fuera de horario."""
    
class CalculoError(SoftwareFJError):
    """Esta excepcion se usa cuando hay un error en los calculos del sistema. como en los costos de los servicios, en los descuentos, en los impuestos, etc."""
    
class OperacionNoPermitidaError(SoftwareFJError):
    """Esta excepcion se usa cuando se intenta realizar una operacion que no esta permitida."""
    
class LogError(SoftwareFJError):
    """Esta excepcion se usa cuando hay un error en el registro de logs del sistema."""
    