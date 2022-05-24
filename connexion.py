import identifiants
import mysql.connector

conn = mysql.connector.connect(host=identifiants.host, user=identifiants.user,
                               password=identifiants.password,  database=identifiants.dbname)
cur = conn.cursor()
