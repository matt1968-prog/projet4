#from vues.player import Joueur
import json
from modeles.player import Joueur, JoueurDAO
from vues.tournoi import Tournoi
from vues.match import Match
from vues.round import Tour
from vues.menu import AffichageMenu
from vues.creation_joueurs import CreationJoueurView
from datetime import date
from controleurs.creation_joueurs import JoueurControleur
from controleurs.creation_tournoi import TournoiControleur


def main():

    #dic_joueurs = {}
    choix = -1
    #joueur_cree = False
    #tournoi_cree = False
    while choix != 0:
        menu_ecran = AffichageMenu()
        menu_ecran.display_menu()
        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
        else:
            if choix >= 0 and choix <8:
                if choix == 1:
                    print("Création du tournoi\n")
                    controleur_tournoi = TournoiControleur()
                    controleur_tournoi.create()
                    #tournoi_cree=True
                    # affichage_tournoi=afficher_tournoi() ne trouve pas afficher_tournoi
                    nouveau_tournoi = Tournoi()
                    nouveau_tournoi.afficher_tournoi()
                    print()
                    print("Saisie des 8 joueurs\n")
                    controleur_joueur = JoueurControleur()
                    controleur_joueur.create()  #affichage de la liste des données tournoi depuis controleurs/creation_tournoi

                elif choix < 1 or choix > 7:
                    print("Le choix doit être un entier compris entre 0 et 6")

                elif choix == 2:
                    pass

                elif choix == 3:
                    pass

                elif choix == 4:
                    pass

                elif choix == 5:
                    pass
                    """joueurs.sort(key=lambda j: j.rating, reverse=True)
                    print(joueurs)
                    for i in joueurs:
                        print(f"Nom : {i.nom} Prénom {i.prenom} ELO : {i.rating}")"""

                elif choix == 6:
                    """data_joueurs = json.loads(file.read())
                        joueurs = []
                        for d in data_joueurs:
                            j = Joueur(**d)
                            joueurs.append(j)
                        for i in data_joueurs:"""
                    dao=JoueurDAO()
                    joueurs = dao.load()
                    for i in joueurs:
                        print(i.nom, i.prenom, i.rating)
                elif choix == 7:
                    print("Tournoi actuel :\n")
                    dao_tournoi = TournoiDAO()
                    donnees_tournoi = dao_tournoi.load
                    for i in donnees_tournoi:
                        print(i.nom_tournoi, i.date_tournoi, i.lieu_tournoi)


                        #loadafficher_liste_joueurs(joueurs)
                    #joueurs=dao.load()
                    """print("Liste alphabétique des joueurs\n")
                    joueurs.sort(key=lambda j: j.nom)
                    print(joueurs)
                    for i in joueurs:
                        print(f"Nom : {i.nom} Prénom {i.prenom}")"""

                elif choix == 0:
                    exit()


if __name__ == "__main__":
    main()
