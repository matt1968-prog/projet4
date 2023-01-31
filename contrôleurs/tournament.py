from vues.creation_tournoi import CreationTournoiView
from modeles.tournoi import Tournoi
import json

class TournoiControleur:

    def create(self):
        vue = CreationTournoiView()
        table_tournoi = []
        #nom, prenom, dob, sexe, rating  = vue.creer_joueur() # modifier
        tournoi = Tournoi(self.nom_tournoi, self.lieu_tournoi, self.date_debut_tournoi, self.date_fin_tournoi, self.type_tournoi: int, self.description: str, self.nombre_tours)
        table_tournoi.append(tournoi)
        
        with open ('table_tournoi.json', 'w') as file_tournoi:
            data = json.dumps([j.to_dict() for j in table_tournoi], indent =4)
            file_tournoi.write(table_tournoi)