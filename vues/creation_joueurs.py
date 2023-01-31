import json
from modeles.player import Joueur
from vues.creation_tournoi import CreationTournoiView
#from vues.liste_joueurs import affichage_liste


class CreationJoueurView:
    def __init__(self):       
        self.score = 0

    def creer_joueur(self):
        score = 0
        print("Saisie du joueur \n")
        nom = input ("Nom du joueur :\n")
        prenom = input("Prénom du joueur : \n")
        try:
            dob=int(input ("Année de naissance :"))
        except ValueError:
            print("Vous devez saisir une année valide")
        sexe = input("Sexe du joueur (H/F), par défaut H :")
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

        #affichage des joueurs ligne 36 à 41, peuvent être effacée si non fonctionnelles (ajout en cours de test)
        print("Liste alphabétique des joueurs\n")
        liste=affichage_liste(joueurs)
        joueurs.sort(key=lambda j: j.nom, reverse=False)      
        print(joueurs)
        for i in joueurs:
            print("Nom : {i.nom} Prénom {i.prenom)}")

    #liste alphabétique des joueurs
    def afficher_liste_joueurs(self):
        #def __init__(self):
        #self.joueurs = joueurs  
            joueurs.sort(key=lambda j: j.nom, reverse=False)
            print("\nClassement par ordre alphabétique : \n")        
            for i in joueurs:
                print(i.nom, i.prenom, i.rating)
    
    #classement des joueurs par ELO   
    def tri_elo(self):
        joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)
    
    #initialisation du tableau des matchs disputés. O si match non joué, 1 si match joué (ou i=j)
    """"def init_matchs_joues(self):
        matchs_joues=[[][]]
    
        for i in range (0,6):
            for j in range(0,6):
                print(i)
                print(j)
                if i==j:
                    matchs_joues.append(1)
                else:
                matchs_joues.append(0)  """

    #définition des matchs du 1er tour
    def match_round1(self):
        def __init__(self, joueur1, joueur2):
            self.joueur1=joueur1
            self.joueur2=joueur2   
        
    #affichage des matchs du 1er tour    
    def display_round1():
        for i in range(0,3):
            print(f"Match  {i} : ")
            print(joueurs[i].nom +" vs "+ joueurs[i+3].nom)
            match=([joueurs[i].nom, joueurs[i].score], [joueurs[i+3].nom, joueurs[i+3], joueurs[i+3].score])

    #saisie des résultats du 1er tour
    def input_results(self):
        for i in range(0,3):
            z=i
            print(joueurs[i].name +" vs "+ joueurs[i+3].name) 
            resultat=int(input("Résultat : "))
            if resultat==1:
                joueurs[i].score+=1            
            elif resultat==2:
                 joueurs[i+3].score+=1
            elif resultat==0:
                joueurs[i].score+=0.5
                joueurs[i+3].score+=0.5
            else:
                print("Donnée non valide")    
        print(str(joueurs[i].score) +" " +str(joueurs[i+3].score))# -> vue pour l'affichage, controler pour modif des scores
        matchs_joues[i][z+3]=1