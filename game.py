# moteur de jeu kgc game
from random import randint,choice

def nombre_aleatoire(debut,fin):
    nombre_secret=randint(debut,fin)
    essais=5
    tentatives=0
    def reinitialiser():
        nonlocal essais,tentatives,nombre_secret
        essais=5
        tentatives=0
        nombre_secret=randint(debut,fin)
    # BOUCLE
    while True :
        try:
            mon_choix=int(input("devinez le nombre secret:"))
        except ValueError:
            print("ERREUR le choix est un chiffre ou entier pas une lettre.")
            continue

        essais-=1
        tentatives+=1
        if essais <1 and mon_choix != nombre_secret:
            print (f"GAME OVER ESSAIS EPUISE {tentatives} tentatives ")
            recommencer=input("recommencer ? oui/non :").strip().lower()
            if recommencer =='oui':
                reinitialiser()
                continue
            else:

                break
        # CONDITION GRAND PETIT
        if mon_choix > nombre_secret:
            print("INDICE : le nombre secret est petit que ton essais")
            print(f"essais restant :{essais}")
        if mon_choix< nombre_secret:
            print("INDICE : le nombre secret est grand que ton essais")
            print(f"essais restant :{essais}")

        # trouve
        if mon_choix==nombre_secret:
            print(f"BRAVO! vous avez le nombre secret en {tentatives} tentatives")
            try:
                recommencer=input("vous avez gagne . vous voulez encore jouer ? oui/non :").strip().lower()
            except ValueError:
                print("ERREUR . mauvaise saisie ")

            if recommencer=="oui":
                reinitialiser()
                
                continue
            else:
                break



def nom_aleatoire(liste):
    pass