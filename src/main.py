import numpy as np
import pandas as pd
import config
import matplotlib.pyplot as plt

def creacion_dfm(dbc):
    dfm = pd.read_sql("SELECT *  FROM MOVIE", con=dbc)
    return dfm

def creacion_dft(dbc):
    dft = pd.read_sql("SELECT *  FROM TV_SHOW", con=dbc)
    return dft

def minimun(df, s):
    return np.min(df[s])

def maximun(df, s):
    return np.max(df[s])

def average_movie(dfm):
    return np.average(dfm["duration"])

def average_tv_show(dft):
    return np.average(dft["duration"])

def std_movie(dfm):
    return np.std(dfm["duration"])

def std_tv_show(dft):
    return np.std(dft["duration"])

def count(df):
    return df.notnull().sum()

def count_null(df):
    return df.isnull().sum()

def numero_muestras(dfm, dft):
    print("Número de muestras (valores distintos de missing).")
    print(count(dfm) + count(dft))
    print()

def medias(dfm, dft):
    print("Media de la columna duración para peliculas")
    print("{:.2f}".format(average_movie(dfm)))
    print("Media de la columna duración para tv shows")
    print("{:.2f}".format(average_tv_show(dft)))
    print()

def desviaciones(dfm, dft):
    print("Desviación estándar de la columna duración en peliculas.")
    print("{:.2f}".format(std_movie(dfm)))
    print("Desviación estándar de la columna duración en tv shows.")
    print("{:.2f}".format(std_tv_show(dft)))
    print()

def duraciones_peliculas(dfm):
    print("Duración mínima en películas")
    print(minimun(dfm, "duration"))
    print("Duración máxima en películas")
    print(maximun(dfm, "duration"))
    print()

def duraciones_series(dft):
    print("Duración mínima en tv shows")
    print(minimun(dft, "duration"))
    print("Duración máxima en tv shows")
    print(maximun(dft, "duration"))
    print()

def anhos_peliculas(dfm):
    print("Año mínimo de lanzamiento de pelicula")
    print(minimun(dfm, "release_year"))
    print("Año máximo de lanzamiento de pelicula")
    print(maximun(dfm, "release_year"))
    print()

def anhos_series(dft):
    print("Año mínimo de lanzamiento de tv shows")
    print(minimun(dft, "release_year"))
    print("Año máximo de lanzamiento de tv shows")
    print(maximun(dft, "release_year"))
    print()

def observaciones_peliculas(dfml, dfmc):
    print("Número de observaciones de películas de más de 90'")
    print(count(dfml['duration']))
    print("Número de observaciones de películas de menos de 90'")
    print(count(dfmc['duration']))


def observaciones_series(dftl,dftc):
    print("Número de observaciones de tv shows de más de 2 temporadas")
    print(count(dftl['duration']))
    print("Número de observaciones de tv shows de 1 o 2 temporadas")
    print(count(dftc['duration']))
    print()


def ausentes_peliculas(dfml, dfmc):
    print("Número de valores ausentes (missing) de películas de más de 90'")
    print(count_null(dfml['duration']))
    print("Número de valores ausentes (missing) de películas de menos de 90'")
    print(count_null(dfmc['duration']))


def ausentes_series(dftl,dftc):
    print("Número de valores ausentes (missing) de tv shows de más de 2 temporadas")
    print(count_null(dftl['duration']))
    print("Número de valores ausentes (missing) de 1 o 2 temporadas")
    print(count_null(dftc['duration']))
    print()

def mediana_peliculas(dfml, dfmc):
    print("Mediana de películas de más de 90'")
    print(np.median(dfml['duration']))
    print("Mediana de películas de menos de 90'")
    print(np.median(dfmc['duration']))


def mediana_series(dftl,dftc):
    print("Mediana de tv shows de más de 2 temporadas")
    print(np.median(dftl['duration']))
    print("Mediana de 1 o 2 temporadas")
    print(np.median(dftc['duration']))
    print()


def media_peliculas(dfml, dfmc):
    print("Media de películas de más de 90'")
    print("{:.2f}".format(np.average(dfml['duration'])))
    print("Media de películas de menos de 90'")
    print("{:.2f}".format(np.average(dfmc['duration'])))


def media_series(dftl,dftc):
    print("Media de tv shows de más de 2 temporadas")
    print("{:.2f}".format(np.average(dftl['duration'])))
    print("Media de 1 o 2 temporadas")
    print("{:.2f}".format(np.average(dftc['duration'])))
    print()


def varianza_peliculas(dfml, dfmc):
    print("Varianza de películas de más de 90'")
    print("{:.2f}".format(np.var(dfml['duration'])))
    print("Varianza de películas de menos de 90'")
    print("{:.2f}".format(np.var(dfmc['duration'])))


def varianza_series(dftl,dftc):
    print("Varianza de tv shows de más de 2 temporadas")
    print("{:.2f}".format(np.var(dftl['duration'])))
    print("Varianza de 1 o 2 temporadas")
    print("{:.2f}".format(np.var(dftc['duration'])))
    print()


def duraciones_peliculas_largas(dfml):
    print("Duración mínima en películas de más de 90'")
    print(minimun(dfml, "duration"))
    print("Duración máxima en películas de más de 90'")
    print(maximun(dfml, "duration"))
    print()


def duraciones_peliculas_cortas(dfmc):
    print("Duración mínima en películas de menos de 90'")
    print(minimun(dfmc, "duration"))
    print("Duración máxima en películas de menos de 90'")
    print(maximun(dfmc, "duration"))
    print()


def duraciones_series_largas(dftl):
    print("Duración mínima en tv shows de más de 2 temporadas")
    print(minimun(dftl, "duration"))
    print("Duración máxima en tv shows de más de 2 temporadas")
    print(maximun(dftl, "duration"))
    print()


