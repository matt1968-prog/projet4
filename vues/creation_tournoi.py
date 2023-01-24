from modeles.tournoi import Tournoi
class NouveauTournoi:

    def __init__(self):
        self.nom_tournoi = input("Nom du tournoi :\n")
        self.lieu_tournoi = input("Lieu du tournoi :\n")
        self.date_tournoi = input("Date du tournoi : ")
        self.nombre_tours = 4
        self.type_tournoi = int(input("Type de tournoi : Rapide(1), Blitz(2), Bullet(3) (Rapide par défaut) : \n"))
        self.description = input("Description (facultatif, taper sur Entrée pour ne pas mettre de description) \n")
        nouveau_tournoi = Tournoi(self.nom_tournoi, self.lieu_tournoi, self.date_tournoi, self.type_tournoi, self.description, self.nombre_tours)
        
    def afficher_tournoi(self):
        print(f"Nom du tournoi : {self.nom_tournoi}")
        print(f"Lieu : {self.lieu_tournoi}")
        print(f"Date : {self.date_tournoi}")
        #print(self.joueurs)
        print(self.nombre_tours)
        print(f"Type de tournoi : {self.type_tournoi}")
        print(f"Description du directeur du tournoi : {self.description}")
    