"""
Implementa un programa que analice un conjunto de tweets almacenados en una lista. 
Crea una función lambda que filtre los tweets que contienen una palabra clave específica. 
Luego, utiliza una lista de comprensión para generar una nueva lista con los tweets que coinciden con la palabra clave.
"""

# La palabra clave será 'Python'
lista_tweets = [
    "¡Hoy aprendí a programar en Python y estoy emocionado! 🐍 #Python #Programación",
    "El clima en la ciudad está perfecto para salir a pasear 🌞 #BuenTiempo #Paseo",
    "Me encanta cocinar nuevas recetas en mi tiempo libre 🍳 #Cocina #Recetas",
    "Python es un lenguaje de programación versátil y poderoso. ¡Me encanta! #Python #Programación",
    "Disfrutando de un buen libro en mi rincón favorito 📖 #Lectura #Relajación",
    "¡Nuevo tutorial de Python en mi blog! ¡No te lo pierdas! #Python #Programación #Blog",
    "Mi gato se ha convertido en mi compañero de trabajo durante la cuarentena 😺 #TrabajoDesdeCasa #Gato",
    "Hoy he probado una nueva receta de pasta y ha quedado deliciosa 🍝 #Cocina #Recetas",
    "¿Alguien sabe cómo resolver un problema de bucle en Python? ¡Necesito ayuda! #Python #Programación",
    "La programación en Python me resulta fascinante. ¡Siempre hay algo nuevo por descubrir! 🐍 #Python #Programación,,,,"
]

# Palabra clave para filtrar
palabra_clave = "Python"

# Usar una función lambda para filtrar los tweets que contienen la palabra clave. El argumento sería tweet.
tweets_filtrados = list(filter(lambda tweet: palabra_clave in tweet, lista_tweets))
"""
Lambda está heredando el argumento de filter, que en este caso es lista_tweet. En este caso lambda se está comportando como el hijo y filter como el padre.
"""

"""
Esta línea de código utiliza la función filter en conjunto con una función lambda para filtrar elementos de la lista lista_tweets y almacenar los elementos que cumplan con una condición específica en la lista tweets_filtrados. Aquí está el desglose:

filter: filter es una función incorporada en Python que se utiliza para filtrar elementos de una secuencia (en este caso, una lista) según una condición dada.

lambda tweet: palabra_clave in tweet: Esto define una función lambda que toma un argumento tweet y verifica si la palabra_clave está contenida en ese tweet. Devolverá True si la palabra_clave está en el tweet, y False en caso contrario.

lista_tweets: Esta es la lista de tweets en la que deseas realizar el filtrado.

list(...): Se utiliza para convertir el resultado de filter en una lista. filter retorna un iterable, y al envolverlo en list(...), lo convertimos en una lista para que sea más fácil de manejar.
"""

# Imprimir los tweets filtrados
for tweet in tweets_filtrados:
    print(tweet)
