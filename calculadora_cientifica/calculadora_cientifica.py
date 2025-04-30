'''
# 🧮 Calculadora Científica

Crea un programa que simule una calculadora científica con las siguientes características:

- Solicita al usuario un número entero positivo (`n`) y una operación matemática.
- Permite calcular:
  - `seno` (`sin`)
  - `coseno` (`cos`)
  - `tangente` (`tan`)
  - `exponencial` (`exp`)
  - `logaritmo neperiano` (`log`)
- Muestra por pantalla una **tabla** con los enteros del 1 al número ingresado y el resultado de aplicar la función a cada uno de ellos.

'''
import pandas as pd
import math as m
opciones = {1 :"Seno", 2: "Coseno", 3:"Tangente", 4:"Exponencial", 5:"Logaritmo"}

def calculadora (nro , funcion):
    valores =[]
    val_cal=[]
    for n in range (1,nro+1):
        valores.append(n)
    match funcion:
        case 1:
            for valor in valores: 
                val_cal.append([valor,m.sin(valor)])
        case 2:
            for valor in valores: 
                val_cal.append([valor,m.cos(valor)])
        case 3:
            for valor in valores: 
                val_cal.append([valor,m.tan(valor)])
        case 4:
            for valor in valores: 
                val_cal.append([valor,m.exp(valor)])
        case 5:
            for valor in valores: 
                val_cal.append([valor,m.log(valor)])
    df = pd.DataFrame(val_cal, columns=["Nro", opciones[funcion]])
    print(df)

while True:
    nro = int(input("Ingrese el nro a analizar: \n"))
    funcion = int(input(f"Ingrese la funcion que quiere realizar : {opciones} \n"))
    if funcion in opciones: 
        calculadora(nro,funcion)
    elif funcion == 0:
        break
    else:
        print(f"\n Has ingresado un valor incorrecto. ")
