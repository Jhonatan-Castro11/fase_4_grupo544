"""
main.py - Simulación de operaciones del sistema Software FJ.
Responsable: Persona 3

Tareas:
- Listas internas de clientes, servicios y reservas (sin base de datos).
- Función ejecutar_operacion() que capture errores para que el programa no se detenga.
- Simular al menos 12 operaciones válidas e inválidas (ver el plan de trabajo).
"""
# Excepción padre de todas las del sistema (excepciones.py)
from excepciones import SoftwareFJError
# Clase Cliente del sistema (entidades.py)
from entidades import Cliente
# Clase ReservaSala, AlquilerEquipo y Asesoria del sistema (servicios.py)
from servicios import ReservaSala, AlquilerEquipo, Asesoria
# Clase Reserva del sistema (reserva.py)
from reserva import Reserva

# Listas internas: reemplazan a la base de datos
clientes = []
servicios = []
reservas = []

# Contadores para el resumen final
resumen = {"exitosas": 0, "fallidas": 0}


def ejecutar_operacion(numero, descripcion, funcion):
    """Captura errores de las operaciones para que el programa no se detenga."""
    print(f"Ejecutando operación {numero}: {descripcion}")  # Muestra el número y la descripción de la operación
    try:
        funcion()                             # Ejecuta la función que representa la operación recibida como argumento
    except SoftwareFJError as e:
        print(f"ERROR controlado: {e}")
        if e.__cause__:                               # Si el error trae otro encadenado...
            print(f"  Causa original: {e.__cause__}")  # ...también muestra el error original
        resumen["fallidas"] += 1              # Registra la operación fallida en el resumen

    except Exception as e:
        print(f"ERROR inesperado: {e}")       # Muestra errores de programación sin detener el programa
        resumen["fallidas"] += 1              # Cuenta la operación como fallida
    else:
        print("Operación exitosa")            # Si no hay errores, muestra un mensaje de éxito
        resumen["exitosas"] += 1              # Registra la operación exitosa en el resumen
    finally:
        print("Fin de la operación\n")        # Muestra un mensaje al finalizar la operación


def op_cliente_valido():
    """Registra un cliente con todos sus datos correctos."""
    cliente = Cliente(1, "Ana Pérez", "1010", "ana@correo.com", "3001234567")  # Crea el cliente (valida sus datos)
    clientes.append(cliente)                                                    # Lo guarda en la lista
    print(cliente.describir())
    
def op_correo_invalido():
    """Intenta registrar un cliente con un correo inválido."""
    cliente = Cliente(2, "Luis García", "1011", "luis@correo", "3001234568")  # Crea el cliente (valida sus datos)
    clientes.append(cliente)                                                    # Lo guarda en la lista
    print(cliente.describir())                                                 # Muestra sus datos

def op_cliente_sin_documento():
    """Intenta registrar un cliente sin número de documento."""
    cliente = Cliente(3, "María López", "", "maria@correo.com", "3001234569")  # Crea el cliente (valida sus datos)
    clientes.append(cliente)                                                    # Lo guarda en la lista
    print(cliente.describir())                                                  # Muestra sus datos

def op_crear_sala():
    """Crea un servicio de reserva de sala con datos correctos."""
    sala = ReservaSala("Sala A", 50000)  # Crea la sala (valida sus datos)
    servicios.append(sala)               # La guarda en la lista
    print(sala.describir())              # Muestra sus datos

def op_servicio_precio_negativo():
    """Intenta crear un servicio con precio negativo."""
    sala = ReservaSala("Sala B", -5000)  # Crea la sala (valida sus datos)
    servicios.append(sala)                   # La guarda en la lista
    print(sala.describir())                  # Muestra sus datos

def op_crear_equipo_y_asesoria():
    """Crea un servicio de alquiler de equipo y asesoría con datos correctos."""
    equipo = AlquilerEquipo("Proyector", 20000, tipo_equipo="Audiovisual")  # Crea el equipo (valida sus datos)
    asesoria = Asesoria("Asesoría de marketing", 150000, especialidad="Marketing", recargo=0.1)  # Crea la asesoría (valida sus datos)
    servicios.append(equipo)               # Guarda el equipo en la lista
    servicios.append(asesoria)             # Guarda la asesoría en la lista
    print(equipo.describir())              # Polimorfismo: el mismo método describir()
    print(asesoria.describir())            # da una respuesta diferente según el tipo de servicio

