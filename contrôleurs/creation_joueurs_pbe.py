import json
from modeles.player import Joueur

class CreationJoueur:

    def __init__(self):
        pass

    def creer_joueurs(self):
        global joueurs
        joueurs = []
         
        for i in range (1,9):
            score=0
            print(f"Saisie du joueur {i}\n")
            nom = input (f"Nom  du joueur {i} :\n")
            prenom = input(f"Prénom du joueur {i} : \n")
            dob=input ("Date de naissance :") #vérif dans la VUE
            sex=input("Sexe du joueur (H/F), par défaut H :")

            while True:
                try:
                    rating=int(input("Classement ELO (nombre entier >1599:) "))
                    if rating>1599:
                        break
                except ValueError:
                    print("Le classement doit être un entier, positif et au moins égal à 1600")
        
            joueur = Joueur(nom, prenom, dob, sex, rating, score)
            joueurs.append(joueur)   
        print(joueurs)
            #joueur = {"Nom": "nom", "Prenom": "prenom", "Date de naissance": "dob", "Sexe": "sex", "Classement ELO": "rating", "Classement tournoi": "score"}
            #joueurs.append(joueur)
            
        #json.dump(joueurs, fjoueurs)
          #  print(fj)    



    #classement alphabétique   
    def tri_alpha(self, joueurs):    
        joueurs.sort(key=lambda j: j.name, reverse=False)
        print("\nClassement par ordre alphabétique : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)
    
  #classement par ELO   
    def tri_elo(self, joueurs):
        joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)