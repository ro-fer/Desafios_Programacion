'''
🔐 Ejercicio: Cifrado César
📌 Descripción:
El cifrado César es una técnica antigua de encriptación donde cada letra del mensaje se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto.

📥 Entrada:

Un texto a cifrar (solo letras, sin signos ni números).

Un número entero que indica el desplazamiento (positivo).

📤 Salida:

El texto cifrado, manteniendo las mayúsculas y minúsculas (si querés complicarlo más, podés hacer que conserve espacios y caracteres no alfabéticos sin cifrar).
'''
def cifrado_cesar(texto, nro):
    texto_codificado=""
    nuevo_valor = 0
    for letra in texto:
        if letra.isalpha():
            valor_ascii = ord(letra)
            if letra.islower():  #  minúsculas
                nuevo_valor = (valor_ascii - 97 + nro) % 26 + 97
            elif letra.isupper():  #  mayúsculas
                nuevo_valor = (valor_ascii - 65 + nro) % 26 + 65
            texto_codificado += chr(nuevo_valor)
        else:
            texto_codificado += letra
    print(f"El texto original es: \n {texto} \n El texto cifrado es: {texto_codificado}")

texto = input("Ingrese texto a cifrar: \n")
nro_desplaz = int (input("Ingrese un nro entero que indica el desplazamiento para el cifrado Cesar: \n"))
cifrado_cesar(texto, nro_desplaz)