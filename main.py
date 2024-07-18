import numpy as np

# Constantes del cohete y misión
m = 20000  # masa estimada del cohete en kg
g = 9.81   # aceleración de la gravedad en m/s^2
I_sp = 450  # impulso específico del motor en segundos (estimado)
h_max = 350  # altura alcanzada por flotabilidad en metros
h_total = 105000  # altura total típica de la misión en metros

# Calcular energía potencial ganada por la flotabilidad
E_p = m * g * h_max

# Masa de combustible ahorrada
masa_combustible_ahorrada = E_p / (I_sp * g)

# Energía total necesaria para la misión completa
E_total = m * g * h_total

# Masa de combustible total necesaria
masa_combustible_total = E_total / (I_sp * g)

# Ahorro en porcentaje
ahorro_porcentaje = (masa_combustible_ahorrada / masa_combustible_total) * 100

# Mostrar el ahorro en porcentaje
print(f"Ahorro de combustible en porcentaje: {ahorro_porcentaje:.2f}%")
