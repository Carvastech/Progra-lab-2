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

#En esta grafica, se pueden observar cuales son los animes 5 animes con mas capitulos listados en la plataforma crunchyroll, asi mismo, este top cinco, sirve para ver cual es el porcentaje total de capitulos abarcados
#por anime, para asi poder ver datos como la diferencia en cuanto a porcentaje de capitulos unos con otros, y ver que en este caso, el top 1 tiene una diferencia casi del 50%. Tambien nos puede servir para ver cuanto 
#tiempo un anime estuvo en emision, ya que entre mas capitulos posean, significa que mas tiempo han estado al aire.
