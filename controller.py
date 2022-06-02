
#from os import getloadavg
import json

from mysql.connector import IntegrityError

#from psycopg2 import IntegrityError

import connexion
# def initDB():
#     global

currentUser = ""
isAdmin = False


def verifConnexion(login, password):
    global isAdmin, currentUser
    print(login, password)
    try:

        sql = "SELECT * from user WHERE login ='" + \
            login + "' and password ='" + password + "'"

        connexion.cur.execute(sql)
        row = connexion.cur.fetchone()
        if row[0] == login and row[1] == password:
            currentUser = login
            if row[2] == 1:
                isAdmin = True
                print(isAdmin)
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
    global currentUser
    if currentUser != "":
        sql = "SELECT password from user WHERE user.login = '" + currentUser + "'"
        connexion.cur.execute(sql)
        if(connexion.cur.fetchone()[0] == ancienMDP):
            sql = "UPDATE user SET password = '" + nouvMDP + "' WHERE user.login = '" + \
                connexion.currentUser + "' AND password = '" + ancienMDP + "'"
            connexion.cur.execute(sql)
            connexion.conn.commit()
        else:
            print("mauvais mot de passe")


def quitter():
    global currentUser
    connexion.cur.close()
    connexion.conn.close()

    currentUser = ""

def deconnecter():
    print("deco")



#pip install pandas et openpyxl
import pandas as pd

def importerCommande(fichier):
    global currentUser
    print(currentUser)
    if not fichier.endswith('.xlsx'):
        print("Mauvais format de fichier")
        return None
    
    commande = pd.read_excel(fichier)

    print(commande)

    commandes = {} #dictionnaire : à chaque commande correspond la liste de verre qu'on transformera en json

    for index, row in commande.iterrows():
        idcommande = row['Commandes']
        if idcommande in commandes.keys():
            listeVerre = commandes[idcommande]
            listeVerre.append({"special": int(row['Spécial']), "type": row['Type de verre'], "quantite": row['Quantité']})
            commandes[idcommande] = listeVerre
        
        else:
            listeVerre = [{"special": int(row['Spécial']), "type": row['Type de verre'], "quantite": row['Quantité']}]
            commandes[idcommande] = listeVerre
        
    #print(commandes)

    #enregistrement dans la base de données
    try:
        for idcommande in commandes:
            sql = "INSERT INTO commande values ('" + idcommande + "', '" + currentUser + "', '" + json.dumps(commandes[idcommande]) + "')"
            print(sql)
            connexion.cur.execute(sql)
            connexion.conn.commit()

    except IntegrityError as err:        
        print("Commande deja dans la base de données ou mauvais format de donnée dans le excel : {}".format(err))
        
    
    return commandes

def getInfosCommande(idcommande):

    sql = "SELECT * FROM commande WHERE numero_commande = '" + idcommande + "'"
    connexion.cur.execute(sql)
    
    results = connexion.cur.fetchall()
    if len(results) > 0:
        return results[0][2]
    else:
        return None
