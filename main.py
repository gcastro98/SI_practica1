import mysql.connector
import numpy as np
import pandas as pd
import db_start as db
import config
import insert_users as iu


def get_connection():
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        passwd="Lechugaa10016",
        auth_plugin='mysql_native_password',
        database='table_practica'
    )
    return db_connection


'''def load_to_dataframeGeneral(db_conn):
    df = pd.read_sql("SELECT * FROM table_practica2 WHERE typeShow =\"TV Show\"", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return df
'''
'''
def load_to_dataframeSeries(db_conn):
    dfSeries = pd.read_sql("SELECT * FROM TV_SHOW", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return dfSeries


def load_to_dataframePeliculas(db_conn):
    dfPeliculas = pd.read_sql("SELECT * FROM MOVIE", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return dfPeliculas


connection = get_connection()
dfShows = load_to_dataframeSeries(connection)
dfMovies = load_to_dataframePeliculas(connection)

print(dfShows)
print(dfMovies)

'''
'''def numeroMuestras(dfGeneral):
    return pd.notna(dfGeneral)


withoutMissing = numeroMuestras(dfGeneral)


# print(withoutMissing)

def calculo_duracionPelis(dfMovies):
    n = len(dfMovies.index)
    t = 0
    for i in range(0, 500):
        x = dfMovies.at[i, 'duration']
        a = x.split(" ")
        print(i, a)
        dur = int(a[0])
        t += dur
    print(t)


calculo_duracionPelis(dfMovies)
print(dfMovies['duration'])

def calculo_duracionSeries(dfShows):
    duracion = dfShows.get("duration")
    min, season = []
    for o in duracion:def calculo_duracionSeries(dfShows):
    duracion = dfShows.get("duration")
    min, season = []
    for o in duracion:
        aux = int(o.split(" ")[0])
        if " min" in o:
            min.append(aux)
        if " Seasons" in o:
            season.append(aux)

    print("\nPeliculas:")
    print(f'Valor medio de duracion de las peliculas: {np.average(min):,.2f} minutos')
    print(f'Valor de la desviacion tipica de la duracion de las peliculas: {np.std(min):,.2f}')
    print("\nTVShows:")
    print(f'Valor medio de duracion de las TVSHOWS: {np.average(season):,.2f} temporadas')
    print(f'Valor de la desviacion tipica de la duracion de las TVSHOWS: {np.std(season):,.2f}')

if __name__ == '__main__':
    db_connector = get_connection()
    df = load_to_dataframe(db_connector)
    calculo_duracion(df)
        aux = int(o.split(" ")[0])
        if " min" in o:
            min.append(aux)
        if " Seasons" in o:
            season.append(aux)

    print("\nPeliculas:")
    print(f'Valor medio de duracion de las peliculas: {np.average(min):,.2f} minutos')
    print(f'Valor de la desviacion tipica de la duracion de las peliculas: {np.std(min):,.2f}')
    print("\nTVShows:")
    print(f'Valor medio de duracion de las TVSHOWS: {np.average(season):,.2f} temporadas')
    print(f'Valor de la desviacion tipica de la duracion de las TVSHOWS: {np.std(season):,.2f}')
'''


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


