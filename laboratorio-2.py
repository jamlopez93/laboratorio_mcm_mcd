from math import gcd
from functools import reduce


def factorizar(n):
    factores = {}
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factores[divisor] = factores.get(divisor, 0) + 1
            n //= divisor
        divisor += 1
    return factores


def mcm_descomposicion(numeros):
    factores = [factorizar(num) for num in numeros]
    mcm_factores = {}
    for factores_num in factores:
        for factor, exp in factores_num.items():
            mcm_factores[factor] = max(mcm_factores.get(factor, 0), exp)
    mcm = 1
    for factor, exp in mcm_factores.items():
        mcm *= factor ** exp
    return mcm

def mcd_descomposicion(numeros):
    factores = [factorizar(num) for num in numeros]
    mcd_factores = {}
    for factor in set.intersection(*[set(f.keys()) for f in factores]):
        mcd_factores[factor] = min(factorizar(num).get(factor, 0) for num in numeros)
    mcd = 1
    for factor, exp in mcd_factores.items():
        mcd *= factor ** exp
    return mcd


def mcd_euclidiano(numeros):
    return reduce(gcd, numeros)

def mcm_euclidiano(numeros):
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    return reduce(lcm, numeros)


if __name__ == "__main__":
    print("Ingrese numeros enteros positivos separados por espacios:")
    numeros = list(map(int, input().split()))

    
    mcm1 = mcm_descomposicion(numeros)
    mcd1 = mcd_descomposicion(numeros)
    print(f"Metodo 1 (Descomposición Factorial):\nMCM: {mcm1}, MCD: {mcd1}")

    
    mcd2 = mcd_euclidiano(numeros)
    mcm2 = mcm_euclidiano(numeros)
    print(f"Metodo 2 (Algoritmo de euclides):\nMCM: {mcm2}, MCD: {mcd2}")
