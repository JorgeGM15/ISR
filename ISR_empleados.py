# Alumno: Gómez Meza Jorge Ángel
# Grupo 1 - Módulo 1: Inducción

import pandas as pd
import numpy as np

# 1. Definimos los parámetros de la tabla ISR
limite_inferior = 18837.38
porcentaje_excedente = 0.2352 

# 2. Generamos datos ficticios (aleatorios) para 10 empleados
np.random.seed(1) # "Semilla" para reproducibilidad (Nos ayudará a que la secuencia de números "aleatorios" que genere NumPy sea exactamente la misma)
n_empleados = 10
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

datos_empleados = {
    'nombre': [f'Empleado {i+1}' for i in range(n_empleados)],
    'direccion': [f'Calle {i+1}, CDMX' for i in range(n_empleados)],
    'telefono': [f'555555{1000+i}' for i in range(n_empleados)]
}

# Generamos salarios mensuales aleatorios dentro del rango
for mes in meses:
    datos_empleados[mes] = np.random.uniform(18837.38, 38775.38, n_empleados).round(2) #Redondea a dos cifras decimales.

# 3. Creamos el DataFrame principal
df_salarios = pd.DataFrame(datos_empleados)


# 4. Calculamos el ISR mensual con la fórmula
df_isr = df_salarios[['nombre']].copy() # Usamos .copy() para asegurar que creamos una tabla nueva e independiente y evitar problemas en el DataFrame original.

for mes in meses:
    excedente = df_salarios[mes] - limite_inferior
    isr_mensual = excedente * porcentaje_excedente 
    df_isr[f'isr_{mes}'] = isr_mensual.round(2)


# 5. Calculamos los totales anuales
df_anual = df_salarios[['nombre']].copy()

# Sumamos todos los salarios mensuales para obtener el total anual
df_anual['salario_anual'] = df_salarios[meses].sum(axis=1).round(2) # Suma los valores, pero gracias a axis=1, lo hace de forma horizontal (a lo largo de las filas).

# Sumamos todas las retenciones de ISR mensuales para el total anual
df_anual['retencion_isr_anual'] = df_isr[[f'isr_{mes}' for mes in meses]].sum(axis=1).round(2)


# Impresión de los Resultados
print("--- DataFrame de Salarios Mensuales de Empleados ---")
print(df_salarios.to_string()) # Lo que hace df_salarios.to_string() es que convierte el DataFrame completo a texto (string).
print("\n" + "\n")

print("--- DataFrame de Retención de ISR Mensual ---")
print(df_isr.to_string())
print("\n" + "\n")

print("--- Resumen Anual por Empleado ---")
print(df_anual.to_string())