# Proyecto de Ejercicios en Python

Este proyecto contiene dos scripts en Python que implementan ejercicios simples de consola:

## `ejecicio1.py`

- Presenta un sistema médico básico.
- Solicita al usuario el número total de médicos a registrar.
- Valida que el número de médicos sea un entero positivo.
- Para cada médico, pide un nombre que tenga al menos 6 caracteres y no contenga espacios.
- Pide los años de experiencia, valida que sean un entero no negativo y clasifica al médico como:
  - residente junior cuando tiene 5 años o menos de experiencia
  - especialista senior cuando tiene más de 5 años de experiencia
- Imprime un resumen final con el conteo de residentes y especialistas.

## `ejecicio2.py`

- Presenta un menú de biblioteca en consola.
- Define las siguientes opciones:
  1. Libros disponibles
  2. Realizar préstamo
  3. Devolver préstamo
  4. Historial de préstamos
  5. Salir
- Controla el stock de libros y el historial de préstamos.
- Valida la entrada de opciones y de cantidades de libros.
- Permite prestar libros si hay stock suficiente.
- Permite devolver libros si no se excede el stock máximo.
- Muestra un conteo de préstamos realizados en la opción de historial.

## Ejecución

Ejecuta cada archivo con Python desde la terminal:

```bash
python ejecicio1.py
python ejecicio2.py
```
