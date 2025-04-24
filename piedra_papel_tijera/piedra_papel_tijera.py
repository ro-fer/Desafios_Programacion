'''
✊📄✂️ Piedra, Papel o Tijera

Este programa calcula quién gana más partidas en una serie de enfrentamientos de **Piedra, Papel o Tijera**.

## 📌 Descripción

La función recibe una lista de jugadas, donde cada jugada es un par de elecciones entre:

- `"R"` → **Rock** (Piedra)  
- `"P"` → **Paper** (Papel)  
- `"S"` → **Scissors** (Tijera)

Cada par representa una partida entre el **Jugador 1** y el **Jugador 2**.  
El programa cuenta cuántas partidas gana cada jugador y determina el resultado general:

- `"Player 1"` → gana más partidas el Jugador 1  
- `"Player 2"` → gana más partidas el Jugador 2  
- `"Tie"` → empataron en cantidad de victorias

'''

def pied_papel_tij (jugadas):
    jugadas = list(jugadas)
    ganadores = {"R": "S","S": "P","P": "R"}
    p1=0
    p2=0
    for j1, j2 in jugadas: 
        if ganadores[j1] == j2: 
            p1 +=1 
        elif ganadores[j2] == j1:
            p2 +=1 
    if p1>p2:
        print(f"Gano el jugador 1, con {p1} puntos")
    elif p2>p1:
        print(f"Gano el jugador 2, con {p2} puntos")
    else: 
        print(f"EMPATARON!")


jugadas = []
print("Ingrese las jugadas en el formato 'R S', 'P R', etc. (Enter vacío para terminar):")
while True:
    linea = input("> ").strip().upper()
    if linea == "":
        break
    partes = linea.split()
    if len(partes) == 2 and partes[0] in "RPS" and partes[1] in "RPS":
        jugadas.append((partes[0], partes[1]))
    else:
        print("Entrada no válida. Usá solo R, P o S, separados por un espacio.")

pied_papel_tij(jugadas)