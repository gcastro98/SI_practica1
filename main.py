import mysql.connector
import numpy as np
import pandas as pd


def get_connection():
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        passwd="",
        auth_plugin='mysql_native_password',
        database='table_practica'
    )
    return db_connection


def load_to_dataframeGeneral(db_conn):
    df = pd.read_sql("SELECT * FROM table_practica2 WHERE typeShow =\"TV Show\"", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return df


def load_to_dataframeSeries(db_conn):
    dfSeries = pd.read_sql("SELECT * FROM table_practica2 WHERE typeShow =\"TV Show\"", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return dfSeries


def load_to_dataframePeliculas(db_conn):
    dfPeliculas = pd.read_sql("SELECT * FROM table_practica2 WHERE typeShow =\"Movie\"", con=db_conn)
    pd.set_option('display.max_columns', None)
    desired_width = 320
    pd.set_option('display.width', desired_width)
    return dfPeliculas


connection = get_connection()
dfShows = load_to_dataframeSeries(connection)
dfMovies = load_to_dataframePeliculas(connection)
dfGeneral = load_to_dataframeGeneral(connection)

print(dfShows)
print(dfMovies)


def numeroMuestras(dfGeneral):
    return pd.notna(dfGeneral)


withoutMissing = numeroMuestras(dfGeneral)

print(withoutMissing)

'''def calculo_duracion(dfGeneral):
    duracion = df.get("duration")
    min, season = []
    for o in duracion:def calculo_duracion(df):
    duracion = df.get("duration")
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


if __name__ == '__main__':
    db_connector = get_connection()
    df = load_to_dataframe(db_connector)
    calculo_duracion(df)'''
