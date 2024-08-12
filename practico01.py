# practico01.py

# Importación de librerías necesarias
import numpy as np
import pandas as pd

# Generar datos de estatura y peso controlados
np.random.seed(42)  # Fijamos una semilla para asegurar la reproducibilidad de los resultados
estaturas = np.random.uniform(1.4, 2.0, 100)  # Generamos 100 estaturas aleatorias entre 1.4m y 2.0m
pesos = []  # Lista para almacenar los pesos generados

# Bucle para generar pesos aleatorios controlados según la estatura
for estatura in estaturas:
    # Calcular el peso mínimo y máximo usando el IMC saludable (18.5 a 24.9)
    peso_min = 18.5 * (estatura ** 2)  # Peso mínimo según IMC de 18.5
    peso_max = 24.9 * (estatura ** 2)  # Peso máximo según IMC de 24.9
    # Generar un peso aleatorio entre el peso mínimo y máximo calculado
    peso = np.random.uniform(peso_min, peso_max)
    pesos.append(peso)  # Añadir el peso a la lista de pesos

# Crear un DataFrame con los datos de estatura y peso
data = pd.DataFrame({
    'Estatura (m)': estaturas,
    'Peso (kg)': pesos
})

# Guardar los datos en un archivo CSV
data.to_csv('datos_peso_estatura.csv', index=False)
