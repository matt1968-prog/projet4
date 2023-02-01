from vues.creation_tournoi import CreationTournoiView
from modeles.tournoi import Tournoi
import json


class TournoiControleur:
    
    def create(self):
        vue = CreationTournoiView()
        data_tournoi = []
        #ligne qui suit est un ajout
        nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, type_tournoi, description, nombre_tours=vue.creer_tournoi()
        tournoi = Tournoi(nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, type_tournoi, description, nombre_tours)
        data_tournoi.append(tournoi)
        
        with open ('data_tournoi.json', 'w') as file:
            data_tournoi = json.dumps([j.to_dict() for j in data_tournoi], indent = 4)
            file.write(data_tournoi)