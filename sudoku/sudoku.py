'''
🧠 Ejercicio: Sudoku válido (versión simplificada)
📋 Consigna:
Escribí un programa que reciba una matriz de 9x9 (una lista de listas en Python), representando un tablero de Sudoku, y verifique si es válido.

Un tablero es válido si:

Cada fila contiene solo números del 1 al 9 sin repetir.

Cada columna contiene solo números del 1 al 9 sin repetir.

Cada subcuadro de 3x3 también contiene números del 1 al 9 sin repetir.

🧩 No es necesario que sea resoluble, solo que lo que esté cargado cumpla con esas reglas.
'''
def sudoku (tablero):
    nros_ordenados = [i for i in range(1, 10)]
    for fila in tablero:
        if sorted(fila)  != nros_ordenados:
            print(f"❌ El sudoku no es correcto")
            break
    for col in range(9):
        columna = [tablero[fila][col] for fila in range(9)]
        if sorted(columna)  != nros_ordenados:
            print(f"❌ El sudoku no es correcto")
            break
    if not verificar_bloques(tablero):
        return
    

def verificar_bloques(tablero):
    nros_ordenados = [i for i in range(1, 10)]
    for fila_bloque in range(0, 9, 3):          # 0, 3, 6
        for col_bloque in range(0, 9, 3):       # 0, 3, 6
            bloque = []
            for i in range(3):
                for j in range(3):
                    bloque.append(tablero[fila_bloque + i][col_bloque + j])
            if sorted(bloque) != nros_ordenados:
                print(f" ❌ El sudoku no es correcto")
                return False
    return True

tablero = []
print("Ingrese cada fila del Sudoku como 9 números separados por espacios:")
for i in range(9):
    fila = list(map(int, input(f"Fila {i+1}: ").split()))
    tablero.append(fila)
sudoku(tablero)