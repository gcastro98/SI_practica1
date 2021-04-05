import random as rn
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
        "last_sign_in DATETIME DEFAULT NOW()," + "\n" +
        "PRIMARY KEY (user_id)" + "\n" +
        ")"
    )
    cur.execute("CREATE TABLE VIEWING (" + "\n" +
                "user_id varchar(8) NOT NULL," + "\n" +
                "show_id varchar(8) NOT NULL," + "\n" +
                "viewing_date DATETIME DEFAULT NOW()," + "\n" +
                "type_show varchar(45) DEFAULT NULL," + "\n" +
                "rating INTEGER DEFAULT NULL," + "\n" +
                "PRIMARY KEY (user_id)" + "\n" +
                ")"
                )

def generar_usuario(dbc):
    cur = dbc.cursor()
    for i in range(0, 20):
        print(
            "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        )
        # cur.execute(
        #     "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        # )

def generar_visionados(dbc):
    cur = dbc.cursor()
    df3 = pd.read_sql("SELECT * FROM USER", con=dbc)
    dfm = pd.read_sql("SELECT * FROM MOVIE", con=dbc)
    dft = pd.read_sql("SELECT * FROM TV_SHOW", con=dbc)
    for i in df3["user_id"]:
        for j in range(0,1):
            if ((rn.random()*2) % 2 == 0):
                x = int(rn.random()* len(dfm))
                print(
                    "INSERT INTO VIEWING (user_id, show_id, viewing_date, type_show, rating) VALUES (\"" + i + "\",\"" + dfm["show_id"].iloc[x] + "\",NOW(),\"" + dfm[x]["type_show"]+ "\",\"" + str(rn.random() * 6) +"\");"
                )
            else:
                x = int(rn.random()* len(dft))
                print(
                    "INSERT INTO VIEWING (user_id, show_id, viewing_date, type_show, rating) VALUES (\"" + i + "\",\"" + dft["show_id"].iloc[x] + "\",NOW(),\"" + dft[x]["type_show"]+ "\",\"" + str(rn.random() * 6) +"\");"
                )
