import json
from modeles.player import Joueur
from vues.creation_tournoi import CreationTournoiView



class CreationJoueurView:
    def __init__(self):        
        self.score = 0

    def creer_joueur(self):
        score = 0
        print("Saisie du joueur \n")
        nom = input ("Nom  du joueur :\n")
        prenom = input("Prénom du joueur : \n")
        try:
            dob=int(input ("Année de naissance :"))
        except ValueError:
            print("Vous devez saisir une année valide")
        sexe=input("Sexe du joueur (H/F), par défaut H :")
        if sexe == "" or sexe.upper() != "F":
            sexe = "H"
    
        while True:
            try:
                rating = int(input("Classement ELO (nombre entier >1599:) "))
                if rating > 1599:
                    break
            except ValueError:
                print("Le classement doit être un entier, positif et au moins égal à 1600")
        
        return nom, prenom, dob, sexe, rating
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