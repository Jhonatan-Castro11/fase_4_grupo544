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

    def __init__(self, nombre: str, precio_base: float, disponible: bool = True):
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

    def __init__(self, nombre: str, precio_base: float, disponible: bool = True):
        super().__init__(nombre, precio_base, disponible)

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

# ---------------------------------------------------------------------------
# CLASES DE CAMILO GUERRERO: AlquilerEquipo y Asesoria
# Requiere (arriba en servicios.py): from excepciones import ServicioInvalidoError, CalculoInconsistenteError
# ---------------------------------------------------------------------------


class AlquilerEquipo(Servicio):  # Servicio especializado: alquiler de equipos, se cobra por día
    """Alquiler de equipos (portátiles, proyectores, etc.). La duración se mide en DÍAS."""

    DIAS_MAXIMOS = 30  # Límite de días permitidos por alquiler

    def __init__(self, nombre, precio_base, disponible=True, tipo_equipo="general"):  # Constructor de la clase hija
        super().__init__(nombre, precio_base, disponible)  # Reutiliza validaciones y atributos de la clase padre
        self._tipo_equipo = tipo_equipo  # Atributo propio: tipo de equipo (encapsulado)

    @property  # Permite leer el tipo de equipo como atributo
    def tipo_equipo(self):  # Getter del tipo de equipo
        return self._tipo_equipo  # Devuelve el tipo de equipo almacenado

    def validar_parametros(self, duracion):  # Sobrescribe el método abstracto de Servicio
        try:  # Intenta validar el tipo de dato de la duración
            dias = int(duracion)  # Convierte la duración a entero (días completos)
            if dias != duracion:  # Rechaza valores con decimales (ej. 2.5 días)
                raise ValueError("los días deben ser enteros")  # Error interno que se encadena abajo
        except (TypeError, ValueError) as error:  # Captura duración no numérica o con decimales
            raise CalculoInconsistenteError(f"Duración inválida para el alquiler: {duracion!r}") from error  # Encadena la excepción original
        if dias <= 0 or dias > self.DIAS_MAXIMOS:  # Verifica el rango permitido de días
            raise CalculoInconsistenteError(f"El alquiler debe ser de 1 a {self.DIAS_MAXIMOS} días, se recibió {dias}")  # Fuera de rango
        return dias  # Devuelve los días ya validados

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):  # Cálculo con parámetros opcionales (sobrecarga)
        dias = self.validar_parametros(duracion)  # Valida la duración antes de calcular
        if not 0.0 <= descuento <= 1.0:  # El descuento es una fracción: 0.10 = 10 %, máximo 1.0 = 100 %
            raise CalculoInconsistenteError(f"Descuento fuera de rango (0 a 1): {descuento}")  # Descuento mayor a 100 % o negativo
        if impuesto < 0.0:  # El impuesto no puede ser negativo
            raise CalculoInconsistenteError(f"Impuesto negativo: {impuesto}")  # Cálculo inconsistente
        subtotal = self.precio_base * dias  # Costo bruto: precio por día por cantidad de días
        subtotal_con_descuento = subtotal * (1.0 - descuento)  # Aplica el descuento sobre el subtotal
        total = subtotal_con_descuento * (1.0 + impuesto)  # Suma el impuesto (ej. 0.19 = IVA 19 %)
        if total < 0:  # Verifica que el resultado final no sea negativo
            raise CalculoInconsistenteError(f"Costo total negativo: {total}")  # Costo negativo
        return round(total, 2)  # Devuelve el costo con dos decimales

    def describir(self):  # Sobrescribe el método abstracto de descripción
        estado = "disponible" if self.disponible else "no disponible"  # Texto según la disponibilidad
        return (f"Alquiler de equipo '{self.nombre}' ({self._tipo_equipo}): "  # Datos básicos del servicio
                f"${self.precio_base:,.0f} por día, máximo {self.DIAS_MAXIMOS} días, {estado}.")  # Tarifa, límite y estado


