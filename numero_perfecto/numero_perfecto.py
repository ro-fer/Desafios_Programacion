'''
🔢 Ejercicio: Número perfecto
Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo él mismo).

Por ejemplo:

6 → sus divisores son 1, 2 y 3 → 1 + 2 + 3 = 6 → ✅ es perfecto

28 → divisores: 1, 2, 4, 7, 14 → suma = 28 → ✅

12 → divisores: 1, 2, 3, 4, 6 → suma = 16 → ❌ no es perfecto
'''

def nro_perfecto (nro):
    divisores=[]
    suma=0
    for n in range(1,nro):
         
        if (nro % n) == 0:
            divisores.append(n)
            suma +=n
    print(f"\nEl número {nro} {'es' if suma == nro else 'no es'} perfecto.")
    print(f"Divisores: {divisores}")
    if suma != nro:
        print(f"Suma de divisores: {suma}")


nro = input("Ingrese el nro a analizar si es perfecto o no: \n")
nro_perfecto(int(nro))   
