from vues.player import Joueur
#from modeles.player_before_first_round import JoueursPremierTour
from modeles.player import Joueur
from vues.tournoi import Tournoi
from vues.match import Match
from vues.round import Tour
from vues.menu import AffichageMenu
from vues.tri_joueurs import TriJoueurs
from contrôleurs.creation_joueurs import CreationJoueur
from contrôleurs.creation_tournoi import NouveauTournoi
from datetime import date
import json
#from contrôleurs.creation_joueurs import tri_alpha
#from contrôleurs.creation_joueurs import tri_elo


def main():
    menu_ecran = AffichageMenu()
    menu_ecran.display_menu()

    joueurs = []
    choix=-1
    while choix!=0:
        try:
            choix = int(input("Votre choix :"))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
        else:
            if choix >= 0 and choix <8:       
                if choix == 1:
                    print("Saisie des joueurs")
                    #nouveaux_joueurs = CreationJoueur()
                    #nouveaux_joueurs.creer_joueurs()
                    #nouveaux_joueurs.tri_alpha()
                    #joueurs.tri_alpha
                    #joueurs.tri_elo
                    nouveau_tournoi = NouveauTournoi()
                    nouveau_tournoi.afficher_tournoi()

            elif choix == 2:
                pass

            elif choix == 3:
                pass

            elif choix == 4:
                print("Test Choix 4")

            elif choix == 5:
                pass

            elif choix == 6:
                print("Liste des joueurs\n")
                tri = TriJoueurs()
                tri.tri_alpha(joueurs)
                tri.tri_elo(joueurs)

            elif choix == 0:
                exit()
        

if __name__ == "__main__":
    main()