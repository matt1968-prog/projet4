#from vues.player import Joueur
from modeles.player import Joueur
from vues.tournoi import Tournoi
from vues.match import Match
from vues.round import Tour
from vues.menu import AffichageMenu
#from vues.creation_joueurs import Joueur
#from vues.creation_joueurs import creer_joueurs
#from vues.tri_joueurs import TriJoueurs
from vues.creation_joueurs import CreationJoueurView
#from vues.creation_tournoi import CreationNouveuTournoi
from datetime import date
from contrôleurs.player import JoueurControleur
from contrôleurs.creation_tournoi import TournoiControleur
from contrôleurs.creation_joueurs import CreationJoueurView
#from contrôleurs.creation_joueurs import tri_alpha
#from contrôleurs.creation_joueurs import tri_elo


def main():
    

    #joueurs = []
    dic_joueurs={}
    choix=-1
    jsonFile = open("data.json", "w")
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
                    
                    #nouveau_tournoi = Tournoi()
                    #nouveau_tournoi.afficher_tournoi()
                    print()
                    print("Saisie des 8 joueurs")
                    print()
                    #controleur = JoueurControleur()
                    #controleur.create()
                    
                #lignes 47 et 48  : ajout
                    controleur_tournoi = TournoiControleur()
                    controleur_tournoi.create()

                elif choix<1 or choix >6:
                    print("Le choix doit être un entier compris entre 0 et 6")
                
                elif choix == 2:
                    pass

                elif choix == 3:
                    pass

                elif choix == 4:
                    pass

                elif choix == 5:
                    pass

                elif choix == 6:
                    print("Liste alphabétique des joueurs\n")
                    joueurs.sort(key=lambda j: j.nom, reverse=False)      
                    print(joueurs)
                    for i in joueurs:
                        print("Nom : {i.nom} Prénom {i.prenom)}")

                elif choix == 0:
                    exit()
        

if __name__ == "__main__":
    main()
