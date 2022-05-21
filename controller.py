import main
import identifiants
import mysql.connector


conn = mysql.connector.connect(host=identifiants.host, user=identifiants.user, password=identifiants.password,  database=identifiants.dbname)
cur = conn.cursor()
# def initDB():
#     global
    
currentUser = ""

def verifConnexion(login, password):
    print(login, password)

    sql = "SELECT * from User WHERE login ='" + login  + "' and password ='" + password + "'"

    cur.execute(sql)
    raw = cur.fetchone()
    if raw[0] == login and raw[1] == password:
        currentUser = login
        return True
  

def ajouterUtilisateur(login, password, isAdmin):
    sql = "SELECT * from User WHERE login ='" + login + "'"
    cur.execute(sql)
    myresult = cur.fetchall()

    if(len(myresult) > 0):
        print("utilisateur existe deja")
    else:
        sql = "INSERT INTO User values ('" + login + "','" + password + "'," + str(isAdmin) + ")"
        cur.execute(sql)
        conn.commit()

def modifMDP(ancienMDP, nouvMDP):
    if currentUser != "":
        sql = "SELECT password from User WHERE User.login = '" + currentUser + "'"
        cur.execute(sql)
        if(cur.fetchone()[0] == ancienMDP):
            sql = "UPDATE User SET password = '" + nouvMDP + "' WHERE User.login = '" + currentUser + "' AND password = '" + ancienMDP + "'"
            cur.execute(sql)
            conn.commit()
        else:
            print("mauvais mot de passe")

