"""
main.py - Simulación de operaciones del sistema Software FJ.
Responsable: Persona 3
"""
from excepciones import SoftwareFJError
from logger import registrar_evento, registrar_error

# Listas internas (no se usa base de datos)
clientes = []
servicios = []
reservas = []


def ejecutar_operacion(numero: int, descripcion: str, funcion) -> None:
    """Ejecuta una operación y captura cualquier error para que el programa siga."""
    pass  # TODO Persona 3


def main() -> None:
    print("Software FJ - esqueleto listo")  # TODO Persona 3: 12 operaciones


if __name__ == "__main__":
    main()
