# JEU DEVINETTE KGC
from auth import creer_compte,connexion
from game import nombre_aleatoire

def creer():
    nom=input("tapez le nom :").strip().lower()
    mot_de_passe=input("tapez le mot de passe :")
    print(creer_compte(nom,mot_de_passe))
    

def conn():
    nom=input("tapez le nom :").strip().lower()
    mot_de_passe=input("tapez le mot de passe :")
    reponse=connexion(nom,mot_de_passe)
    print(reponse)
    if reponse.startswith("SUCCES"):
        print("BIENVENUE DANS KGC GAME")
        print("1.jeu nombre aleatoire")
        print("2.quit")

        # choix
        choix = int(input("tapez votre choix :"))
        if choix ==1:
            debut=int(input("commencer par combien :"))
            fin =int(input("terminer par combien :"))
            nombre_aleatoire(debut, fin)
        elif choix ==2:
            print("AU REVOIR")
            exit()
        else:
            print("CHOIX NON RECONNU")
                   



# BOUCLE PRINCIPALE 
while True:
     print("KGC RANDOM GAME")
     print("1.creer_compte")
     print("2.connexion")
     print("3.quit")
     try:
          choix=int(input("tapez votre choix :"))
     except ValueError:
          print("ERREUR DE SAISIE ")
          continue
     if choix == 1:
          creer()
     elif choix == 2 :
          conn()
     elif choix ==3:
          print("AU REVOIR ")
          
          break
     else:
          print("ERREUR choix non reconnu")


    
    


