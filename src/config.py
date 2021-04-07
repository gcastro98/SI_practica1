import mysql.connector


def get_connection(n):
    if (n == 1):
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            passwd="Lechugaa10016",
            auth_plugin='mysql_native_password',
            database='table_practica'
        )
        return db_connection
    else:
        db_connection = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            passwd="",
            auth_plugin='mysql_native_password',
            database='db_practica'
        )
        return db_connection