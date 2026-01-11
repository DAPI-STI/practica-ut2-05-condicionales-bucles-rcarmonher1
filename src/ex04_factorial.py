"""
Ejercicio 4 (un poco más complejo):
Factorial de un número.
"""

def factorial(n: int) -> int:
    """
    Devuelve n! (n factorial).

    Reglas:
    - 0! = 1
    - Si n < 0, lanza ValueError.
    - Debe resolverse usando un bucle (no recursión).
    """
    if n < 0:
        raise ValueError("Introduce un número que sea entero positivo o cero")
    
    factorial = 1
    
    for i in range(1, n + 1):
        factorial = factorial * i
        
    return factorial
    raise NotImplementedError("Implementa factorial(n)")
