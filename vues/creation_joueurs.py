import json
from vues.player import Joueur

class CreationJoueur:

    def __init__(self):
        
        joueurs=[]

    def creer_joueurs(self):
        joueurs = []
        dic_joueurs = {}

        for i in range (1,9):
            score=0
            print(f"Saisie du joueur {i}\n")
            nom = input (f"Nom  du joueur {i} :\n")
            prenom = input(f"Prénom du joueur {i} : \n")
            try:
                dob=int(input ("Année de naissance :"))
            except ValueError:
                print("Vous devez saisir une année valide")
            sexe=input("Sexe du joueur (H/F), par défaut H :")
            if sexe=="" or sexe!="F":
                sexe="H"
        
            while True:
                try:
                    rating=int(input("Classement ELO (nombre entier >1599:) "))
                    if rating>1599:
                        break
                except ValueError:
                    print("Le classement doit être un entier, positif et au moins égal à 1600")
            
            joueur = Joueur(nom, prenom, dob, sexe, rating, score=0)
            joueurs.append(joueur)
            #joueur_dic = joueur.to_dict(joueur)
            #dic_joueurs.append(joueur_dic)
        #with open ('data.json', 'w') as fichier_joueurs:
        #    json.dump(dic_joueurs, fichier_joueurs)
            #print(joueur)
            
            #print(joueur.nom, joueur.prenom, joueur.dob, joueur.sexe, joueur.rating, joueur.score)
            #joueur = {"Nom": "nom", "Prenom": "prenom", "Date de naissance": "dob", "Sexe": "sex", "Classement ELO": "rating", "Classement tournoi": "score"}
            #joueurs.append(joueur)
            
        #print(dic_joueurs)    



    #classement alphabétique   
    """def tri_alpha(self):    
        joueurs.sort(key=lambda j: j.name, reverse=False)
        print("\nClassement par ordre alphabétique : \n")        
        for i in joueurs:
            print(i.name, i_prenom, i.rating)
    
    #classement par ELO   
    def tri_elo(self):
        joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)"""