
# importar librerias
import pandas as pd
import numpy as np

print("analisis de datos alumnos Ian gutierrez NC=0091")
clientes = {
"Cliente": ["mark", "yonaa", "yonaa", "micky", "micky", "lucas"],
"Antiguedad_Meses": [2, 36, 12, 5, 48, 1],
"Gasto_Mensual": [29.99, 89.99, 59.99, 19.99, 110.00, 49.99],
"Cancela_Servicio": [True, False, False, True, False, True]
}
df = pd.DataFrame(clientes)
print(df)
print("-+-+-+-+- agrupar una sola columna cliente -+-+-+-+-")
agrupado = df.groupby('Cliente')
print(agrupado)
print("-+-+-+-+- promedio -+-+-+-+-")
# antiguedad promedio por cliente
print(agrupado['Antiguedad_Meses'].mean())
print("-+-+-+-+- antiguedad maxima-+-+-+-+-")
# antiguedad maxima en cada cliente
print(agrupado['Antiguedad_Meses'].max())
print("+-+-IAN+-+-+- segunda parte -+-+-+0091-+-+")
print("Agregacion multiples")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Gasto_Mensual'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)
print("Agrupación por varias columnas")
print("Agrega columna al dataframe")
print("Columna Team --> equipo")
df['Equipo'] = ['A', 'B', 'A', 'B', 'A', 'B']
agrupado_múltiple = df.groupby(['Cliente', 'Equipo'])['Gasto_Mensual'].mean()
print(agrupado_múltiple)
