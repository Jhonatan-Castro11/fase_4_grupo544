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
        print(f"ERROR controlado: {e}")       # Muestra el error sin detener el programa
        resumen["fallidas"] += 1              # Registra la operación fallida en el resumen
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

def main():
    """Ejecuta la simulación completa."""
    ejecutar_operacion(1, "Registro de cliente válido", op_cliente_valido) #Muestra una operación que funciona correctamente
    ejecutar_operacion(2, "Registro de cliente con correo inválido", op_correo_invalido) #Muestra una operación que falla y captura el error sin detener el programa
    ejecutar_operacion(3, "Registro de cliente sin documento", op_cliente_sin_documento) #Muestra una operación que falla y captura el error sin detener el programa
    # Aquí se pueden agregar más operaciones de prueba, tanto exitosas como fallidas
    print(f"Clientes registrados: {len(clientes)}")  # Solo deben quedar los clientes válidos
    print(f"Resumen: {resumen['exitosas']} exitosas, {resumen['fallidas']} fallidas")
    print("El programa terminó sin detenerse") # Muestra un mensaje al finalizar el programa


if __name__ == "__main__":
    main()

