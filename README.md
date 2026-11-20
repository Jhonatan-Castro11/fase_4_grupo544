# Software FJ — Sistema de gestión de clientes, servicios y reservas

Curso Programación (213023) — UNAD — Fase 4 — Grupo 544

Sistema orientado a objetos en Python, sin base de datos, que gestiona clientes,
servicios (reserva de salas, alquiler de equipos y asesorías especializadas) y
reservas, con manejo avanzado de excepciones y registro de eventos en un archivo
de logs. El programa sigue funcionando aunque ocurran errores durante su ejecución.

## Cómo ejecutarlo

Requiere Python 3.10 o superior. No necesita instalar librerías externas.

```bash
python main.py
```

El programa simula 12 operaciones (5 válidas y 7 inválidas) y termina sin detenerse.
Los eventos y errores quedan registrados en `logs/eventos.log`.

## Estructura del proyecto

| Archivo            | Contenido                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| `excepciones.py`   | Excepción base `SoftwareFJError` y 6 excepciones personalizadas que heredan de ella                     |
| `logger.py`        | Funciones `registrar_evento` y `registrar_error`, que escriben en `logs/eventos.log` con fecha y nivel  |
| `entidades.py`     | Clase abstracta `EntidadBase` y clase `Cliente` con datos encapsulados y validados                      |
| `servicios.py`     | Clase abstracta `Servicio` y sus servicios especializados: `ReservaSala`, `AlquilerEquipo` y `Asesoria` |
| `reserva.py`       | Clase `Reserva` con los métodos `confirmar`, `cancelar` y `procesar`, y su control de estados           |
| `main.py`          | Simulación de 12 operaciones, protegidas por la función `ejecutar_operacion`                            |
| `logs/eventos.log` | Registro de eventos y errores (se genera al ejecutar el programa)                                       |

## Conceptos aplicados

| Concepto                      | Dónde se aplica                                                                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Abstracción                   | `EntidadBase` y `Servicio` son clases abstractas con métodos `@abstractmethod`                                                                      |
| Herencia                      | `Cliente` hereda de `EntidadBase`; `ReservaSala`, `AlquilerEquipo` y `Asesoria` heredan de `Servicio`; las excepciones heredan de `SoftwareFJError` |
| Polimorfismo                  | Cada servicio sobrescribe `calcular_costo`, `describir` y `validar_parametros` a su manera (operación 6)                                            |
| Encapsulación                 | Atributos protegidos con `@property` y setters que validan en `Cliente` y en los servicios                                                          |
| Sobrecarga simulada           | `calcular_costo(duracion, impuesto=0.0, descuento=0.0)` con parámetros opcionales (operación 12)                                                    |
| try / except                  | `ejecutar_operacion` en `main.py` atrapa los errores del sistema y los inesperados                                                                  |
| try / except / else           | `ejecutar_operacion` cuenta las operaciones exitosas en el `else`                                                                                   |
| try / except / finally        | `Reserva.procesar` registra en el log el fin del procesamiento, haya o no error                                                                     |
| Encadenamiento de excepciones | `Reserva.procesar` convierte `CalculoInconsistenteError` en `ReservaInvalidaError` con `raise ... from` (operación 11)                              |
| Listas internas               | `clientes`, `servicios` y `reservas` en `main.py` reemplazan a la base de datos                                                                     |
| Archivo de logs               | Todas las clases registran eventos y errores en `logs/eventos.log`                                                                                  |

## Operaciones simuladas

| #   | Operación                                    | Resultado esperado                                             |
| --- | -------------------------------------------- | -------------------------------------------------------------- |
| 1   | Registrar cliente válido                     | Éxito                                                          |
| 2   | Registrar cliente con correo inválido        | `ClienteInvalidoError`                                         |
| 3   | Registrar cliente sin documento              | `ClienteInvalidoError`                                         |
| 4   | Crear sala con precio válido                 | Éxito                                                          |
| 5   | Crear sala con precio negativo               | `ServicioInvalidoError`                                        |
| 6   | Crear alquiler de equipo y asesoría          | Éxito (polimorfismo)                                           |
| 7   | Reserva confirmada y procesada               | Éxito con costo final                                          |
| 8   | Reserva con duración cero                    | `ReservaInvalidaError`                                         |
| 9   | Reservar un servicio ocupado                 | `ServicioNoDisponibleError`                                    |
| 10  | Cancelar una reserva ya procesada            | `OperacionNoPermitidaError`                                    |
| 11  | Procesar con descuento mayor al 100 %        | `ReservaInvalidaError` causada por `CalculoInconsistenteError` |
| 12  | Comparar las 3 variantes de `calcular_costo` | Éxito (sobrecarga simulada)                                    |

## Integrantes

| Integrante         | Responsabilidad                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| Jhonatan Castro    | `excepciones.py`, `logger.py`, `entidades.py` creación del repositorio, documento PDF de entrega |
| Jhorman González   | `servicios.py`: clase abstracta `Servicio` y `ReservaSala`                                       |
| Camilo Guerrero    | `servicios.py`: `AlquilerEquipo` y `Asesoria`;                                                   |
| Carlos Andrés Díaz | `reserva.py`, `main.py`, `README.md`; integración y pruebas del reposiorio                       |
