'''
🔢 Ejercicio: Números primos en un rango
Escribí un programa que pida un número entero positivo n y calcule todos los números primos en el rango de 1 a n.
🔍 ¿Qué es un número primo?
Un número primo es aquel que solo tiene dos divisores: 1 y el mismo número.

Por ejemplo:
2 es primo (solo tiene divisores 1 y 2).

3 es primo (solo tiene divisores 1 y 3).

4 no es primo (divisores: 1, 2, 4).
'''

def primos (nro):
    primos = []
    for n in range(2, nro + 1):  # Empezamos en 2, porque 1 no es primo
        es_primo = True
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(n)
    print(f'Los nros primos entre 1 y {nro} son: \n {primos}')

nro = input('Ingrese un nro para definir el rango a analizar: \n')
primos(int(nro))