if __name__ == '__main__':
    dbc = config.get_connection(2);
    dfm = pd.read_sql("SELECT *  FROM MOVIE", con=dbc)
    dft = pd.read_sql("SELECT *  FROM TV_SHOW", con=dbc)
    print()
    print(len(dfm))
    print()
    print("Número de muestras (valores distintos de missing).")
    print(count(dfm) + count(dft))
    print()
    print("Media de la columna duración para peliculas")
    print("{:.2f}".format(average_movie(dfm)))
    print("Media de la columna duración para tv shows")
    print("{:.2f}".format(average_tv_show(dft)))
    print()
    print("Desviación estándar de la columna duración en peliculas.")
    print("{:.2f}".format(std_movie(dfm)))
    print("Desviación estándar de la columna duración en tv shows.")
    print("{:.2f}".format(std_tv_show(dft)))
    print()
    print("Duración mínima en películas")
    print(minimun(dfm,"duration"))
    print("Duración máxima en películas")
    print(maximun(dfm,"duration"))
    print()
    print("Duración mínima en tv shows")
    print(minimun(dft,"duration"))
    print("Duración máxima en tv shows")
    print(maximun(dft,"duration"))
    print()
    print("Año mínimo de lanzamiento de pelicula")
    print(minimun(dfm,"release_year"))
    print("Año máximo de lanzamiento de pelicula")
    print(maximun(dfm,"release_year"))
    print()
    print("Año mínimo de lanzamiento de tv shows")
    print(minimun(dft,"release_year"))
    print("Año máximo de lanzamiento de tv shows")
    print(maximun(dft,"release_year"))
    print()

    dfml = dfm[dfm['duration'] >= 90]
    dfmc = dfm[dfm['duration'] < 90]
    dftl = dft[dft['duration'] >= 3]
    dftc = dft[dft['duration'] < 3]

    print("Número de observaciones de películas de más de 90'")
    print(count(dfml['duration']))
    print("Número de observaciones de películas de menos de 90'")
    print(count(dfmc['duration']))
    print("Número de observaciones de tv shows de más de 2 temporadas")
    print(count(dftl['duration']))
    print("Número de observaciones de tv shows de 1 o 2 temporadas")
    print(count(dftc['duration']))
    print()

    print("Número de valores ausentes (missing) de películas de más de 90'")
    print(count_null(dfml['duration']))
    print("Número de valores ausentes (missing) de películas de menos de 90'")
    print(count_null(dfmc['duration']))
    print("Número de valores ausentes (missing) de tv shows de más de 2 temporadas")
    print(count_null(dftl['duration']))
    print("Número de valores ausentes (missing) de 1 o 2 temporadas")
    print(count_null(dftc['duration']))
    print()

    print("Mediana de películas de más de 90'")
    print(np.median(dfml['duration']))
    print("Mediana de películas de menos de 90'")
    print(np.median(dfmc['duration']))
    print("Mediana de tv shows de más de 2 temporadas")
    print(np.median(dftl['duration']))
    print("Mediana de 1 o 2 temporadas")
    print(np.median(dftc['duration']))
    print()

    print("Media de películas de más de 90'")
    print("{:.2f}".format(np.average(dfml['duration'])))
    print("Media de películas de menos de 90'")
    print("{:.2f}".format(np.average(dfmc['duration'])))
    print("Media de tv shows de más de 2 temporadas")
    print("{:.2f}".format(np.average(dftl['duration'])))
    print("Media de 1 o 2 temporadas")
    print("{:.2f}".format(np.average(dftc['duration'])))
    print()

    print("Varianza de películas de más de 90'")
    print("{:.2f}".format(np.var(dfml['duration'])))
    print("Varianza de películas de menos de 90'")
    print("{:.2f}".format(np.var(dfmc['duration'])))
    print("Varianza de tv shows de más de 2 temporadas")
    print("{:.2f}".format(np.var(dftl['duration'])))
    print("Varianza de 1 o 2 temporadas")
    print("{:.2f}".format(np.var(dftc['duration'])))
    print()

    print("Duración mínima en películas de más de 90'")
    print(minimun(dfml, "duration"))
    print("Duración máxima en películas de más de 90'")
    print(maximun(dfml, "duration"))
    print()
    print("Duración mínima en películas de menos de 90'")
    print(minimun(dfmc, "duration"))
    print("Duración máxima en películas de menos de 90'")
    print(maximun(dfmc, "duration"))
    print()
    print("Duración mínima en tv shows de más de 2 temporadas")
    print(minimun(dftl, "duration"))
    print("Duración máxima en tv shows de más de 2 temporadas")
    print(maximun(dftl, "duration"))
    print()
    print("Duración mínima en tv shows de 1 o 2 temporadas")
    print(minimun(dftc,"duration"))
    print("Duración máxima en tv shows de 1 o 2 temporadas")
    print(maximun(dftc,"duration"))
    print()

    # iu.create_tables_users(dbc)
    iu.generar_usuario(dbc)
    iu.generar_visionados(dbc)
    df3 = pd.read_sql("SELECT * FROM USER", con=dbc)
    print(df3)
    # db.create_tables()
    # db.import_data(dbc,".\\res\\data.txt")
    # db_connector = get_connection()
    # df = load_to_dataframe(db_connector)
    # calculo_duracion(df)
