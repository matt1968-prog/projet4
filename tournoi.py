from vues.player import Joueur
#from modeles.player_before_first_round import JoueursPremierTour
from modeles.player import Joueur
from vues.tournoi import Tournoi
from vues.match import Match
from vues.round import Tour
from vues.menu import AffichageMenu
from vues.creation_joueurs import Joueur
#from vues.creation_joueurs import creer_joueurs
from vues.tri_joueurs import TriJoueurs
from vues.creation_joueurs import CreationJoueur
from vues.creation_tournoi import NouveauTournoi
from datetime import date
import json
#from contrôleurs.creation_joueurs import tri_alpha
#from contrôleurs.creation_joueurs import tri_elo


def main():
    

    joueurs = []
    choix=-1
    while choix!=0:
        menu_ecran = AffichageMenu()
        menu_ecran.display_menu()
        try:
            choix = int(input("Votre choix :"))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
        else:
            if choix >= 0 and choix <8:       
                if choix == 1:
                    print("Création du tournoi")
                    
                    #nouveaux_joueurs.tri_alpha()
                    
                    #joueurs.tri_elo
                    nouveau_tournoi = NouveauTournoi()
                    nouveau_tournoi.afficher_tournoi()
                    #print()
                    print("Saisie des 8 joueurs")
                    print()
                    nouveaux_joueurs = CreationJoueur()
                    nouveaux_joueurs.creer_joueurs()
                    print()
                    #print("Liste des joueurs par ordre alphabétique")
                    #nouveaux_joueurs.tri_alpha()

                elif choix == 2:
                    pass

                elif choix == 3:
                    pass

                elif choix == 4:
                    pass

                elif choix == 5:
                    pass

                elif choix == 6:
                    print("Liste des joueurs\n")
                    joueurs.sort(key=lambda j: j.nom, reverse=False)
                    print("\nClassement par ordre alphabétique : \n")        
                    for i in joueurs:
                        print(i.nom, i.prenom, i.rating)

                elif choix == 0:
                    exit()
        

if __name__ == "__main__":
    main()