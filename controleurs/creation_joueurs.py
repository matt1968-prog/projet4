from vues.creation_joueurs import CreationJoueurView
from modeles.player import Joueur, JoueurDAO
import json


class JoueurControleur:

    def create(self):
        vue = CreationJoueurView()
        joueurs = []
        for i in range(1, 5):
            nom, prenom, dob, sexe, id, rating = vue.creer_joueur()
            joueur = Joueur(nom, prenom, dob, sexe, id, rating, score=0)
            joueurs.append(joueur)
            #print(joueurs)

        dao = JoueurDAO()
        dao.save(joueurs)
        
        print(joueurs)
