import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("animes.csv")

# Ordenar los animes por numero de capitulos
df_sorted = df.sort_values(by='episodes', ascending=False)

# Seleccionar los 5 animes con mas capitulos en Crunchyroll
top_5_animes = df_sorted.head(5)

# Crear gráfico de pastel
plt.pie(top_5_animes['episodes'], 
        labels=top_5_animes['anime'],  
        autopct="%1.1f%%", 
        colors=['red', 'blue', 'lightblue', 'lightgreen', 'yellow'])

plt.title('Top 5 Animes con mas capitulos listados en Crunchyroll')
plt.show()

#En este codigo, realizamos un grafico el cual, de los animes listados en la plataforma Crunchyroll, podamos ver cuales son los 5 animes con mas
#capitulos en la plataforma, asi mismo, teniendo los porcentajes de capitulos que tiene cada anime dentro de este propio top 5.