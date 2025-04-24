'''
🕵️‍♀️ Ejercicio: Palabra oculta
📋 Consigna:
Escribí un programa que reciba dos palabras e indique si la segunda está "oculta" dentro de la primera.
Una palabra está oculta en otra si se pueden encontrar todas sus letras, en orden, dentro de la primera palabra (aunque no necesariamente seguidas).

🔍 Ejemplo:

Entrada:
Palabra 1: "murciélago"
Palabra 2: "río"
Salida: ✅ "río" está oculta en "murciélago"

Entrada:
Palabra 1: "murciélago"
Palabra 2: "luz"
Salida: ❌ "luz" no está oculta en "murciélago"

🎯 Objetivo: Practicar recorrido secuencial de strings y uso de condiciones.
'''

def palabra_oculta (pal, texto):
    contador=0
    for letra in texto:
        for letra2 in pal:
            if letra == letra2: 
                contador +=1
    if contador == len(pal):
        print(f'{pal} está oculta en {texto}')
    else:
        print(f'{pal} no está oculta en {texto}')

pal = input('Ingrese la palabra oculta a buscar: \n')
texto = input('Ingrese la palabra oculta a buscar: \n')
palabra_oculta (pal, texto)