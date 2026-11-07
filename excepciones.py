"""
excepciones.py - Excepciones personalizadas del sistema Software FJ.
Responsable: Persona 1
"""


class SoftwareFJError(Exception):
    """Excepción base: todas las excepciones del sistema heredan de esta."""
    pass


class ClienteInvalidoError(SoftwareFJError):
    """Datos de cliente inválidos o faltantes."""
    pass


class ServicioInvalidoError(SoftwareFJError):
    """Servicio creado con datos inválidos."""
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    """El servicio no está disponible para reservar."""
    pass


class ReservaInvalidaError(SoftwareFJError):
    """Reserva con datos o estado inválidos."""
    pass


class OperacionNoPermitidaError(SoftwareFJError):
    """Operación no permitida en el estado actual."""
    pass


class CalculoInconsistenteError(SoftwareFJError):
    """Resultado de cálculo de costo inválido (negativo, descuento > 100 %, etc.)."""
    pass
