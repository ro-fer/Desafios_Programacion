# Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.

def calculadora(atacante, defensor, ataque, defensa):
    efect = efectividad(atacante,defensor)
    danio = 50 * (ataque / defensa) * efect
    print(f"El daño que se realizo fue de : \n {danio}")

def efectividad(atacante, defensor):
    efect = {
        "agua-agua" : 0.5, "agua-fuego": 2.0, "agua-planta":0.5, "agua-electrico" : 1.0,
        "fuego-agua" : 0.5, "fuego-fuego": 0.5, "fuego-planta": 2.0, "fuego-electrico" : 1.0,
        "planta-agua" : 2.0, "planta-fuego": 0.5, "planta-planta":0.5, "planta-electrico" : 1.0,
        "electrico-agua" : 2.0, "electrico-fuego": 1.0, "electrico-planta":0.5, "electrico-electrico" : 0.5,
    }
    atacante=atacante.lower()
    defensor=defensor.lower()
    clave_efec= atacante+"-"+defensor
    return efect[clave_efec]

print(f"BIENVENIDX! Esta es una calculadora de pokemon! Tene en cuenta que los tipos de pokemones son: \n 🔥 Fuego \t 💧 Agua \t 🌱 Planta \t⚡ Eléctrico")
atacante = input("Primero vas a tener que ingresar el tipo del pokemon atacante:  \n")
defensor = input("Ahora vas a tener que ingresar el tipo del pokemon defensor:  \n")
ataque = int( input ("Ingresa el valor de ataque que debe de estar entre 1 y 100 \n"))
defensa = int( input ("Ingresa el valor de defensa que debe de estar entre 1 y 100 \n"))
calculadora(atacante, defensor, ataque, defensa)