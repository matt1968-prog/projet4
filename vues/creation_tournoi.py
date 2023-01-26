from modeles.tournoi import Tournoi

class NouveauTournoi:

    def __init__(self):
        self.nom_tournoi = input("Nom du tournoi :\n")
        self.lieu_tournoi = input("Lieu du tournoi :\n")
        self.date_tournoi = input("Date du tournoi : ")
        self.nombre_tours = 4
        while True:
            try:
                self.type_tournoi = int(input("Type de tournoi : Rapide(1), Blitz(2), Bullet(3) (Rapide par défaut) : \n"))
                if self.type_tournoi >0 and self.type_tournoi <4:
                    break
            except ValueError:
                print("La valeur doit être comprise entre 1 et 3")

        self.description = input("Description (facultatif, taper sur Entrée pour ne pas mettre de description) \n")
        nouveau_tournoi = Tournoi(self.nom_tournoi, self.lieu_tournoi, self.date_tournoi, self.type_tournoi, self.description, self.nombre_tours)
        
    def afficher_tournoi(self):
        TOURNAMENT_TYPE ={1:"Rapide", 2:"Blitz", 3:"Bullet"}
        print()
        print(f"Récapitulatif du nouveau tournoi {self.nom_tournoi} : ")
        print()
        print(f"Nom du tournoi : {self.nom_tournoi}")
        print(f"Lieu : {self.lieu_tournoi}")
        print(f"Date : {self.date_tournoi}")
        #print(self.joueurs)
        type_tournoi = int(self.type_tournoi)
        print(f"Type de tournoi : {TOURNAMENT_TYPE[type_tournoi]}")# ({self.type_tournoi}) ")
        #type_tournoi = int(self.type_tournoi)
        #print(f"type_tournoi : {type_tournoi}")
        #print(TOURNAMENT_TYPE)
        #print (TOURNAMENT_TYPE[type_tournoi])
        #print(type_tournoi)
        print(f"Description du directeur du tournoi : {self.description}")
    