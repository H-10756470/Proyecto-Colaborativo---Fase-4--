class SoftwareFJError(Exception):
    """Esta clase sirve de clase padre para todas las demas excepciones personalizadas del sistema"""
    pass

class ClienteIdentificacionError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente no ingresa todos los datos pedidos o los ingresa mal."""
    pass

class ServicioNoEncontradoError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente solicita un servicio que no provehe Software FJ o lo solicita mal."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Esta excepcion se usa cuando el cliente hace una reserva invalida."""
    pass

