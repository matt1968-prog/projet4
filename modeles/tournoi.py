import json


class Tournoi:

    def __init__(self, nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, description, type_tournoi, nombre_tours=4):
        self.nom_tournoi = nom_tournoi
        self.lieu_tournoi = lieu_tournoi
        self.date_debut_tournoi = date_debut_tournoi
        self.date_fin_tournoi = date_fin_tournoi
        self.nombre_tours = nombre_tours
        self.type_tournoi = type_tournoi
        self.description = description
        self.nombre_tour = nombre_tours

    def to_dict(self):
        return {'Nom du tournoi': self.nom_tournoi, 'Lieu du Tournoi': self.lieu_tournoi, 'Date de début': self.date_debut_tournoi, 'Date de fin': self.date_fin_tournoi, 'Description': self.description, 'Type de tournoi': self.type_tournoi, 'Nombre de tours': '4'}


class TournoiDAO:
    def save(self, tournoi):
        with open('data_tournoi.json', 'w') as file:
            data = json.dumps([j.to_dict() for j in tournoi], indent=4)
            file.write(data)

    def load(self):
        with open('data_tournoi.json', 'r') as file:
            data = json.loads(file.read())
            nouveau_tournoi = []
            for d in data:
                j = Tournoi(**d)
                nouveau_tournoi.append(j)
            print(nouveau_tournoi)
            return nouveau_tournoi

    """with open ('data_tournoi.json', 'w') as file:
        data_tournoi = json.dumps([j.to_dict() for j in tournoi], indent = 4)
        file.write(data_tournoi)
        #print(data_tournoi)

    with open('data_tournoi.json', 'r') as fichier_tournoi:
        data_lues = json.load(fichier_tournoi)
        print(data_lues)"""