class Asesoria(Servicio):  # Servicio especializado: asesoría, se cobra por hora más un recargo
    """Asesoría especializada. La duración se mide en HORAS y se suma un recargo porcentual."""

    HORAS_MAXIMAS = 8  # Límite de horas por sesión de asesoría

    def __init__(self, nombre, precio_base, disponible=True, especialidad="general", recargo=0.0):  # Constructor de la clase hija
        super().__init__(nombre, precio_base, disponible)  # Reutiliza validaciones y atributos de la clase padre
        if recargo < 0.0:  # El recargo no puede ser negativo
            raise ServicioInvalidoError(f"Recargo negativo: {recargo}")  # Dato inválido al crear el servicio
        self._especialidad = especialidad  # Atributo propio: área de la asesoría (encapsulado)
        self._recargo = recargo  # Atributo propio: recargo como fracción (0.20 = 20 %)

    @property  # Permite leer la especialidad como atributo
    def especialidad(self):  # Getter de la especialidad
        return self._especialidad  # Devuelve la especialidad almacenada

    @property  # Permite leer el recargo como atributo
    def recargo(self):  # Getter del recargo
        return self._recargo  # Devuelve el recargo almacenado

    def validar_parametros(self, duracion):  # Sobrescribe el método abstracto de Servicio
        try:  # Intenta validar el tipo de dato de la duración
            horas = float(duracion)  # Convierte la duración a número (se permiten medias horas)
        except (TypeError, ValueError) as error:  # Captura duración no numérica
            raise CalculoInconsistenteError(f"Duración inválida para la asesoría: {duracion!r}") from error  # Encadena la excepción original
        if horas <= 0 or horas > self.HORAS_MAXIMAS:  # Verifica el rango permitido de horas
            raise CalculoInconsistenteError(f"La asesoría debe durar más de 0 y máximo {self.HORAS_MAXIMAS} horas, se recibió {horas}")  # Fuera de rango
        return horas  # Devuelve las horas ya validadas

    def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):  # Cálculo con parámetros opcionales (sobrecarga)
        horas = self.validar_parametros(duracion)  # Valida la duración antes de calcular
        if not 0.0 <= descuento <= 1.0:  # El descuento es una fracción: 0.10 = 10 %, máximo 1.0 = 100 %
            raise CalculoInconsistenteError(f"Descuento fuera de rango (0 a 1): {descuento}")  # Descuento mayor a 100 % o negativo
        if impuesto < 0.0:  # El impuesto no puede ser negativo
            raise CalculoInconsistenteError(f"Impuesto negativo: {impuesto}")  # Cálculo inconsistente
        subtotal = self.precio_base * horas  # Costo bruto: precio por hora por cantidad de horas
        subtotal_con_recargo = subtotal * (1.0 + self._recargo)  # Suma el recargo de la asesoría
        subtotal_con_descuento = subtotal_con_recargo * (1.0 - descuento)  # Aplica el descuento sobre el valor con recargo
        total = subtotal_con_descuento * (1.0 + impuesto)  # Suma el impuesto (ej. 0.19 = IVA 19 %)
        if total < 0:  # Verifica que el resultado final no sea negativo
            raise CalculoInconsistenteError(f"Costo total negativo: {total}")  # Costo negativo
        return round(total, 2)  # Devuelve el costo con dos decimales

    def describir(self):  # Sobrescribe el método abstracto de descripción
        estado = "disponible" if self.disponible else "no disponible"  # Texto según la disponibilidad
        return (f"Asesoría de {self._especialidad} '{self.nombre}': "  # Datos básicos del servicio
                f"${self.precio_base:,.0f} por hora + recargo del {self._recargo:.0%}, "  # Tarifa y recargo
                f"máximo {self.HORAS_MAXIMAS} horas, {estado}.")  # Límite de horas y estado
