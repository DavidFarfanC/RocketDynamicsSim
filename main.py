import numpy as np

# Definición de variables
rho = 1000  # Densidad del agua (kg/m^3)
g = 9.81    # Aceleración debido a la gravedad (m/s^2)
V = 100      # Volumen de la cámara de vacío (m^3)
C_d = 0.7   # Coeficiente de arrastre del cohete
A = 4.52    # Área transversal del cohete (m^2)
m = 20000   # Masa del cohete (kg)
h = 100      # Profundidad de sumersión (m)

# Cálculo de la Fuerza de Flotabilidad
def calcular_flotabilidad(rho, g, V):
    return rho * g * V

# Cálculo de la Fuerza de Arrastre
def calcular_arrastre(rho, C_d, A, v):
    return 0.5 * rho * C_d * A * v**2

# Determinación de la Aceleración Neta y Velocidad al Emerger
def calcular_aceleracion_y_velocidad(F_b, F_d, m, g, h):
    a = (F_b - F_d - m * g) / m
    v = np.sqrt(2 * a * h)
    return a, v

# Cálculo de la Altura Máxima Alcanzada
def calcular_altura_maxima(v, g):
    return v**2 / (2 * g)

# Simulación
F_b = calcular_flotabilidad(rho, g, V)
v = 10  # Estimar la velocidad inicial para el cálculo de arrastre
F_d = calcular_arrastre(rho, C_d, A, v)
a, v_final = calcular_aceleracion_y_velocidad(F_b, F_d, m, g, h)
h_max = calcular_altura_maxima(v_final, g)

# Mostrar resultados
print(f"Fuerza de flotabilidad: {F_b} N")
print(f"Fuerza de arrastre: {F_d} N")
print(f"Aceleración neta: {a} m/s^2")
print(f"Velocidad al emerger: {v_final} m/s")
print(f"Altura máxima alcanzada: {h_max} m")
