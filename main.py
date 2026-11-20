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


def prueba_ok():
    """Operación de prueba que funciona."""
    print("Todo salió bien")


def prueba_falla():
    """Operación de prueba que lanza un error del sistema."""
    raise SoftwareFJError("Algo salió mal")


def main():
    """Ejecuta la simulación completa."""
    ejecutar_operacion(1, "Prueba que funciona", prueba_ok) #Muestra una operación que funciona correctamente
    ejecutar_operacion(2, "Prueba que falla", prueba_falla) #Muestra una operación que falla y captura el error sin detener el programa
    # Aquí se pueden agregar más operaciones de prueba, tanto exitosas como fallidas
    print(f"Resumen: {resumen['exitosas']} exitosas, {resumen['fallidas']} fallidas")
    print("El programa terminó sin detenerse") # Muestra un mensaje al finalizar el programa


if __name__ == "__main__":
    main()

