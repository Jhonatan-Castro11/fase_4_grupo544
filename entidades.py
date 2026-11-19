#Modulo que contiene las entidades base y la clase Cliente del sistema
from abc import ABC, abstractmethod
import re
from excepciones import ClienteInvalidoError
from logger import registrar_evento, registrar_error

class EntidadBase(ABC):
#Clase abstracta base para las entidades del sistema
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar(self):
        pass

class Cliente(EntidadBase):
#Entidad que representa a un cliente con validación de datos personales
    
    def __init__(self, id, nombre, documento, correo, telefono):
        super().__init__(id)
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono
        self.validar()
        registrar_evento(f"Cliente creado: {self.nombre} (ID: {self.id})")
#=========Nombre===================
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            registrar_error("Intento de asignar nombre vacío al cliente.")
            raise ClienteInvalidoError("El nombre no puede estar vacío.")
        self._nombre = valor.strip()
#===========Documento=============================
    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if not valor:
            registrar_error("Intento de asignar documento vacío al cliente.")
            raise ClienteInvalidoError("El documento es obligatorio.")
        self._documento = str(valor).strip()
#=============correo=============================
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', str(valor)):
            registrar_error(f"Formato de correo inválido: {valor}")
            raise ClienteInvalidoError(f"Correo con formato incorrecto: {valor}")
        self._correo = valor.strip()
#==================telefono==================================
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            registrar_error(f"Teléfono inválido ingresado: {valor}")
            raise ClienteInvalidoError("El teléfono debe tener al menos 7 números.")
        self._telefono = str(valor)

# metodos de la clase abstracta
    def validar(self):
        return True

    def describir(self):
        return f"Cliente {self.nombre} (Doc: {self.documento}, Correo: {self.correo})"