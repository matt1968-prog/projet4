from vues.creation_tournoi import CreationTournoiView
from modeles.tournoi import Tournoi
import json


class TournoiControleur:

    def create(self):
        vue = CreationTournoiView()
        data_tournoi = []
        nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, type_tournoi, description, nombre_tours = vue.creer_tournoi()
        tournoi = Tournoi(nom_tournoi, lieu_tournoi, date_debut_tournoi, date_fin_tournoi, description, type_tournoi, nombre_tours)
        data_tournoi.append(tournoi)

        with open('data_tournoi.json', 'w') as file:
            data_tournoi = json.dumps([j.to_dict() for j in data_tournoi], indent = 4)
            file.write(data_tournoi)
            print(data_tournoi)

        with open('data_tournoi.json', 'r') as fichier_tournoi:
            data_lues = json.load(fichier_tournoi)
            print(data_lues)

        #lecture cles individuelles
        #cle_tournoi = open('data_tournoi.json', 'r')
        #data_lues = cle_tournoi.read()
        #affichage des données du tournoi sous forme de dictionnaire
        #cle = json.loads(data_lues)
        #print("Clé : ")
        #print(cle[0])
        #print(cle['Nom du tournoi'])
        #print(type(cle))
