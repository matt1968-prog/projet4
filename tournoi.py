from vues.player import Joueur
#from modeles.player_before_first_round import JoueursPremierTour
from modeles.player import Joueur
from vues.tournoi import Tournoi
from vues.match import Match
from vues.round import Tour
from vues.menu import AffichageMenu
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
    while True:
        try:
            choix = int(input("Votre choix :"))
            if choix >= 0 and choix <8:
                break
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")

    if choix == 1:
        print("Saisie des joueurs")
        nouveaux_joueurs = CreationJoueur
        nouveaux_joueurs.creer_joueurs()
        #joueurs.tri_alpha
        #joueurs.tri_elo
        #nouveau_tournoi = NouveauTournoi
        #nouveau_tournoi.afficher_tournoi()
    elif choix == 2:
        pass
    elif choix == 3:
        pass
    elif choix == 4:
        pass
    elif choix == 5:
        pass
    elif choix == 6:
        pass  
    elif choix == 0:
        exit()


if __name__ == "__main__":
    main()