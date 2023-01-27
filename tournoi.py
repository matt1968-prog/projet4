#from vues.player import Joueur
from modeles.player import Joueur
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
                    
                    nouveau_tournoi = NouveauTournoi()
                    nouveau_tournoi.afficher_tournoi()
                    """print()
                    print("Saisie des 8 joueurs")
                    print()
                    nouveau_joueur = CreationJoueur()
                    nouveau_joueur.creer_joueur()
                    joueurs.append(nouveau_joueur)"""
                    #player = nouveau_joueur.to_dict()
                    #jsonString = json.dump(player)
                    #print()
                    #print("Liste des joueurs par ordre alphabétique")
                    #nouveaux_joueurs.tri_alpha()
                    #joueurs.tri_elo
                
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
                    print("Liste des joueurs\n")
                    joueurs.sort(key=lambda j: j.nom, reverse=False)
                    print("\nClassement par ordre alphabétique : \n")        
                    for i in joueurs:
                        print(i.nom, i.prenom, i.rating)

                elif choix == 0:
                    exit()
        

if __name__ == "__main__":
    main()