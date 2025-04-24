'''
🔤 Ejercicio: Eliminar vocales
📋 Consigna:
Escribí un programa que reciba una cadena de texto e imprima la misma cadena pero sin vocales (a, e, i, o, u).

🔍 Ejemplo:

Entrada: "Hola mundo"

Salida: "Hl mnd"

🎯 Objetivo: Practicar recorrido de cadenas y filtrado de caracteres.
'''

def eliminar_vocales(texto):
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    texto_sin_vocales = ""
    for letra in texto:
        if letra not in vocales:
            texto_sin_vocales += letra
    print(f"El texto \n {texto}  \n sin vocales es: \n {texto_sin_vocales}")

texto = input('Ingrese un texto para eliminar las vocales: \n')

eliminar_vocales(texto)