'''
Ejercicio 2 : Repeticiones Maximas

Dado un string, devolvé el carácter que más veces se repite (y cuántas veces). 
 -> Pensarlo sin utilizar librerias externas
'''
def contador_letras (texto):
    contador = {}
    texto = texto.replace(" ", "").lower()
    for letra in texto:
        if letra in contador:
            contador[letra] +=1
        else:
            contador[letra] =1
    max=0
    letra_max = ""
    for letra in contador:
        if contador[letra] > max:
            letra_max=letra
            max=contador[letra]
    print(f"La letra mas repetida de {texto} es {letra_max} y aparece {max} de veces. ")

texto = input('Ingrese una palabra o texto: ')
contador_letras(texto)

