import numpy as np
import matplotlib.pyplot as plt

# Definición de constantes
rho = 1000  # Densidad del agua (kg/m^3)
g = 9.81    # Aceleración debido a la gravedad (m/s^2)
C_d = 0.7   # Coeficiente de arrastre del cohete
A = 4.52    # Área transversal del cohete (m^2)
m = 20000   # Masa del cohete (kg)
velocidad_inicial = 10  # Velocidad inicial estimada para cálculo de arrastre

# Rangos de variación
volumenes = np.linspace(50, 300, 11)  # Volumen de 50 m^3 a 150 m^3
profundidades = np.linspace(50, 150, 11)  # Profundidad de 50 m a 150 m

# Preparación de la matriz de resultados
resultados = np.zeros((len(volumenes), len(profundidades), 2))  # Última dimensión para velocidad y altura

# Funciones de cálculo
def calcular_flotabilidad(V):
    return rho * g * V

def calcular_arrastre(v):
    return 0.5 * rho * C_d * A * v**2

def calcular_aceleracion_y_velocidad(F_b, F_d, h):
    a = (F_b - F_d - m * g) / m
    if a > 0:
        v = np.sqrt(2 * a * h)
    else:
        v = 0
    return a, v

def calcular_altura_maxima(v):
    return v**2 / (2 * g)

# Iteración sobre volumen y profundidad
for i, V in enumerate(volumenes):
    for j, h in enumerate(profundidades):
        F_b = calcular_flotabilidad(V)
        F_d = calcular_arrastre(velocidad_inicial)
        a, v_final = calcular_aceleracion_y_velocidad(F_b, F_d, h)
        h_max = calcular_altura_maxima(v_final)
        resultados[i, j, 0] = v_final  # Velocidad al emerger
        resultados[i, j, 1] = h_max   # Altura máxima alcanzada

# Gráficos
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
X, Y = np.meshgrid(profundidades, volumenes)

# Velocidad al emerger
cs = ax[0].contourf(X, Y, resultados[:, :, 0], cmap='viridis')
cbar = fig.colorbar(cs, ax=ax[0], orientation='vertical')
ax[0].set_title('Velocidad al Emerger (m/s)')
ax[0].set_xlabel('Profundidad (m)')
ax[0].set_ylabel('Volumen (m^3)')

# Altura máxima alcanzada
cs = ax[1].contourf(X, Y, resultados[:, :, 1], cmap='viridis')
cbar = fig.colorbar(cs, ax=ax[1], orientation='vertical')
ax[1].set_title('Altura Máxima Alcanzada (m)')
ax[1].set_xlabel('Profundidad (m)')
ax[1].set_ylabel('Volumen (m^3)')

plt.tight_layout()
plt.show()
