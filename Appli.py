def msgBienvenue():
    print("Bonjour et bienvenue dans notre ERP")

def demandePrenom():
    prenom = ""
    print("Veuillez saisir votre prénom")
    input(prenom)
    return prenom

def demandeNom():
    nom = ""
    print("Veuillez saisir votre nom")
    input(nom)
    return nom

def recherchePersonneDB(prenom, nom, dataBase):
    #TO DO comparaison avec la DB pour identification
    #return user
    print("coucou")

def demandeAction():

    action = ""
    print("Veuillez choisir l'action à effectuer")
    print("1 pour Action 1")
    print("2 pour Action 2")
    print("3 pour Action 3")
    print("4 pour Action 4")
    print("5 pour Action 5")
    action = input()
    return action

def lancerAction(numeroAction):
    if numeroAction == "1":
        action1()
    if numeroAction == "2":
        action2()
    if numeroAction == "3":
        action3()
    if numeroAction == "4":
        action4()
    if numeroAction == "5":
        action5()

def action1():
    print("WIP Action 1")

def action2():
    print("WIP Action 2")

def action3():
    print("WIP Action 3")

def action4():
    print("WIP Action 4")

def action5():
    print("WIP Action 5")
    

def loop():
    msgBienvenue()
    prenom = demandePrenom()
    nom = demandeNom()
    currentUser = "toto"
    #currentUser = recherchePersonneDB(prenom, nom, dataBase)
    while(True):
        choix = demandeAction()
        lancerAction(choix)

    

    


loop()