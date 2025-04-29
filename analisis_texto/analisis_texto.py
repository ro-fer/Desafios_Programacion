'''
# 📊 Análisis de Texto

## 🧠 Consigna

Crea un programa que analice un texto y obtenga la siguiente información utilizando **un único bucle**:

- 📌 Número total de palabras.
- 📏 Longitud media de las palabras.
- 🔢 Número de oraciones (cada vez que aparece un punto `.`).
- 🏆 La palabra más larga del texto.'''

def analisis (texto):
    texto = texto.split()
    palabra_larga=""
    long_pal_larga = 0
    total_palabras=0
    long_media = 0.00
    nro_oraciones = 0
    for palabra in texto:
        nro_oraciones += palabra.count(".")
        palabra = palabra.strip(".,;:¡!¿?\"()[]")
        total_palabras += 1
        long_media  += len(palabra)
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    if total_palabras > 0:
        long_media = round(long_media / total_palabras, 2)
    else:
        long_media = 0
    print(f" Total de palabras: {total_palabras} \n Longitud media: {long_media} \n Número de oraciones: {nro_oraciones} \n Palabra más larga: '{palabra_larga}'  ")

texto = input("Ingrese el texto a analizar: \n")
analisis(texto)