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

#Este grafico nos muestra cuales son los 10 paises mas poblados del mundo. Esto nos deja saber diferentes cosas, como la diferencia que tienen los paises entre si en cuanto a su numero de poblacion, tambien podemos
#ver cuando son los continentes con paises mas poblados, en comparacion a los demas continentes, siendo asia el continente con los paises mas poblados. Tambien podria ayudar a realizar analisis para lanzar algun 
#producto al mercado, ya que a mayor poblacion, mayor es la probabilidad de que un producto sea rentable, siendo por esto, que China es una de las prioridades al lanza productos al mercado.
