import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("videojuegos.csv")


# Ordenar los juegos por ventas en Europa de mayor a menor
df_sorted = df.sort_values(by='EU_Sales', ascending=False)

# Seleccionar los 5 juegos con mayores ventas en Europa
top_5_games = df_sorted.head(5)

# Crear el grafico de barras
plt.bar(top_5_games['Genre'], top_5_games['EU_Sales'], color='gray')

# Añadir títulos y etiquetas
plt.title('Top 5 generos de videojuegos con mayores ventas en europa')
plt.xlabel('generos')
plt.ylabel('Ventas en Europa (millones)')

# Mostrar el gráfico
plt.show(block=True)

#este codigo nos permite crear un grafico de barras para poder ver cual ha sido el genero de videojuegos que mas ha vendido.