import numpy as np
import random
import math
import csv

# ---------------- FUNCIONES ----------------

def normalizar_angulo(theta):
    return (theta + np.pi) % (2 * np.pi) - np.pi


def F_R(x, r, R, a):
    return (2 * R * np.arctan((abs(r + R) * np.tan((x - a) / 2)) / abs(r - R))) \
           / (abs(r - R) * abs(r + R))


def integrar_funcion(x1, x2, r, R, a):
    x1n = normalizar_angulo(x1 - a)
    x2n = normalizar_angulo(x2 - a)

    if x2n >= x1n:
        return F_R(x2n + a, r, R, a) - F_R(x1n + a, r, R, a)
    else:
        eps = 1e-8
        parte1 = F_R(np.pi - eps + a, r, R, a) - F_R(x1n + a, r, R, a)
        parte2 = F_R(x2n + a, r, R, a) - F_R(-np.pi + eps + a, r, R, a)
        return parte1 + parte2

# ---------------- LÍMITES ----------------

pi = np.pi

limites = {
    "tierra":    [-pi/6,  pi/6],
    "viento":    [ pi/6,  pi/2],
    "oscuridad": [ pi/2,  5*pi/6],
    "fuego":     [5*pi/6, 7*pi/6],
    "agua":      [7*pi/6, 3*pi/2],
    "luz":       [3*pi/2, 11*pi/6],
}

# ---------------- SIMULACIÓN ----------------

N = 1000000  # un millón

with open("simulacion.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["r", "a", "mayor"])  # encabezado

    for _ in range(N):

        r = random.random()
        a = random.random() * 2 * pi

        efectos = {}

        for nombre, (x1, x2) in limites.items():
            efectos[nombre] = integrar_funcion(
                normalizar_angulo(x1),
                normalizar_angulo(x2),
                r, 1, a
            )

        # VIDA
        if r < (1/9):
            efectos["vida"] = integrar_funcion(-pi+1e-8, pi-1e-8, r, 1/9, 0)
        else:
            efectos["vida"] = ((2/9) * pi)/(r**2)

        mayor = max(efectos, key=efectos.get)

        writer.writerow([r, a, mayor])

print("Simulación terminada.")

