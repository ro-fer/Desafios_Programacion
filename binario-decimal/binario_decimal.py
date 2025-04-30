'''
🔁 Conversión Decimal-Binario

## 📌 Consigna

Escribe un programa que contenga dos funciones:

1. Una función que convierta un número **decimal** en **binario**.
2. Otra función que convierta un número **binario** (como cadena de texto) en **decimal**.
'''

def binario (nro):
    nro_bin =""
    while True: 
        if nro>= 2:
            nro_bin += str(int(nro %2))
            nro = nro // 2
        else:
            nro_bin += str(nro)
            break
    nro_bin = nro_bin[::-1]
    print(f"El nro en binario es : \n {nro_bin} \n")

def decimal (nro):
    nro_bin = str(nro)
    suma = 0
    for index, valor in enumerate(nro_bin[::-1]):
        suma += int(valor) * (2 ** index)
    print(f"El valor binario {nro_bin} en decimal es: {suma} \n")

def calculadora(opc, nro):
    match opc:
        case 1:
            binario(nro)
        case 2:
            decimal(nro)
        

opciones = {1:"Decimal a Binario", 2:"Binario a Decimal"}
while True:
    opc = int(input(f"Ingrese la opcion que quiere realizar : {opciones} \n Ingrese el 0 paara salir del programa. \n"))
    if opc in opciones: 
        nro = int(input("Ingrese el nro a convertir: \n"))
        calculadora(opc,nro)
    elif opc == 0:
        break
    else:
        print(f"\n Has ingresado un valor incorrecto. ")