
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
            else:
                isAdmin = False
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

    commandes = {} #dictionnaire : ?? chaque commande correspond la liste de verre qu'on transformera en json

    #ajouter les ids pour la r??f??rence
    #dossier client pour les verres sp??ciaux
    for index, row in commande.iterrows():
        idcommande = row['Commandes']
        if idcommande in commandes.keys():
            listeVerre = commandes[idcommande]
            listeVerre.append({"special": int(row['Sp??cial']), "type": row['Code article'], "quantite": row['Quantit??'], "client": str(row['Dossier Client'])})
            commandes[idcommande] = listeVerre
        
        else:
            listeVerre = [{"special": int(row['Sp??cial']), "type": row['Code article'], "quantite": row['Quantit??'], "client": str(row['Dossier Client'])}]
            commandes[idcommande] = listeVerre
        
    print(commandes)

    #enregistrement dans la base de donn??es
    try:
        for idcommande in commandes:
            sql = "INSERT INTO commande values ('" + idcommande + "', '" + currentUser + "', '" + json.dumps(commandes[idcommande]) + "')"
            print(sql)
            connexion.cur.execute(sql)
            connexion.conn.commit()

    except IntegrityError as err:        
        print("Commande deja dans la base de donn??es ou mauvais format de donn??e dans le excel : {}".format(err))
        
    
    return commandes

def getInfosCommande(idcommande):

    sql = "SELECT * FROM commande WHERE numero_commande = '" + idcommande + "'"
    connexion.cur.execute(sql)
    
    results = connexion.cur.fetchall()
    if len(results) > 0:
        verres = results[0][2]
        if verres == None:
            return None
        
        verres = str(verres)[2:-1]
        verres = json.loads(verres)
        return verres
    else:
        return None

def getInfosTypeVerre(code_article):
    sql = "SELECT * FROM type_de_verre WHERE code_article = '" + code_article + "'"
    connexion.cur.execute(sql)
    
    results = connexion.cur.fetchall()
    if len(results) > 0:
        return results[0]
        # infoType = results[0]
        
        # print (infoType[0])

    else:
        return None