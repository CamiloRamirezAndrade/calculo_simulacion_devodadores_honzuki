# Simulación del efecto de las Puertas Fronterizas en Yurgenschmidt

Modelo numérico para estimar qué atributo (dios/color) domina en un
devorador según su posición dentro de Yurgenschmidt, considerando el
efecto de:

-   Las **puertas fronterizas**
-   El **círculo central de Ewigeliebe (Vida)**

El resultado es un mapa de regiones de dominancia.

------------------------------------------------------------------------

## Modelo físico asumido

El sistema no está definido matemáticamente en la historia, por lo que
se establecen estas hipótesis:

1.  **Ley de efecto** E ∝ 1/d²

2.  **Puertas como arcos**, no puntos.

3.  **Dominancia**: el color del devorador corresponde al efecto mayor.

4.  **Simplificaciones**

    -   Todas las puertas tienen igual densidad de efecto.
    -   Radio de Yurgenschmidt normalizado: R = 1
    -   Radio del círculo de Ewigeliebe: Rc = 1/9
    -   Puertas separadas cada 60°.

------------------------------------------------------------------------

## Cálculo del efecto

Distancia entre devorador (r,a) y un punto del arco:

d² = r² + R² − 2rR cos(θ−a)

Efecto total de una puerta:

E = ∫ dM / d²

La integral cerrada se implementa en:

    F_R(x, r, R, a)

------------------------------------------------------------------------

## Puertas modeladas

  Atributo    Rango angular
  ----------- -----------------
  Tierra      −π/6 → π/6
  Viento      π/6 → π/2
  Oscuridad   π/2 → 5π/6
  Fuego       5π/6 → 7π/6
  Agua        7π/6 → 3π/2
  Luz         3π/2 → 11π/6
  Vida        círculo central

Para **Vida**: - Dentro del círculo → integración de anillo - Fuera →
aproximación como fuente puntual

------------------------------------------------------------------------

## Archivos

### simulacion.py

Simulación Monte Carlo.

-   Genera 1,000,000 posiciones aleatorias.
-   Calcula efectos de todos los atributos.
-   Guarda el dominante.

Salida: simulacion.csv

  Columna   Descripción
  --------- --------------------
  r         radio (0--1)
  a         ángulo (rad)
  mayor     atributo dominante

------------------------------------------------------------------------

### graficar_simulacion.py

Visualización del resultado.

-   Convierte polar → cartesiano
-   Grafica por color
-   Dibuja el círculo exterior

------------------------------------------------------------------------

## Uso

Instalar dependencias:

    pip install numpy pandas matplotlib

Ejecutar simulación:

    python simulacion.py

Graficar:

    python graficar_simulacion.py

------------------------------------------------------------------------

## Propósito

Obtener los límites de influencia cuando resolver analíticamente las
igualdades entre funciones se vuelve complejo.\
La simulación aproxima las fronteras entre atributos mediante muestreo
masivo.
