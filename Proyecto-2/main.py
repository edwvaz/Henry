from fastapi import FastAPI
import pandas as pd
import pydantic


app = FastAPI()

#http://127.0.0.1:8000


# Se ingestan los datos y se crea un dataframe
# The data is ingested and a dataframe is created
df_movies = pd.read_csv(r"C:\Users\Edwin\Desktop\Henry\M7. Proyecto Individual\df_movies_clean")

@app.get("/")
def index():
    return "Las flores son rojas"


# en: inglés

@app.get("/df_movies")
def get_df_movies():
    return df_movies


@app.get('/peliculas_idioma')
def peliculas_idioma(idioma: str):
    cantidad = len(df_movies[df_movies['original_language'] == idioma])
    return f"{cantidad} películas fueron producidas en {idioma}" 

@app.get('/peliculas_duracion')
def peliculas_duracion(pelicula: str):
    pelicula = df_movies[df_movies['title'] == pelicula]
    if len(pelicula) > 0:
        duracion = pelicula['runtime'].values[0]
        anio = pelicula['release_year'].values[0]
        return f"{pelicula['title'].values[0]}. Duración: {duracion}. Año: {anio}"
    else:
        return f"No se encontró la película '{pelicula}'"


@app.get('/franquicia')
def franquicia(franquicia: str):
    peliculas = df_movies[df_movies['belongs_to_collection'] == franquicia]
    cantidad_peliculas = len(peliculas)
    ganancia_total = peliculas['revenue'].sum()
    ganancia_promedio = peliculas['revenue'].mean()
    
    return f"La franquicia '{franquicia}' posee {cantidad_peliculas} película(s), una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"

@app.get('/peliculas_pais')
def peliculas_pais(pais: str):
    peliculas = df_movies[df_movies['production_countries'].apply(lambda x: pais in str(x))]
    cantidad_peliculas = len(peliculas)
    
    return f"Se produjeron {cantidad_peliculas} película(s) en el país '{pais}'"


@app.get('/productoras_exitosas')
def productoras_exitosas(productora: str):
    peliculas = df_movies[df_movies['production_companies'].apply(lambda x: isinstance(x, list) and productora in x)]
    cantidad_peliculas = len(peliculas)
    revenue_total = peliculas['revenue'].sum()

    return f"La productora '{productora}' ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} película(s)"

@app.get('/productoras_exitosas')
def productoras_exitosas(productora: str):
    peliculas = df_movies[df_movies['production_companies'].str.contains(productora, na=False)]
    cantidad_peliculas = len(peliculas)
    revenue_total = peliculas['revenue'].sum()

    return f"La productora '{productora}' ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} película(s)"



@app.get('/get_director')
def get_director(nombre_director):
    movies_list = []
    total_return = 0
    count = 0

    for _, movie in df_movies.iterrows():
        directors = movie['directors']

        if nombre_director in directors:
            title = movie['title']
            release_date = movie['release _date']
            individual_return = movie['return']
            costo = movie['budget']
            ganancia = movie['revenue']

            movie_details = {
                'title': title,
                'release _date': release_date,
                'individual_return': individual_return,
                'costo': costo,
                'ganancia': ganancia
            }

            total_return += individual_return
            count += 1

            movies_list.append(movie_details)

    exito_director = total_return / count if count > 0 else 0
    movies_list.insert(0, {'exito_director': exito_director})

    return movies_list


























































