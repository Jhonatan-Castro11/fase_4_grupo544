"""
servicios.py - Clase abstracta Servicio y servicios especializados.
Responsable: Persona 2

Tareas:
- Servicio (abstracta, hereda de EntidadBase): nombre, precio_base, disponible.
  Métodos abstractos: calcular_costo(duracion, impuesto=0.0, descuento=0.0),
  describir() y validar_parametros(duracion).
- Tres servicios hijos que sobrescriben esos métodos:
  ReservaSala (por hora), AlquilerEquipo (por día), Asesoria (por hora + recargo).
- Lanzar ServicioInvalidoError y CalculoInconsistenteError cuando corresponda.
"""