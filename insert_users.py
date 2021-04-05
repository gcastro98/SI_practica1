import random as rn
from datetime import datetime, timedelta

import random_username.generate as ran
import main as mn
import pandas as pd
import numpy as np

import mysql.connector

def create_tables_users(dbc):
    cur = dbc.cursor()
    cur.execute("DROP TABLE USER")
    cur.execute("DROP TABLE VIEWING")
    cur.execute("CREATE TABLE USER (" + "\n" +
        "user_id varchar(8) NOT NULL," + "\n" +
        "username varchar(45) NOT NULL," + "\n" +
        "last_sign_in DATETIME DEFAULT NULL," + "\n" +
        "PRIMARY KEY (user_id)" + "\n" +
        ")"
    )
    cur.execute("CREATE TABLE VIEWING (" + "\n" +
                "user_id varchar(8) NOT NULL," + "\n" +
                "show_id varchar(8) NOT NULL," + "\n" +
                "type_show varchar(45) DEFAULT NULL," + "\n" +
                "rating INTEGER DEFAULT NULL," + "\n" +
                "PRIMARY KEY (user_id,show_id)" + "\n" +
                ")"
                )

def generar_usuario(dbc):
    cur = dbc.cursor()
    for i in range(0, 13):
        print(
            "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        )
        # cur.execute(
        #     "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        # )

def generar_visionados(dbc):
    cur = dbc.cursor()
    try:
        fout = open("insert_visionados.sql", "w", encoding="utf-8")
    except IOError:
        fout = open("insert_visionados.sql", "x", encoding="utf-8")
    df3 = pd.read_sql("SELECT * FROM USER", con=dbc)
    dfm = pd.read_sql("SELECT * FROM MOVIE", con=dbc)
    dft = pd.read_sql("SELECT * FROM TV_SHOW", con=dbc)
    for i in df3["user_id"]:
        array = []
        for j in range(0,300):
            if (int((rn.random()*2)) % 2 == 0):
                x = int(rn.random()* len(dfm))
                if (not x in array):
                    array.append(x)
                    fout.write(
                        "INSERT INTO VIEWING (user_id, show_id, type_show, rating) VALUES (\"" + i + "\",\"" + dfm["show_id"].iloc[x] + "\",\"" + dfm["type_show"].iloc[x]+ "\",\"" + str(int(rn.random() * 6)) +"\");\n"
                    )
            else:
                x = int(rn.random() * len(dft))
                if (not x in array):
                    array.append(x)
                    fout.write(
                        "INSERT INTO VIEWING (user_id, show_id, type_show, rating) VALUES (\"" + i + "\",\"" + dft["show_id"].iloc[x] + "\",\""+ dft["type_show"].iloc[x] + "\",\"" + str(int(rn.random() * 6)) +"\");\n"
                    )
