#Modulo de excepciones personalizadas para el sistema Software FJ

class SoftwareFJError(Exception):
    """Clase padre de todas las excepciones del sistema"""
    pass

class ClienteInvalidoError(SoftwareFJError):
    """Lanzada cuando los datos del cliente fallan la validacion o faltan."""
    pass

class ServicioInvalidoError(SoftwareFJError):
    """Lanzada cuando se crea un servicio con datos incorrectos"""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Lanzada cuando se intenta confirmar una reserva sin disponibilidad"""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Lanzada por errores lógicos en la reserva"""
    pass

class OperacionNoPermitidaError(SoftwareFJError):
    """Lanzada cuando se intenta una accion sobre un estado que no lo permite"""
    pass

class CalculoInconsistenteError(SoftwareFJError):
    """Lanzada cuando un descuento supera el 100% o el cálculo falla"""
    pass