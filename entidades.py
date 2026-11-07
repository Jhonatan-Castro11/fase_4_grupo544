"""
entidades.py - Clase abstracta EntidadBase y clase Cliente.
Responsable: Persona 1
"""
from abc import ABC, abstractmethod

from excepciones import ClienteInvalidoError


class EntidadBase(ABC):
    """Clase abstracta que representa cualquier entidad del sistema."""

    def __init__(self, id_entidad: str):
        self.id = id_entidad

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción de la entidad."""

    @abstractmethod
    def validar(self) -> None:
        """Valida los datos de la entidad; lanza excepción si son inválidos."""


class Cliente(EntidadBase):
    """Cliente con datos personales encapsulados (atributos privados)."""

    def __init__(self, id_entidad: str, nombre: str, documento: str,
                 correo: str, telefono: str):
        super().__init__(id_entidad)
        # TODO Persona 1: atributos privados (self.__nombre, ...) + @property con validación
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    def describir(self) -> str:
        return f"Cliente {self.nombre}"  # TODO Persona 1

    def validar(self) -> None:
        pass  # TODO Persona 1: lanzar ClienteInvalidoError si algo falla
