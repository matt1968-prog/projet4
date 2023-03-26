import json
from vues.player import Joueur
from modeles.player import Joueur, JoueurDAO
from modeles.tournoi import TournoiDAO
from modeles.tour import Round
from vues.tournoi import Tournoi
from vues.match import Match
from vues.tour import CreationTourView
from vues.menu import AffichageMenu
from vues.creation_joueurs import CreationJoueurView
from vues.creation_tour import CreationTourView
from datetime import date
from controleurs.creation_joueurs import JoueurControleur
from controleurs.creation_tournoi import TournoiControleur
from uuid import UUID, uuid4
from controleurs.creation_tours import TourControleur
from datetime import datetime
import locale
from pprint import pprint
from typing import List


def main():

    choix = -1
    nouveau_tournoi = False
    NBRE_JOUEURS = 4
    MAX_ROUND = 4
    round_number = 1

    nouveau_tournoi = False
    matchs = []
    nom_base_tour = "Round "
    tournoi_termine = False

    #round_name = "Tournoi test"
    #controleur_tour = ControleurTour()
    #controleur_tour.create()
    exit

    while choix != 0:
        menu_ecran = AffichageMenu()
        menu_ecran.display_menu()
        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
            if choix < 0 or choix > 8:
                print("La valeur doit être un entier compris entre 0 et 8\n")
        else:
            if choix < 1 or choix > 8:
                print("\nLe choix doit être un entier compris entre 0 et 8\n")
            if choix >= 0 and choix < 9:
                if choix == 1:

                    while nouveau_tournoi == False:

                        print("Le nouveau tournoi va effacer l'ancien tournoi, s'il existe")
                        nouveau_tournoi = True

                    print("Création du tournoi\n")
                    controleur_tournoi = TournoiControleur()
                    controleur_tournoi.create()
                    print()

                elif choix == 2:
                    print(f"Saisie des {NBRE_JOUEURS} joueurs\n")
                    controleur_joueur = JoueurControleur()
                    controleur_joueur.create()  #affichage de la liste des données tournoi depuis controleurs/creation_tournoi
                    #Affectation des matchs joués avant le premier tour pour éviter qu'un joueur puisse se rencontrer lui-même lors du premier tour (ou d'un tour suivant).MAJ après chaque match
                    #méthode affectation des matchs avec tableau à deux dimensions
                    print("Initialisation de la grille des matchs par index, 1 = joueur de l'index correspondant est le joueur lui-même, match impossible\n")
                    matchs_joues = []

                    for ligne in range(NBRE_JOUEURS):
                        nvligne = []
                        for col in range(NBRE_JOUEURS):
                            if ligne == col:
                                nvligne.append(1)
                            else:
                                nvligne.append(0)
                        matchs_joues.append(nvligne)

                    for ligne in matchs_joues:
                        print(ligne)


                elif choix == 3:
                    # définition des matchs du premier tour selon le classement ELO des joueurs (système suisse) ou des tours suivants
                    print()
                    if not tournoi_termine == True and nouveau_tournoi == True:
                        with open('data_joueurs.json', 'r') as file:
                            data = json.loads(file.read())
                            dao = JoueurDAO()
                            joueurs = dao.load()
                            joueurs.sort(key=lambda j: j.rating, reverse=True)

                        # matchs du premier tour (système suisse)
                        if round_number == 1:
                            # création du tour MVC
                            id = uuid4()
                            round_name = nom_base_tour + str(round_number)
                            date_heure_debut = "23 mars 10h00"
                            date_heure_fin = "24 mars 20h00"
                            #round_name = Round(id, round_name, round_number,
                                               #date_heure_debut, date_heure_fin, []) #INSERER PARAMETRES
                            #print(f"Paramètres du tour {round}\n")
                            print(f"Nom du tour : {round_name}\n")
                            controleur_tour = TourControleur(id, round_name, round_number, date_heure_debut, date_heure_fin, [])
                            controleur_tour.create()
                            print(f"Matchs du tour {round_number}\n")
                            print("-----------------")
                            print()
                            for i in range(0, 2):
                                print(f"Match  {i+1} : ")
                                print(joueurs[i].nom + " vs " + joueurs[i+2].nom)
                                match = ([joueurs[i].nom, joueurs[i].score], [joueurs[i+2].nom, joueurs[i+2], joueurs[i+2].score])
                                #round.matchs.append(match)
                            print()

                        # à partir du tour 2, appariement en fonction des scores dans le tournoi (1 contre 2, 3 vs 4 etc.)
                        elif round_number > 1 and round_number < MAX_ROUND:
                            # création du tour  CONTROLEUR OU CLASSE SIMPLE ?
                            round_name = nom_base_tour +str(round_number)
                            print(f"Nom du tour : {round_name}\n")
                            #controleur_tour = TourControleur()
                            #controleur_tour.create()
                            print(f"Matchs du tour {round_number}\n")
                            #tour = Round(round_name, round_number, matchs)
                            joueurs.sort(key=lambda j: j.score)
                            j=0
                            for i in range(0, 2):
                                print(f"Match  {i+1} : ")
                                print(joueurs[j].nom + " vs " + joueurs[j+1].nom)
                                match = ([joueurs[j].nom], joueurs[j].score, [joueurs[j+1].nom, joueurs[j+1].score])
                                matchs.append(match)
                                j += 2
                            print()

                            match = ([joueurs[i].nom, joueurs[i].score], [joueurs[i+1].nom, joueurs[i+1], joueurs[i+1].score])
                            matchs.append(match)
                    else:
                        print("Le tournoi est terminé ou aucun nouveau tournoi n'a été créé.\n")
                        continue  

                elif choix == 4:
                    if not tournoi_termine == True:
                        print("Pour les résultats, 1=gain premier joueur, 2=gain second joueur, 0=match nul\n")

                        print(f"Résultats du tour {round_number}")
                        print("-----------------")
                        print()
                        if round_number == 1:
                            for i in range(0, 2):
                                print(joueurs[i].nom + " vs " + joueurs[i+2].nom)
                                resultat = int(input("Résultat : "))

                                if resultat == 1:
                                    joueurs[i].score += 1
                                elif resultat == 2:
                                    joueurs[i+2].score += 1
                                elif resultat == 0:
                                    joueurs[i].score += 0.5
                                    joueurs[i+2].score += 0.5
                                else:
                                    print("Donnée non valide")
                                    print(str(joueurs[i].score) + " " + str(joueurs[i+2].score))# -> vue pour l'affichage, controler pour modif des scores

                            matchs_joues[0][2] = 1
                            matchs_joues[2] [0] = 1
                            matchs_joues[1][3] = 1
                            matchs_joues[3][1] = 1
                            print(f"Nouvelle grille après le tour {round_number} :")
                            print(matchs_joues)

                        elif round_number > 1 and round_number < 4: 
                            j=0
                            for i in range(0, 2):
                                print(f"Match  {i+1} : ")
                                print(joueurs[j].nom + " vs " + joueurs[j+1].nom)
                                match = ([joueurs[j].nom], [joueurs[j+1].nom])
                                resultat = int(input("Résultat : "))
                                if resultat == 1:
                                    joueurs[j].score += 1
                                elif resultat == 2:
                                    joueurs[j+1].score += 1
                                elif resultat == 0:
                                    joueurs[j].score += 0.5
                                    joueurs[j+1].score += 0.5
                                else:
                                    print("Donnée non valide")
                                j += 2

                                matchs_joues[0][1] = 1
                                matchs_joues[1][0] = 1
                                matchs_joues[2][3] = 1
                                matchs_joues[3][2] = 1

                            print(f"Nouvelle grille après le tour {round_number} :")
                            print(matchs_joues)
                            print()

                        elif round_number >3:
                            print("Tous les tours ont été joués. Le tournoi est terminé.\n")
                            tournoi_termine = True
                            continue

                    #enregistrement après saisie des résultats du tour achevé
                    with open('data_joueurs.json', 'w') as file:
                        data_joueurs = json.dumps([j.to_dict() for j in joueurs], indent=4)
                        file.write(data_joueurs)

                    # màj classement après le tour
                    joueurs.sort(key=lambda j: j.score, reverse=True)

                    print(f"Classement après le tour {round_number}\n")
                    for i in joueurs:
                        print(f"{i.nom} {i.prenom} Score : {i.score}")
                    print()

                    round_number += 1
                    
                elif choix == 5:
                    if round_number < MAX_ROUND:
                        print(f"Tour {round_number}\n")
                        #round_number += 1
                        j=0
                        for i in range(0, 2):
                            print(f"Match  {i+1} : ")
                            print(joueurs[j].nom + " vs " + joueurs[j+1].nom)
                            match = ([joueurs[j].nom, joueurs[j].score], [joueurs[j+1].nom, joueurs(j+1).score])
                            j += 2
                    print()

                elif choix == 6:
                    dao = JoueurDAO()
                    joueurs = dao.load()
                    joueurs.sort(key=lambda j: j.rating, reverse=True)
                    print("\nListe par classement ELO : \n")
                    for i in joueurs:
                        print(f"Nom : {i.nom} Prénom {i.prenom} ELO : {i.rating}")
                    print()

                    joueurs.sort(key=lambda j: j.nom, reverse=False)
                    print("\nListe par ordre alphabétique : \n")
                    for i in joueurs:
                        print(i.nom, i.prenom, i.rating)
                    print()

                elif choix == 7:

                    dao = JoueurDAO()
                    joueurs = dao.load()
                    joueurs.sort(key=lambda j: j.score, reverse = True)
                    print(f"\nClassement du tournoi après le tour {round_number}: \n")
                    print("Nom:             Prénom :            Score :")
                    for i in joueurs:
                        print(i.nom, i.prenom, i.score)
                    print()

                elif choix == 8:
                    dao_tournoi = TournoiDAO()
                    print("Tournoi actuel :\n")
                    donnees_tournoi = dao_tournoi.load()
                    for i in donnees_tournoi:
                        print(f"Nom du tournoi : {i.nom_tournoi}\nLieu du tournoi : {i.lieu_tournoi}\nDate de debut du tournoi : {i.date_debut_tournoi}\nDate de fin de tournoi   : {i.date_fin_tournoi}\n")
                    print()

                elif choix == 0:
                    exit()


if __name__ == "__main__":
    main()
