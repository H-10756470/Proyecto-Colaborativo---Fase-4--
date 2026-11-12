class SoftwareFJError(Exception):
    """Esta clase sirve de clase padre para todas las demas excepciones personalizadas"""
    pass

class ClienteIdentificacionError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente no ingresa todos los datos pedidos o los ingresa mal."""
    pass

class ServicioNoEncontradoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente solicita un servicio que no provehe Software FJ."""
    pass

class ReservInvalidaError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente hace una reserva invalida."""
    pass

