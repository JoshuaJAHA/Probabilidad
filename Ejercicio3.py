# Utilizando python haz los siguientes puntos y sube tu programa al classroom
# TAREA 07 DE PROBABILIDAD
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom, norm

# Variables para el reparto binomial
num_ensayos = 1000
prob_exito = 0.3

# Obtener la p.m.f del reparto binomial
valores_binom = np.arange(0, num_ensayos + 1)
pmf_binom = binom.pmf(valores_binom, num_ensayos, prob_exito)

# Graficar la p.m.f del reparto binomial
plt.figure(figsize=(10, 6))
plt.stem(valores_binom, pmf_binom, markerfmt='o', linefmt='blue', basefmt=" ")
plt.title('PMF de X ~ Binomial(1000, 0.3)')
plt.xlabel('X')
plt.ylabel('Probabilidad')
plt.show()

# Convertir la variable X a Y
valores_transformados = (valores_binom - 300) / np.sqrt(210)

# Graficar la p.m.f convertida
plt.figure(figsize=(10, 6))
plt.stem(valores_transformados, pmf_binom, markerfmt='o', linefmt='green', basefmt=" ")
plt.title('PMF de Y = (X - 300) / sqrt(210)')
plt.xlabel('Y')
plt.ylabel('Probabilidad')
plt.show()

# Obtener la p.m.f del reparto normal estándar
valores_norm = np.linspace(-5, 5, 1000)
pmf_norm = norm.pdf(valores_norm, 0, 1)

# Graficar la p.m.f del reparto normal estándar
plt.figure(figsize=(10, 6))
plt.plot(valores_norm, pmf_norm, color='red')
plt.title('PMF de Z ~ Normal(0, 1)')
plt.xlabel('Z')
plt.ylabel('Probabilidad')
plt.show()

# d)¿Que puedes observar de las graficas del inciso b) y del inciso c)?

# Grafica B)  Muestra una distribución discreta derivada de una variable aleatoria binomial X a través de una transformación.
# Aunque la forma general de la distribución puede permanecer, la escala y la ubicación de la distribución cambian debido a la transformación.

# Grafica C) Representa una distribución normal estándar, que es continua y simétrica, centrada en 0 y con una desviación estándar de 1.

#La gráfica b) es discreta y puede retener ciertas características de la distribución binomial original, mientras que la gráfica c) es una distribución continua. 
