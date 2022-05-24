
import connexion
# def initDB():
#     global

currentUser = ""


def verifConnexion(login, password):
    print(login, password)
    try:

        sql = "SELECT * from user WHERE login ='" + \
            login + "' and password ='" + password + "'"

        connexion.cur.execute(sql)
        row = connexion.cur.fetchone()
        if row[0] == login and row[1] == password:
            currentUser = login
            return True
    except:
        print("Mot de passe ou login invalide")
        return False


def ajouterUtilisateur(login, password, isAdmin):
    sql = "SELECT * from user WHERE login ='" + login + "'"
    connexion.cur.execute(sql)
    myresult = connexion.cur.fetchall()

    if(len(myresult) > 0):
        print("utilisateur existe deja")
    else:
        sql = "INSERT INTO user values ('" + login + \
            "','" + password + "'," + str(isAdmin) + ")"
        connexion.cur.execute(sql)
        connexion.conn.commit()


def modifMDP(ancienMDP, nouvMDP):
    if currentUser != "":
        sql = "SELECT password from user WHERE User.login = '" + currentUser + "'"
        connexion.cur.execute(sql)
        if(connexion.cur.fetchone()[0] == ancienMDP):
            sql = "UPDATE user SET password = '" + nouvMDP + "' WHERE User.login = '" + \
                connexion.currentUser + "' AND password = '" + ancienMDP + "'"
            connexion.cur.execute(sql)
            connexion.conn.commit()
        else:
            print("mauvais mot de passe")


def deconnexion():
    connexion.cur.close()
    connexion.conn.close()
    currentUser = ""
