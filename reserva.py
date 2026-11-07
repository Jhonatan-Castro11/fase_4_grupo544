"""
reserva.py - Clase Reserva: integra cliente, servicio, duración y estado.
Responsable: Persona 3
"""
from entidades import Cliente
from servicios import Servicio
from excepciones import (ReservaInvalidaError, ServicioNoDisponibleError,
                         OperacionNoPermitidaError)
from logger import registrar_evento, registrar_error


class Reserva:
    """Reserva de un servicio por un cliente."""

    ESTADOS = ("pendiente", "confirmada", "cancelada", "procesada")

    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio,
                 duracion: float):
        self.id = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"
        self.costo_total = 0.0

    def confirmar(self) -> None:
        pass  # TODO Persona 3: ServicioNoDisponibleError si no está disponible

    def cancelar(self) -> None:
        pass  # TODO Persona 3: OperacionNoPermitidaError si ya está procesada

    def procesar(self, impuesto: float = 0.0, descuento: float = 0.0) -> float:
        pass  # TODO Persona 3: try/except/else/finally + raise ... from e
