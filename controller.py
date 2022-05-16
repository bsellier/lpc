import main

def verifConnexion(login, password):
    print(login, password)
    #verif sql
    if login == 'admin' and password == '123':
        #main.changeDisplay('entree', rootStack)
        print("connexion...")
        return True