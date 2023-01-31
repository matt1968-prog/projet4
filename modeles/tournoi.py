class Tournoi:

    def __init__(self, nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, description, type_tournoi, nombre_tours =4 ):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_debut_tournoi = date_debut_tournoi    
        self.date_fin_tournoi = date_fin_tournoi
        self.nombre_tours = nombre_tours
        self.type_tournoi = type_tournoi
        self.description = description

    def to_dict(self):
        return {'Nom du tournoi': self.nom_tournoi, 'Lieu du Tournoi': self.lieu_tournoi, 'Date de début': self.date_debut_tournoi, 'Date de fin': self.date_fin_tournoi, 'Description': self.description, 'Type de tournoi': self.type_tournoi}