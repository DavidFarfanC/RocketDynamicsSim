import numpy as np

# Definición de variables
rho = 1000  # Densidad del agua (kg/m^3)
g = 9.81    # Aceleración debido a la gravedad (m/s^2)
V = 100      # Volumen de la cámara de vacío (m^3)
C_d = 0.7   # Coeficiente de arrastre del cohete
A = 4.52    # Área transversal del cohete (m^2)
m = 20000   # Masa del cohete (kg)
h = 100      # Profundidad de sumersión (m)
I_sp = 300  # Impulso específico del motor en segundos (ejemplo)
h_total = 500  # Altura total objetivo sin asistencia de flotabilidad (m)

# Funciones
def calcular_flotabilidad(rho, g, V):
    return rho * g * V

def calcular_arrastre(rho, C_d, A, v):
    return 0.5 * rho * C_d * A * v**2

def calcular_aceleracion_y_velocidad(F_b, F_d, m, g, h):
    a = (F_b - F_d - m * g) / m
    if a > 0:
        v = np.sqrt(2 * a * h)
    else:
        v = 0  # No hay suficiente flotabilidad para superar el arrastre y la gravedad
    return a, v

def calcular_altura_maxima(v, g):
    return v**2 / (2 * g)

def calcular_ahorro_combustible(E_p, I_sp, g, m_total):
    delta_m = E_p / (I_sp * g)
    ahorro = (1 - delta_m / m_total) * 100
    return ahorro

# Simulación
F_b = calcular_flotabilidad(rho, g, V)
v = 10  # Estimar la velocidad inicial para el cálculo de arrastre
F_d = calcular_arrastre(rho, C_d, A, v)
a, v_final = calcular_aceleracion_y_velocidad(F_b, F_d, m, g, h)
h_max = calcular_altura_maxima(v_final, g)
E_p = m * g * h_max
E_total = m * g * h_total
m_total = E_total / (I_sp * g)
ahorro_combustible = calcular_ahorro_combustible(E_p, I_sp, g, m_total)

# Mostrar resultados
print(f"Fuerza de flotabilidad: {F_b} N")
print(f"Fuerza de arrastre: {F_d} N")
print(f"Aceleración neta: {a} m/s^2")
print(f"Velocidad al emerger: {v_final} m/s")
print(f"Altura máxima alcanzada: {h_max} m")
print(f"Ahorro de combustible: {ahorro_combustible:.2f}%")
