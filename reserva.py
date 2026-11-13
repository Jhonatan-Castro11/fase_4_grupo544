# TEMPORAL: borrar cuando Persona 1 suba excepciones.py y usar el import
class ReservaInvalidaError(Exception):
    pass
class Reserva:
    """Clase que representa una reserva de un servicio por parte de un cliente."""
    def __init__(self, id,cliente, servicio,duracion):
        if duracion <= 0:
            raise ReservaInvalidaError(f"Duración inválida: {duracion}")
        self.id = id
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"  # Estado inicial de la reserva
        self.costo_total = 0.0  # Costo total de la reserva

    def __str__(self):
        return f"Reserva(id={self.id}, cliente={self.cliente}, servicio={self.servicio}, duracion={self.duracion}, estado={self.estado}, costo_total={self.costo_total})"



if __name__ == "__main__":
    r = Reserva(1, "cliente_prueba", "servicio_prueba", 2)
    print(r)
    print(r.id, r.estado, r.costo_total)

    try:
        r2 = Reserva(2, "cliente_prueba", "servicio_prueba", 0)
    except ReservaInvalidaError as e:
        print("Error capturado:", e)

