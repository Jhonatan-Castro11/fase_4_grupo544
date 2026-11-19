from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError, CalculoInconsistenteError


class EntidadBase:
    """Clase base para todas las entidades del sistema."""
    pass


class Servicio(ABC, EntidadBase):
    """
    Clase abstracta que representa un servicio genérico.
    Contiene atributos y métodos comunes a todos los servicios.
    """

    def _init_(self, nombre: str, precio_base: float, disponible: bool = True):
        """
        Inicializa un servicio con sus datos básicos.
        
        :param nombre: Nombre del servicio, no puede estar vacío.
        :param precio_base: Precio base, debe ser mayor o igual a cero.
        :param disponible: Indica si el servicio está disponible. Por defecto True.
        """
        # Valida que el nombre no esté vacío
        if not nombre.strip():
            raise ServicioInvalidoError("El nombre del servicio no puede estar vacío.")
        # Valida que el precio base no sea negativo
        if precio_base < 0:
            raise ServicioInvalidoError("El precio base no puede ser negativo.")
        
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, duracion: float, impuesto: float = 0.0, descuento: float = 0.0) -> float:
        """
        Calcula el costo total del servicio según la duración, impuesto y descuento.
        Cada tipo de servicio implementa su propia lógica.
        
        :param duracion: Tiempo de uso del servicio.
        :param impuesto: Porcentaje de impuesto a aplicar (0.0 a 1.0).
        :param descuento: Porcentaje de descuento a aplicar (0.0 a 1.0).
        :return: Costo total como número flotante.
        """
        pass

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción completa del servicio con sus datos."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion: float) -> None:
        """
        Valida que la duración y otros parámetros sean correctos.
        Lanza una excepción si hay valores incorrectos.
        """
        pass


class ReservaSala(Servicio):
    """Servicio de reserva de sala — cobro por horas de uso."""

    def _init_(self, nombre: str, precio_base: float, disponible: bool = True):
        super()._init_(nombre, precio_base, disponible)

    def calcular_costo(self, duracion: float, impuesto: float = 0.0, descuento: float = 0.0) -> float:
        """
        Calcula el costo de la reserva según horas utilizadas.
        Fórmula: (precio_base × duracion) × (1 + impuesto) × (1 − descuento)
        """
        # Primero valida los parámetros de entrada
        self.validar_parametros(duracion)

        # Valida que el descuento esté entre 0% y 100%
        if descuento < 0 or descuento > 1:
            raise CalculoInconsistenteError("El descuento debe estar entre 0 y 1.")
        # Valida que el impuesto no sea negativo
        if impuesto < 0:
            raise CalculoInconsistenteError("El impuesto no puede ser negativo.")

        # Cálculo del costo base
        costo_base = self.precio_base * duracion
        # Aplica el impuesto
        con_impuesto = costo_base * (1 + impuesto)
        # Aplica el descuento
        costo_total = con_impuesto * (1 - descuento)

        # Valida que el resultado no sea negativo
        if costo_total < 0:
            raise CalculoInconsistenteError("El costo resultante no puede ser negativo.")

        return round(costo_total, 2)

    def describir(self) -> str:
        """Devuelve información detallada de la reserva de sala."""
        estado = "disponible" if self.disponible else "no disponible"
        return f"ReservaSala: {self.nombre} | Precio/hora: ${self.precio_base:.2f} | Estado: {estado}"

    def validar_parametros(self, duracion: float) -> None:
        """Verifica que la duración sea mayor a cero."""
        if duracion <= 0:
            raise CalculoInconsistenteError("La duración debe ser mayor a cero.")