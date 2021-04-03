import mysql.connector
import numpy as np
import pandas as pd
import db_start as db
import config


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

def count(dbc):
    dfm = pd.read_sql("SELECT *  FROM MOVIE", con=dbc)
    dft = pd.read_sql("SELECT *  FROM TV_SHOW", con=dbc)
    print(dfm)
    return dfm.notnull().sum() + dft.notnull().sum()

if __name__ == '__main__':
    dbc = config.get_connection(2);
    # print(count(dbc))
    # db.create_tables()
    db.import_data(dbc,".\\res\\data.txt")
    # db_connector = get_connection()
    # df = load_to_dataframe(db_connector)
    # calculo_duracion(df)
