'''
#Ejercicio 1 : Anagrama
Genere un programa que reciba del usuario, dos palabras y compruebe si son anagramas (tienen las mismas letras en diferente orden). 
'''

def anagrama(pal1,pal2):
    pal1 = pal1.replace(" ", "").lower()
    pal2 = pal2.replace(" ", "").lower()
    if sorted(pal1) == sorted(pal2):
        print(f"{pal1} y {pal2} son anagramas.")
    else:
        print(f"{pal1} y {pal2} no son anagramas.")


pal1 = input('Ingrese la primera palabra: ')
pal2 = input('Ingrese la segunda palabra: ')
anagrama(pal1,pal2)