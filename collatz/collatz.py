'''
🔁 Ejercicio: Secuencia de Collatz (o conjetura de Collatz)
📌 Descripción:
La secuencia de Collatz se construye con las siguientes reglas:

Empezá con cualquier número entero positivo n.

Si n es par, dividilo por 2.

Si n es impar, multiplicalo por 3 y sumale 1.

Repetí este proceso con el nuevo valor de n, hasta que el número llegue a 1.

📥 Entrada: un número entero positivo.

📤 Salida: la secuencia completa de números desde n hasta llegar a 1.
'''
def collatz(nro):
    inicio = nro
    serie = []
    serie.append(nro)
    while nro != 1:
        if (nro% 2 == 0):
            nro = nro//2    
        else:
            nro = nro * 3 + 1    
        serie.append(nro)
    print(f"La serie de Collatz a partir de {inicio} es: \n {serie} ")

nro = int(input("Ingrese el nro entero positivo para realizar la Secuencia de Collatz \n"))
collatz(nro)