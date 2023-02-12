from vues.creation_joueurs import CreationJoueurView
from modeles.player import Joueur
import json


class JoueurControleur:

    def create(self):
        vue = CreationJoueurView()
        joueurs = []
        for i in range(1, 4):
            nom, prenom, dob, sexe, id, rating = vue.creer_joueur()
            joueur = Joueur(nom, prenom, dob, sexe, id, rating, score=0)
            joueurs.append(joueur)
            print(f"Joueurs : {joueurs}")

        with open('data_joueurs.json', 'w') as file:
            data_joueurs = json.dumps([j.to_dict() for j in file], indent=4)
            file.write(data_joueurs)
            #print(data_tournoi)

    """with open('data_joueurs.json', 'r') as fichier_tournoi:
            data_lues = json.load(fichier_joueur)
            print(data_lues)

        print("\nListe alphabétique des joueurs :\n")
        joueurs.sort(key=lambda j: j.nom)
        for i in joueurs:
            print (i.nom, i.prenom)"""
