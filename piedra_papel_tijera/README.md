#✊📄✂️ Piedra, Papel o Tijera

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

---

## 🧪 Ejemplo de uso

```python
jugadas = [("R", "S"), ("S", "R"), ("P", "S")]
resultado = piedra_papel_tijera(jugadas)
print(resultado)  # ➞ "Player 2"