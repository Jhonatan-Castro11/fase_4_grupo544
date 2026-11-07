"""
entidades.py - Clase abstracta EntidadBase y clase Cliente.
Responsable: Persona 1

Tareas:
- EntidadBase (abstracta): atributo id y métodos abstractos describir() y validar().
- Cliente (hereda de EntidadBase): nombre, documento, correo y teléfono
  como atributos privados, con @property y validaciones.
- Lanzar ClienteInvalidoError cuando un dato sea inválido o falte.
"""