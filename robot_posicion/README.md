# 🤖  ¿Dónde está el robot?

## 🧠 Consigna

Calcula la posición final de un **robot** que se encuentra en una cuadrícula bidimensional (ejes **x** e **y**), luego de ejecutar una secuencia de instrucciones de movimiento.

---

## 🔧 Reglas

- El robot comienza en la coordenada **(0, 0)**, mirando hacia el eje **positivo de Y**.
- Se le entrega una **lista de enteros** (positivos o negativos) que representan pasos a avanzar o retroceder.
- **Cada número de la lista indica un movimiento en línea recta**, seguido de un giro de **90° en sentido antihorario** (contra las agujas del reloj).
- **Sentido del giro antihorario**:
  - Mirando al norte (↑) pasa a oeste (←)
  - Luego sur (↓)
  - Luego este (→)
  - Y nuevamente norte (↑)
- Si el valor es negativo, el robot camina hacia atrás, pero luego igual gira.
- Al finalizar todos los movimientos, el programa debe devolver la coordenada final del robot.

---
