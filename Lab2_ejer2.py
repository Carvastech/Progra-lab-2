import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("paises.csv")


# Seleccionar los 10 paises mas poblados
top_10 = df.nlargest(10, 'Population')

# Crear el grafico de lineas
plt.plot(top_10['Country'], top_10['Population'], marker='o', label='Top 10 paises')

# Añadir títulos y etiquetas
plt.title('Top 10 paises mas poblados')
plt.xlabel('paises')
plt.ylabel('poblacion (millones)')

# Mostrar el gráfico
plt.show(block=True)

#Este grafico de lineas esta hecho para que, de una lista de los paises, podamos sacar y saber cuales son los 10 paises mas habitados del mundo