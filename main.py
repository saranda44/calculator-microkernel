"""
Calculadora con arquitectura de microkernel.
"""

from core.microkernel import Microkernel


def main():
    calculator = Microkernel()

    # Cargar todos los plugins automáticamente
    calculator.load_plugins()

    # Ejemplo de uso
    a, b = 5, 3

    # Ejecutar todas las operaciones registradas
    for op_name in calculator.operators:
        result = calculator.execute_operation(op_name, a, b)
        print(f"• {a} {op_name.capitalize()} {b}: {result}")


if __name__ == "__main__":
    main()
