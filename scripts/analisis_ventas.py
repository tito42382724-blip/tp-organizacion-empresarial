
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../datos/ventas.csv')

df['venta']=df['cantidad']*df['precio']

ventas_totales=df['venta'].sum()

print("Ventas:",ventas_totales)
