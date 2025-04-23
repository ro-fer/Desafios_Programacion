'''
#💡 Ejercicio: Contador de palabras únicas
Escribí un programa que reciba un texto (una oración o párrafo) y cuente cuántas palabras distintas hay en él.

Por ejemplo, en el texto:
"Hola mundo hola otra vez"
El programa debería decir que hay 4 palabras distintas: hola, mundo, otra, vez
'''

def contador_pal_unicas (texto):
    palabras_unicas =[]
    for palabra in  texto.lower().split():
        if palabra not in palabras_unicas:
            palabras_unicas.append(palabra)
    print(f"\nEn el texto \n {texto} \n  Hay {len(palabras_unicas)} palabras unicas.\n Que son las siguientes: \n {palabras_unicas}")

texto = input("Ingrese el texto que quiere contar palabras unicas: \n")
contador_pal_unicas(texto)