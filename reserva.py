class Reserva:
    """Clase que representa una reserva de un servicio por parte de un cliente."""
    def __init__(self, id,cliente, servicio,duracion):
        self.id = id
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"  # Estado inicial de la reserva
        self.costo_total = 0.0  # Costo total de la reserva


if __name__ == "__main__":
    r = Reserva(1, "cliente_prueba", "servicio_prueba", 2)
    print(r.id, r.estado, r.costo_total)
