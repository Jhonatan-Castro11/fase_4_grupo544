# TEMPORAL: borrar cuando Persona 1 suba excepciones.py y usar el import
class ReservaInvalidaError(Exception):
    pass
class OperacionNoPermitidaError(Exception):
    pass

class ServicioNoDisponibleError(Exception):
    pass

class CalculoInconsistenteError(Exception):
    pass
class Reserva:
    """Clase que representa una reserva de un servicio por parte de un cliente."""
    def __init__(self, id,cliente, servicio,duracion):
        if duracion <= 0: # Duración inválida
            raise ReservaInvalidaError(f"Duración inválida: {duracion}")
        # Atributos de la reserva
        self.id = id # Identificador único de la reserva
        self.cliente = cliente # Cliente que realiza la reserva
        self.servicio = servicio # Servicio que se reserva
        self.duracion = duracion # Duración de la reserva en horas
        self.estado = "pendiente"  # Estado inicial de la reserva
        self.costo_total = 0.0  # Costo total de la reserva

    def confirmar(self):
        #Regla 1 regla de negocio: Solo se puede confirmar una reserva si está en estado "pendiente"
        if self.estado != "pendiente":
            raise OperacionNoPermitidaError(f"No se puede confirmar una reserva en estado {self.estado}")
        #Regla 2 regla de negocio: Solo se puede confirmar una reserva si el servicio está disponible
        if not self.servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.servicio.nombre} no está disponible")
        self.estado = "confirmada" # Cambiar el estado a "confirmada"
        self.servicio.disponible = False  # Marcar el servicio como no disponible

    def cancelar(self):
        #Regla 3 regla de negocio: Solo se puede cancelar una reserva si está en estado "pendiente" o "confirmada"
        if self.estado not in ["pendiente", "confirmada"]:
            raise OperacionNoPermitidaError(f"No se puede cancelar una reserva en estado {self.estado}")
        # Regla 4: solo libera el servicio la reserva que lo había ocupado (la confirmada)
        if self.estado == "confirmada":
            self.servicio.disponible = True   # Libera el servicio para otras reservas
        self.estado = "cancelada"  
        
    def procesar(self,impuesto=0.0, descuento=0.0):
        # Regla 5: solo se cobra una reserva confirmada
        if self.estado != "confirmada":
            raise OperacionNoPermitidaError(f"No se puede procesar una reserva en estado {self.estado}") 
        try:
            #Polimorfismo: cada servicio calcula el costo de manera diferente
            costo = self.servicio.calcular_costo(self.duracion, impuesto, descuento)
        except CalculoInconsistenteError as error_calculo:
            raise ReservaInvalidaError(f"No se pudo realizar la reserva {self.id}") from error_calculo
        else:
            self.costo_total = costo # Guardar el costo total de la reserva 
            self.estado = "procesada"  # Cambiar el estado a "procesada"
            self.servicio.disponible = True  # Liberar el servicio para otras reservas
            return costo # Devolver el costo total de la reserva
        finally:
            #finally se ejecuta siempre, haya o no error
            print(f"Fin del procesamiento de la reserva {self.id}") 

    def __str__(self):
        return f"Reserva(id={self.id}, cliente={self.cliente}, servicio={self.servicio}, duracion={self.duracion}, estado={self.estado}, costo_total={self.costo_total})"



if __name__ == "__main__":
    class ServicioPrueba:
        """Servicio falso solo para probar Reserva."""
        def __init__(self, nombre):
            self.nombre = nombre
            self.disponible = True

        def calcular_costo(self, duracion, impuesto=0.0, descuento=0.0):
            if descuento > 1:
                raise CalculoInconsistenteError("Descuento fuera de rango")
            return 50000 * duracion * (1 + impuesto) * (1 - descuento)

    sala = ServicioPrueba("Sala A")

    r = Reserva(1, "cliente_prueba", sala, 2)
    r.confirmar()
    print("Estado:", r.estado, "| Sala disponible:", sala.disponible)

    try:
        r.confirmar()                  # confirmar dos veces
    except OperacionNoPermitidaError as e:
        print("Error capturado:", e)

    try:
        r2 = Reserva(2, "cliente_prueba", sala, 1)
        r2.confirmar()                 # la sala ya está ocupada
    except ServicioNoDisponibleError as e:
        print("Error capturado:", e)

    try:
        r3 = Reserva(3, "cliente_prueba", sala, 0)   # duración inválida
    except ReservaInvalidaError as e:
        print("Error capturado:", e)
    
    r.cancelar()                       # r estaba confirmada
    print("Estado:", r.estado, "| Sala disponible:", sala.disponible)

    try:
        r.cancelar()                   # cancelar dos veces
    except OperacionNoPermitidaError as e:
        print("Error capturado:", e)

    a = Reserva(4, "cliente_prueba", sala, 1)
    a.confirmar()                      # A ocupa la sala
    b = Reserva(5, "cliente_prueba", sala, 1)   # B queda pendiente
    b.cancelar()                       # B nunca ocupó la sala
    print("Sala disponible:", sala.disponible)  # debe ser False

    sala_b = ServicioPrueba("Sala B")           # sala libre
    c = Reserva(6, "cliente_prueba", sala_b, 1) # C queda pendiente
    c.cancelar()                                # C nunca ocupó la sala
    print("Sala B disponible:", sala_b.disponible)  # debe ser True

    sala_c = ServicioPrueba("Sala C")
    p = Reserva(7, "cliente_prueba", sala_c, 2)
    p.confirmar()
    p.procesar(0.19, 0.10)             # 19 % de IVA y 10 % de descuento
    print("Costo:", p.costo_total, "| Estado:", p.estado,
          "| Sala C disponible:", sala_c.disponible)

    try:
        p.cancelar()                   # cancelar una reserva ya procesada
    except OperacionNoPermitidaError as e:
        print("Error capturado:", e)

    try:
        q = Reserva(8, "cliente_prueba", sala_c, 1)
        q.confirmar()
        q.procesar(0.19, 1.5)          # descuento del 150 %
    except ReservaInvalidaError as e:
        print("Error capturado:", e, "| Causa:", e.__cause__)

    try:
        Reserva(9, "cliente_prueba", sala_c, 1).procesar()   # sin confirmar
    except OperacionNoPermitidaError as e:
        print("Error capturado:", e)

