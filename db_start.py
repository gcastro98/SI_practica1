import mysql;


def get_connection():
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        passwd="",
        auth_plugin='mysql_native_password',
        database='db_practica'
    )
    return db_connection


def add_movie(f, str):
    str = str.replace("\"", "\\\"")
    str = str.replace("\n", "")
    a = str.split(';')
    x = "INSERT INTO MOVIE (show_id, type_show, title, director, casting, country, date_added, release_year, rating, duration, listed_in, description) " + "VALUES (\"" + \
        a[0] + "\",\"" + a[1] + "\",\"" + a[2] + "\",\"" + a[3] + "\",\"" + a[4] + "\",\"" + a[
            5] + "\"," + "STR_TO_DATE(\"" + a[6] + "\", \"%M %d, %Y\")" + ",\"" + a[7] + "\",\"" + a[8] + "\",\"" + a[
            9] + "\",\"" + a[10] + "\",\"" + a[11] + "\");\n"
    x = x.replace(",\"\",", ",NULL,")
    x = x.replace(" min", "");
    x = x.replace(" Seasons", "");
    x = x.replace(" Season", "");
    x = x.replace("STR_TO_DATE(\"\", \"%M %d, %Y\")", "NULL");
    x = x.replace(",\"\",", ",NULL,")
    f.write(x)


def add_tvshow(f, str):
    str = str.replace("\"", "\\\"")
    str = str.replace("\n", "")
    a = str.split(';')
    x = "INSERT INTO TV_SHOW (show_id, type_show, title, director, casting, country, date_added, release_year, rating, duration, listed_in, description) " + "VALUES (\"" + \
        a[0] + "\",\"" + a[1] + "\",\"" + a[2] + "\",\"" + a[3] + "\",\"" + a[4] + "\",\"" + a[
            5] + "\"," + "STR_TO_DATE(\"" + a[
            6] + "\", \"%M %d, %Y\")" + ",\"" + a[7] + "\",\"" + a[8] + "\",\"" + a[9] + "\",\"" + a[10] + "\",\"" + a[
            11] + "\");\n"
    x = x.replace(",\"\",", ",NULL,")
    x = x.replace(" Seasons", "");
    x = x.replace(" Season", "");
    x = x.replace("STR_TO_DATE(\"\", \"%M %d, %Y\")", "NULL");
    x = x.replace(",\"\",", ",NULL,")
    f.write(x)
    # STR_TO_DATE("August 10 2017", "%M %d %Y")
    # cur.execute(
    #     "INSERT INTO TV_SHOW (show_id, title, director, casting, country, date_added, release_year, rating, duration, listed_in, description) " +
    #     "VALUES (\"" + a[0] + "\",\"" + a[2] + "\",\"" + a[3] + "\",\"" + a[4] + "\",\"" + a[5] + "\",\"" + a[
    #         6] + "\",\"" + a[7] + "\",\"" + a[8] + "\",\"" + a[9] + "\",\"" + a[10] + "\",\"" + a[11] + "\");"
    # )


def create_tables(dbc):
    cur = dbc.cursor()
    cur.execute(
        "DROP TABLE MOVIE"
    )
    cur.execute(
        "DROP TABLE TV_SHOW"
    )
    cur.execute(
        "CREATE TABLE MOVIE (" + "\n" +
        "show_id varchar(8) NOT NULL," + "\n" +
        "type_show varchar(45) DEFAULT NULL," + "\n" +
        "title varchar(500) DEFAULT NULL," + "\n" +
        "director varchar(500) DEFAULT NULL," + "\n" +
        "casting varchar(1500) DEFAULT NULL," + "\n" +
        "country varchar(300) DEFAULT NULL," + "\n" +
        "date_added date DEFAULT NULL," + "\n" +
        "release_year INTEGER DEFAULT NULL," + "\n" +
        "rating varchar(45) DEFAULT NULL," + "\n" +
        "duration INTEGER DEFAULT NULL," + "\n" +
        "listed_in varchar(100) DEFAULT NULL," + "\n" +
        "description varchar(900) DEFAULT NULL," + "\n" +
        "PRIMARY KEY (show_id)" + "\n" +
        ")"
    )
    cur.execute(
        "CREATE TABLE TV_SHOW (" + "\n" +
        "show_id varchar(8) NOT NULL," + "\n" +
        "type_show varchar(45) DEFAULT NULL," + "\n" +
        "title varchar(500) DEFAULT NULL," + "\n" +
        "director varchar(500) DEFAULT NULL," + "\n" +
        "casting varchar(1500) DEFAULT NULL," + "\n" +
        "country varchar(300) DEFAULT NULL," + "\n" +
        "date_added date DEFAULT NULL," + "\n" +
        "release_year INTEGER DEFAULT NULL," + "\n" +
        "rating varchar(45) DEFAULT NULL," + "\n" +
        "duration INTEGER DEFAULT NULL," + "\n" +
        "listed_in varchar(100) DEFAULT NULL," + "\n" +
        "description varchar(900) DEFAULT NULL," + "\n" +
        "PRIMARY KEY (show_id)" + "\n" +
        ")"
    )


def import_data(dbc, path):
    create_tables(dbc)
    try:
        fout = open("insert.sql", "w", encoding="utf-8")
        # Do something with the file
    except IOError:
        fout = open("insert.sql", "x", encoding="utf-8")
    f = open(path, "r", encoding="utf-8")
    for x in f:
        if x.__contains__(";Movie;"):
            add_movie(fout, x)
        else:
            add_tvshow(fout, x)
