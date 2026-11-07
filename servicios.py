"""
servicios.py - Clase abstracta Servicio y sus servicios especializados.
Responsable: Persona 2
"""
from abc import abstractmethod

from entidades import EntidadBase
from excepciones import ServicioInvalidoError, CalculoInconsistenteError


class Servicio(EntidadBase):
    """Servicio abstracto que ofrece Software FJ."""

    def __init__(self, id_entidad: str, nombre: str, precio_base: float,
                 disponible: bool = True):
        super().__init__(id_entidad)
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion: float, impuesto: float = 0.0,
                       descuento: float = 0.0) -> float:
        """Costo total. Variantes: (duracion), (duracion, impuesto), (duracion, impuesto, descuento)."""

    @abstractmethod
    def validar_parametros(self, duracion: float) -> None:
        """Valida la duración pedida; lanza excepción si es inválida."""

    def validar(self) -> None:
        pass  # TODO Persona 2: precio_base > 0, nombre no vacío -> ServicioInvalidoError


class ReservaSala(Servicio):
    """Reserva de salas: cobro por hora."""

    def __init__(self, id_entidad, nombre, precio_base, capacidad: int, disponible=True):
        super().__init__(id_entidad, nombre, precio_base, disponible)
        self.capacidad = capacidad

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        raise NotImplementedError  # TODO Persona 2

    def describir(self):
        return f"Sala {self.nombre}"  # TODO Persona 2

    def validar_parametros(self, duracion):
        pass  # TODO Persona 2


class AlquilerEquipo(Servicio):
    """Alquiler de equipos: cobro por día."""

    def __init__(self, id_entidad, nombre, precio_base, tipo_equipo: str, disponible=True):
        super().__init__(id_entidad, nombre, precio_base, disponible)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        raise NotImplementedError  # TODO Persona 2

    def describir(self):
        return f"Equipo {self.nombre}"  # TODO Persona 2

    def validar_parametros(self, duracion):
        pass  # TODO Persona 2


class Asesoria(Servicio):
    """Asesorías especializadas: tarifa por hora + recargo."""

    def __init__(self, id_entidad, nombre, precio_base, especialidad: str, disponible=True):
        super().__init__(id_entidad, nombre, precio_base, disponible)
        self.especialidad = especialidad

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
        raise NotImplementedError  # TODO Persona 2

    def describir(self):
        return f"Asesoría {self.nombre}"  # TODO Persona 2

    def validar_parametros(self, duracion):
        pass  # TODO Persona 2
