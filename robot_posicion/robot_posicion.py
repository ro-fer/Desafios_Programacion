'''
# 🤖  ¿Dónde está el robot?
Calcula la posición final de un **robot** que se encuentra en una cuadrícula bidimensional (ejes **x** e **y**), luego de ejecutar una secuencia de instrucciones de movimiento.

'''
def posicion_robot(posiciones):
    pos_x = 0
    pos_y = 0
    cont = 0
    for indice, pasos in enumerate(posiciones):
        if ( indice % 2) == 0:
            if (cont % 3) == 0:
                pos_y +=pasos
            else:
                pos_y -=pasos
            
        else: 
            if (cont % 3) == 0:
                pos_x +=pasos
            else:
                pos_x -=pasos
        cont+=1
    print(f' El robot🤖  se encuentra en la posicion ( {pos_x} , {pos_y})')

posiciones =[]
print("Hola! Vamos a ver 🤖  ¿Dónde está el robot?, para eso va a ir ingresando los pasos que  vaya dando. Para dar por finalizado ponga '0' ")
while True:
    pos  = int (input("Dio: \n"))
    if pos!=0:
        posiciones.append(pos)
    else:
        break
posicion_robot(posiciones)