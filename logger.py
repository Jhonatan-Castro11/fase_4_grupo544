#Modulo para el registro de eventos y errores en archivo
import os
from datetime import datetime

def _escribir_log(mensaje_formateado: str) -> None:
    """maneja la apertura del archivo de forma segura"""
    os.makedirs("logs", exist_ok=True)
    archivo = None
    try:
        archivo = open("logs/eventos.log", "a", encoding="utf-8")
        archivo.write(mensaje_formateado + "\n")
    except Exception as e:
        print(f"Error crítico al escribir en el log: {e}")
    finally:
        if archivo is not None:
            archivo.close()

def registrar_evento(mensaje: str, nivel: str = "INFO") -> None:
    """Registra un evento normal en el sistema con su fecha y nivel"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _escribir_log(f"{fecha} - {nivel.upper()} - {mensaje}")

def registrar_error(mensaje: str, excepcion: Exception | None = None) -> None:
    """Registra un error capturado con el detalle de la excepcion"""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detalle = f" - Detalle: {str(excepcion)}" if excepcion else ""
    _escribir_log(f"{fecha} - ERROR - {mensaje}{detalle}")