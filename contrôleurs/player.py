from vues.creation_joueurs import CreationJoueurView
from modeles.player import Joueur
import json

class JoueurControleur:

    def create(self):
        vue = CreationJoueurView()
        joueurs = []
        for i in range(1,3):
            nom, prenom, dob, sexe, rating  = vue.creer_joueur()
            joueur = Joueur(nom, prenom, dob, sexe, rating, score = 0)
            joueurs.append(joueur)
        
        with open ('data.json', 'w') as file:
            data = json.dumps([j.to_dict() for j in joueurs], indent =4)
            file.write(data)