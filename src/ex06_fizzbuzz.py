"""
Ejercicio 6 (un poco más complejo):
FizzBuzz.
"""

def fizzbuzz(n: int) -> list[str]:
    """
    Devuelve una lista con los valores de 1 a n, siguiendo estas reglas:

    - Si el número es múltiplo de 3: "Fizz"
    - Si es múltiplo de 5: "Buzz"
    - Si es múltiplo de 3 y 5: "FizzBuzz"
    - En otro caso: el número en texto (por ejemplo "7")

    Si n <= 0, devuelve lista vacía.
    """
    if n <= 0:
        return []
    
    lista = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista.append("FizzBuzz")
        elif i % 3 == 0:
            lista.append("Fizz")
        elif i % 5 == 0:
            lista.append("Buzz")
        else:
            lista.append(str(i))
    return lista

    raise NotImplementedError("Implementa fizzbuzz(n)")