def duraciones_series_cortas(dftc):
    print("Duración mínima en tv shows de 1 o 2 temporadas")
    print(minimun(dftc, "duration"))
    print("Duración máxima en tv shows de 1 o 2 temporadas")
    print(maximun(dftc, "duration"))
    print()

def grafico_visionados(title):
    # plt.tight_layout()
    if (title == 'Peliculas'):
        df = pd.read_sql("SELECT movie.show_id,movie.title,count(movie.show_id) as count FROM movie,viewing WHERE movie.show_id=viewing.show_id group by show_id;",
        con=dbc)
    elif (title == 'Series'):
        df = pd.read_sql(
        "SELECT tv_show.show_id,tv_show.title,count(tv_show.show_id) as count FROM tv_show,viewing WHERE tv_show.show_id=viewing.show_id group by show_id;",
        con=dbc)
    aux = "Top 10 visionados por " + title
    dfvh = df.sort_values(by="count").tail(10)
    ax = dfvh.plot.barh(x='title',rot=0,figsize=(10,10),xlabel=title,ylabel="Visionados", title=aux, legend="Visionados")
    ax.legend(["Visionados"])
    plt.tight_layout()
    plt.show()

def grafico_medias_peliculas():
    dfgt = pd.read_sql(
        "SELECT movie.show_id, movie.title, count(movie.show_id) as count FROM movie,viewing WHERE movie.show_id=viewing.show_id AND movie.duration < 90 group by movie.show_id;",
        con=dbc)
    dflt =pd.read_sql(
        "SELECT movie.show_id, movie.title, count(movie.show_id) as count FROM movie,viewing WHERE movie.show_id=viewing.show_id AND movie.duration >= 90 group by movie.show_id;",
        con=dbc)
    media_gt = np.average(dfgt["count"])
    media_lt = np.average(dflt["count"])
    df = pd.DataFrame({'title': ['Peliculas de mas de 90 minutos', 'Peliculas de menos de 90 minutos'], 'media': [media_gt, media_lt]})
    ax = df.plot.barh(x='title',rot=0,figsize=(10,10),xlabel="Duracion de peliculas",ylabel="Visionados", title="Media de visionados")
    ax.legend(["Visionados"])
    plt.tight_layout()
    plt.show()

def grafico_medias_series():
    dfgt = pd.read_sql(
        "SELECT tv_show.show_id, tv_show.title, count(tv_show.show_id) as count FROM tv_show,viewing WHERE tv_show.show_id=viewing.show_id AND tv_show.duration <= 2 group by tv_show.show_id;",
        con=dbc)
    dflt =pd.read_sql(
        "SELECT tv_show.show_id, tv_show.title, count(tv_show.show_id) as count FROM tv_show,viewing WHERE tv_show.show_id=viewing.show_id AND tv_show.duration > 2 group by tv_show.show_id;",
        con=dbc)
    media_gt = np.average(dfgt["count"])
    media_lt = np.average(dflt["count"])
    df = pd.DataFrame({'title': ['Series de mas de 2 temporadas', 'Series de menos de 2 temporadas'], 'media': [media_gt, media_lt]})
    ax = df.plot.barh(x='title',rot=0,figsize=(10,10),xlabel="Duracion de Series",ylabel="Visionados", title="Media de visionados")
    ax.legend(["Visionados"])
    plt.tight_layout()
    plt.show()




if __name__ == '__main__':
    #Inicializamos la conexión con la BBDD
    dbc = config.get_connection(2);

    # db.import_data(dbc, "..\\res\\data.txt") # Método que reinicia las tablas y genera un script SQL para insertar los datos

    #Creación de los dataframes
    dfm = creacion_dfm(dbc)
    dft = creacion_dft(dbc)

    print("Ejercicio 2:")
    numero_muestras(dfm, dft)
    medias(dfm, dft)
    desviaciones(dfm, dft)

    duraciones_peliculas(dfm)
    duraciones_series(dft)

    anhos_peliculas(dfm)
    anhos_series(dft)
    print("Fin Ejercicio 2")

    print("Ejercicio 3:")
    dfml = dfm[dfm['duration'] >= 90]
    dfmc = dfm[dfm['duration'] < 90]

    dftl = dft[dft['duration'] >= 3]
    dftc = dft[dft['duration'] < 3]

    observaciones_peliculas(dfml, dfmc)
    observaciones_series(dftl,dftc)

    ausentes_peliculas(dfml, dfmc)
    ausentes_series(dftl,dftc)

    mediana_peliculas(dfml, dfmc)
    mediana_series(dftl,dftc)

    media_peliculas(dfml, dfmc)
    media_series(dftl,dftc)

    varianza_peliculas(dfml, dfmc)
    varianza_series(dftl,dftc)

    duraciones_peliculas_largas(dfml)
    duraciones_peliculas_cortas(dfmc)
    duraciones_series_largas(dftl)
    duraciones_series_cortas(dftc)
    print()
    print("Fin Ejercicio 3")

    # Ejercicio 4:
    #Métodos de la clase insert_users para crear las tablas de la BBDD referentes al ejercicio 4

    #iu.create_tables_users(dbc)    #Metodo que crea las tablas de usuario y de visionado en la base de datos
    #iu.generar_usuario(dbc)        #Método que imprime por consola sentencias SQL de inserción de los usuarios
    #iu.generar_visionados(dbc)     #Método que genera un script SQL para insertar datos en la base de datos de visionados


    print("Ejercicio 5:")
    grafico_visionados("Peliculas")
    grafico_visionados("Series")
    grafico_medias_peliculas()
    grafico_medias_series()