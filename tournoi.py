from views.player import Joueur
from views.tournoi import Tournoi
import re

"""class Tournoi:
    def __init__(self, name_tournoi, lieu_tournoi, date_tournoi, joueurs, type="Blitz", nombre_tours=4, controle_temps="", description=""):
        self.name_tournoi=name_tournoi
        self.lieu_tournoi=lieu_tournoi
        self.date_tournoi=date_tournoi
        self.nombre_tours=nombre_tours
        self.controle_temps=controle_temps
        self.description=description
        self.joueurs=joueurs

    def afficher_tournoi(self):
            print(self.name_tournoi)
            print(self.lieu_tournoi)
            print(self.joueurs)
            """
"""class Joueur:
    def __init__(self, nom, prenom, date_naissance, sexe, rating, score=0):
        self.nom=nom
        self.prenom=prenom
        self.date_naissance = date_naissance
        self.sexe=sexe
        self.rating=rating
        self.score=score

    def __str__(self):
        return self.nom, self.prenom, self.rating
        
    def __repr__(self):
        return str(self)

    
    def afficher_joueur(self):
        print(self.nom + "\n" +self.prenom+ "\n"+self.sexe+"\n"+self.rating)"""

class Tour:
    tours=[]
    def __init__(self,round_number,matchs):
        self.round_number=round_number
        self.matchs=matchs

    def creation_tour():
        print(f"Tour numéro {self.round_number}")

class Match:
    matchs=[]
    def __init__(self):
        #self.joueur1=joueur1
        #self.joueur2=joueur2
        pass

    """for i in range(0,4):
        match[i]=([joueurs[i], score], [joueur[i+4], score])
        Un match unique doit être stocké sous la forme d'un tuple
        contenant deux listes, chacune contenant deux éléments : 
        une référence à une instance de joueur et un score.
        Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour."""

def main():

    # MENU
    #1 Nouveau tournoi
    #2 Saisie des joueurs -> MODELE
    #3 Saisie tour (appareillement selon indice)
    #4 Saisie résultats d'un tour
    #5 Afficher classement
    #6 Quitter


    print("1. Nouveau tournoi et saisie des joueurs")
    print("2. Affichage des matchs")
    print("3. Saisie des résultats")
    print("4. Match du tour suivant")
    print("5. Afficher classement")
    print("6. Quitter")


    """NOUVEAU TOURNOI ET SAISIE DES JOUEURS (6 joueurs pour test)

    Création d'un nouveau tournoi et de la liste des joueurs, classés par ELO, donc pour le 1er tour"""
    
    joueurs=[]

    for i in range (0,6):

        print(f"Entrer le joueur {i}\n")
        
        nom=input (f"Nom  du joueur {i}\n")
        
        prenom=input(f"Prénom du joueur {i}: \n")
        
        date_naissance=input ("Date de naissance (format JJ/MM/AAA :)") #vérif dans la VUE
        #date=re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(./-)([1-9] |1[0-2])(./-|)19[0-9][0-9]$",date_naissance)
        #print(date)

        sexe=input("Sexe du joueur (H/F) :")

        while True:
            try:
                rating=int(input("Classement ELO (nombre entier :) "))
                if rating>1599:
                    break
            except ValueError:
                print("Le classement doit être un chiffre entier, positif et au moins égal à 1600")
        
        joueur=Joueur(nom, prenom, date_naissance, sexe, rating, score=0)
        joueurs.append(joueur)
         
    for i in joueurs:
        #print(f'{i.nom} {i.prenom} {i.date_naissance} {i.sexe}, {i.rating}')
        print(f'{i.nom} {i.rating}')
    
    """Descending sorting players by rank Contrôleur ou modèle ou View ?

    2 loops go though the players' rankings and intervert players where needed"""
    
    for j in range(0,5):
        #table_sorted=true
        for i in range(0,5):
            joueur=joueurs[i].rating
            """# possibilité d'optimiser le tri en commançant dernier élément du tableau
            sans intérêt pour un petit tableau"""
            #print(f'Joueur {joueurs[i].nom} Classement {joueurs[i].rating} index {i}')
            if joueurs[i+1].rating>joueur:
                joueurs[i], joueurs[i+1]=joueurs[i+1], joueurs[i]
                
    print("\nClassement après tri : \n")        
    for i in joueurs:
        print(i.nom, i.prenom, i.rating)

    print(joueurs)

    """#Création d'un tournoi

    nom_tournoi=input("Nom du tournoi : ")
    lieu_tournoi=input("Lieu du tournoi : ")
    date_tournoi=input("Date du tournoi : ")
    print ("Type de tournoi :")
    print("1. Rapide")
    print("2. Blitz")
    print("3. Bullet")
    type_tournoi=int(input
    #self_tournees= ?

    
    tournoi=Tournoi(nom_tournoi,lieu_tournoi,date_tournoi,joueurs)
    tournoi.afficher_tournoi()"""

    """Creating 1 round (premier match), list of matches and add match to a list of matches
    Add to the index of each of the 3 top players to determine opponent for 1st round"""

    matchs=[]
    
    for i in range(0,3):
        print(f"Match  {i} : ")
        print(joueurs[i].nom +" vs "+ joueurs[i+3].nom)
        match=([joueurs[i].nom, joueurs[i].score], [joueurs[i+3].nom, joueurs[i+3], joueurs[i+3].score])
        matchs.append(match)
        tour.append(match)
        print(match)
        #print(matchs)

    premier_tour=Round("Premier tour", 1, matchs)
    print(premier_tourtour)


    #Nouveau tournoi    
    nouveau_tournoi=[]
    nom_tournoi=input("Nom du tournoi :\n")
    lieu_tournoi=input("Lieu du tournoi :\n")
    date_tournoi=input("Date du tournoi : ")
    nombre_tours=int(input("Nombre_tours (4 par défaut, taper sur Entrée pour 4) :\n"))
    type_tournoi=input("Type de tournoi : Rapide, Blitz, Bullet (Rapide par défaut) : \n")
    description=input("Description (facultatif, taper sur Entrée pour ne pas mettre de description) \n")
    nouveau_tournoi=Tournoi(nom_tournoi,lieu_tournoi,date_tournoi,joueurs,type_tournoi,description)
    nouveau_tournoi.afficher_tournoi()

    #Nouveau tour


if __name__ == "__main__":
    main()