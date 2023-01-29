class Tournoi:

    def __init__(self):
        #self, nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, description, type_tournoi, nombre_tours)
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_tournoi = date_debut_tournoi
        self.date_fin_tournoi=date_fin_tournoi
        self.type_tournoi = type_tournoi
        self.description = description
        #self.joueurs = joueurs
        self.nombre_tours = nombre_tours

    def afficher_tournoi(self):
        print(self.nom_tournoi)
        print(self.lieu_tournoi)
        print(self.date_debut_tournoi)
        print(self.date_fin_tournoi)
        print(self.joueurs)
        print(self.nombre_tours)
        print(self.type_tournoi)
        print(self.description)
