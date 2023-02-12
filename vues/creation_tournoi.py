from modeles.tournoi import Tournoi


class CreationTournoiView:

    def __init__(self):
        pass

    def creer_tournoi(self):
        libelle_tournoi = {'1': 'Rapide', '2': 'Blitz', '3': 'Bullet'}
        nom_tournoi = input("Nom du tournoi :\n")
        lieu_tournoi = input("Lieu du tournoi :\n")
        date_debut_tournoi = input("Date de début du tournoi : ")
        date_fin_tournoi = input("Date de fin du tournoi : (Appuyer sur Entrée si le tournoi ne dure qu'un jouer)")
        if not date_fin_tournoi:
            date_fin_tournoi = date_debut_tournoi
        while True:
            try:
                type_tournoi = int(input("Type de tournoi : Rapide(1), Blitz(2), Bullet(3) (Rapide par défaut) : \n"))
                if type_tournoi > 0 and type_tournoi < 4:
                    break
            except ValueError:
                print("La valeur doit être un nombre entier compris entre 1 et 3")
        description = input("Description (Appuyer sur Entrée pour ne pas saisir de description) \n")
        nombre_tours = 4
        libelle_type_tournoi = libelle_tournoi.get(str(type_tournoi))
        print(f"Type de tournoi : {libelle_type_tournoi}")
        #nouveau_tournoi = Tournoi(self.nom_tournoi, self.lieu_tournoi,
        #self.date_debut_tournoi, self.date_fin_tournoi, self.type_tournoi, self.description, self.nombre_tours)

        """def afficher_tournoi(self):"""
        TOURNAMENT_TYPE = {1: "Rapide", 2: "Blitz", 3: "Bullet"}
        print()
        print(f"Récapitulatif du nouveau tournoi {nom_tournoi} : ")
        print()
        print(f"Nom du tournoi : {nom_tournoi}")
        print(f"Lieu : {lieu_tournoi}")
        print(f"Date de début : {date_debut_tournoi}")
        print(f"Date de fin : {date_fin_tournoi}")
        type_tournoi = int(type_tournoi)
        print(f"Type de tournoi : {TOURNAMENT_TYPE[type_tournoi]}")  # ({self.type_tournoi}) ")
        print(f"Description du directeur du tournoi : {description}")

        return nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, type_tournoi, description, nombre_tours
