import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("simulacion.csv")

# Convertir de polar (r,a) a cartesiano
x = df["r"] * np.cos(df["a"])
y = df["r"] * np.sin(df["a"])

# Mapa de colores
colores = {
    "tierra": "red",
    "viento": "yellow",
    "oscuridad": "black",
    "fuego": "blue",
    "agua": "green",
    "luz": "orange",
    "vida": "white"
}

# Crear figura
plt.figure(figsize=(8,8))
plt.gca().set_facecolor("gray")  # fondo para ver puntos blancos

# Graficar por categoría
for categoria, color in colores.items():
    mask = df["mayor"] == categoria
    plt.scatter(x[mask], y[mask], s=1, c=color, label=categoria)

# Dibujar borde del círculo r=1
theta = np.linspace(0, 2*np.pi, 500)
plt.plot(np.cos(theta), np.sin(theta))

plt.axis("equal")
plt.axis("off")
plt.legend(markerscale=6, bbox_to_anchor=(1.05, 1))
plt.show()
