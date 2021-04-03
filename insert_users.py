from random import random as rn
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
    for i in range(0, 40):
        print(
            "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        )
        s = cur.execute(
            "INSERT INTO USER (user_id, username) VALUES (\"" + "u" + str(i) + "\",\"" + ran.generate_username(1)[0] +"\");"
        )
        print(s)

def generar_visionados(dbc):
    cur = dbc.cursor()
    df3 = pd.read_sql("SELECT * FROM USER", con=dbc)
    for i in df3["user_id"]:
        s = cur.execute(
            "INSERT INTO VIEWING (user_id, show_id, viewing_date, type_show, rating) VALUES (\"" + i + "\",\"s" +str((rn.random()*7787)) + "\",NOW(),\"" + +"\");"
        )
        print(s)