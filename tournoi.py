1#from vues.player import Joueur
import json
from modeles.player import Joueur, JoueurDAO
from modeles.tournoi import TournoiDAO
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
    nouveau_tournoi = False
    #joueur_cree = False
    #tournoi_cree = False
    NBRE_JOUEURS=4
    while choix != 0:
        menu_ecran = AffichageMenu()
        menu_ecran.display_menu()
        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
            if choix <0 or choix >8:
                print("La valeur doit être comprise 0 et 8")
        else:
            if choix < 1 or choix > 7:
                    print("Le choix doit être un entier compris entre 0 et 7")
            if choix >= 0 and choix <8:
                if choix == 1:
                    nouveau_tournoi = False
                    while nouveau_tournoi == False:

                        print("Attention, ce choix supprimera l'ancien tournoi s'il existe\n")
                        print("Pour charger le tournoi en cours, sélectionnez le choix 2")
                        print
                        nouveauT = str(input("Etes-vous sur de vouloir creer un nouveau tournoi (O/N) ?"))
                        if nouveauT == "o":
                            nouveau_tournoi = True
                            
                    print("Création du tournoi  et saisie des joueurs\n")
                    controleur_tournoi = TournoiControleur()
                    controleur_tournoi.create()
                    #tournoi_cree=True
                    # affichage_tournoi=afficher_tournoi() ne trouve pas afficher_tournoi
                    #nouveau_tournoi = Tournoi()
                    #nouveau_tournoi.afficher_tournoi()
                    print()
                    print("Saisie des 8 joueurs\n")
                    controleur_joueur = JoueurControleur()
                    controleur_joueur.create()  #affichage de la liste des données tournoi depuis controleurs/creation_tournoi
                    #Affectation des matchs joués avant le premier tour pour éviter qu'un joueur puisse se rencontrer lui-même lors du premier tour (ou d'un tour suivant).MAJ après chaque match
                    matchs_joues=[]
                    rows, cols = (4, 4)
                    for i in range (cols):
                        col = []
                        for j in range(rows):
                            if i==j:
                                col.append(1)
                            else:
                                col.append(0)
                        matchs_joues.append(col)
                    print(matchs_joues) #à fin d'information seulement

                

                elif choix == 2:
                    #pass
                    #définition des matchs du premier tour selon leur classement ELO
                    
                    with open('data_joueurs.json', 'r') as file:
                        data = json.loads(file.read())
                        dao=JoueurDAO()
                        joueurs = dao.load()
                        joueurs.sort(key=lambda j: j.rating, reverse=True)

                    
                    for i in range(0, 2):
                        print(f"Match  {i+1} : ")
                        print(joueurs[i].nom + " vs " + joueurs[i+2].nom)
                        match=([joueurs[i].nom, joueurs[i].rating], [joueurs[i+2].nom, joueurs[i+2], joueurs[i+2].rating])
                        
                
                elif choix == 3:
                    pass

                elif choix == 4:
                    pass

                elif choix == 5:
                    #pass
                    dao=JoueurDAO()
                    joueurs = dao.load()
                    joueurs.sort(key=lambda j: j.rating, reverse=True)
                    print(joueurs)
                    print("\nListe par classement ELO : \n")
                    for i in joueurs:
                        print(f"Nom : {i.nom} Prénom {i.prenom} ELO : {i.rating}")

                elif choix == 6:
                    
                    dao=JoueurDAO()
                    joueurs = dao.load()             
                    joueurs.sort(key=lambda j: j.nom, reverse=False)
                    print("\nListe par ordre alphabétique : \n")        
                    for i in joueurs:
                        print(i.nom, i.prenom, i.rating)
                    print()
                
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