def op_reserva_exitosa():
    """Crea, confirma y procesa una reserva válida de la Sala A."""
    reserva = Reserva(1, clientes[0], servicios[0], 2)   # Ana reserva la Sala A por 2 horas
    reserva.confirmar()                                  # Pasa a confirmada y ocupa la sala
    costo = reserva.procesar(0.19, 0.10)                 # Cobra con 19 % de IVA y 10 % de descuento
    reservas.append(reserva)                             # La guarda en la lista
    print(f"Reserva {reserva.id} procesada. Costo: ${costo:,.2f}")  # Muestra el resultado

def op_reserva_duracion_cero():
    """Intenta crear una reserva con duración cero."""
    reserva = Reserva(2, clientes[0], servicios[0],0)    #Se intenta hacer una reserva con duracionde 0 horas
    reservas.append(reserva)                             #Nunca llega aqui si la duracion es invalida
    
def op_servicio_ocupado():
    """Intenta crear una reserva de un servicio que ya está ocupado."""
    primera = Reserva(3, clientes[0], servicios[0], 1)   # Primera reserva de la Sala A
    primera.confirmar()                                  # Pasa a confirmada y ocupa la sala
    reservas.append(primera)                             # La guarda en la lista
    segunda = Reserva(4, clientes[0], servicios[0], 1)   #Segunda reserva de la misma sala
    segunda.confirmar()                                  #Pasa a confirmar la misma sala ya ocupada

def op_cancelar_procesada():
    """Intenta cancelar una reserva que ya fue procesada."""
    reserva = reservas[0] # La reserva 1, que se procesó en la operación 7
    reserva.cancelar()    # Intenta cancelarla: debe fallar porque ya está procesada

def op_descuento_invalido():
    """"Intenta procesar una reserva con un descuento inválido (mayor al 100%)."""
    reserva = Reserva(5, clientes[0], servicios[1], 2)   # Ana alquila el proyector por 2 días
    reserva.confirmar()                                  # Pasa a confirmada y ocupa la sala
    reserva.procesar(0.19, 1.5)                          # Descuento del 150 %: debe fallar

def op_variantes_costo():
    """Muestra diferentes variantes de cálculo de costo para una asesoría."""
    asesoria = servicios[2]                             # La asesoría
    sin_extras = asesoria.calcular_costo(2)             # Solo duración
    con_iva = asesoria.calcular_costo(2, 0.19)          # Duración + IVA
    completo = asesoria.calcular_costo(2, 0.19, 0.10)   # Duración + IVA + descuento
    print(f"Solo duración:       ${sin_extras:,.2f}")
    print(f"Con IVA:             ${con_iva:,.2f}")
    print(f"Con IVA y descuento: ${completo:,.2f}")

def main():
    """Ejecuta la simulación completa."""
    ejecutar_operacion(1, "Registro de cliente válido", op_cliente_valido) #Muestra una operación que funciona correctamente
    ejecutar_operacion(2, "Registro de cliente con correo inválido", op_correo_invalido) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(3, "Registro de cliente sin documento", op_cliente_sin_documento) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(4, "Creación de sala con precio válido", op_crear_sala) #Muestra una operación que funciona correctamente
    ejecutar_operacion(5, "Creación de sala con precio negativo", op_servicio_precio_negativo) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(6, "Creación de alquiler de equipo y asesoría", op_crear_equipo_y_asesoria) #Muestra una operación que funciona correctamente
    ejecutar_operacion(7, "Reserva exitosa de Sala A", op_reserva_exitosa) #Muestra una operación que funciona correctamente
    ejecutar_operacion(8, "Reserva con duración cero", op_reserva_duracion_cero) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(9, "Reserva de servicio ocupado", op_servicio_ocupado) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(10,"Cancelar una reserva ya procesada", op_cancelar_procesada)  #Muestra una operacion de intento de cancelacion de una reserva ya procesada
    ejecutar_operacion(11, "Procesar reserva con descuento mayor al 100 %", op_descuento_invalido)
    ejecutar_operacion(12, "Variantes de cálculo de costo para una asesoría", op_variantes_costo)
    print(f"Reservas registradas: {len(reservas)}")  # Solo deben quedar las reservas válidas
    print(f"Clientes registrados: {len(clientes)}")  # Solo deben quedar los clientes válidos
    print(f"Servicios registrados: {len(servicios)}")  # Solo deben quedar los servicios válidos
    print(f"Resumen: {resumen['exitosas']} exitosas, {resumen['fallidas']} fallidas")
    print("El programa terminó sin detenerse") # Muestra un mensaje al finalizar el programa


if __name__ == "__main__":
    main()

