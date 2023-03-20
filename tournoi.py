from vues.player import Joueur
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
from pprint import pprint
from typing import List
from uuid import UUID, uuid4


def main():

    #  dic_joueurs = {}
    choix = -1
    nouveau_tournoi = False
    NBRE_JOUEURS = 4
    MAX_ROUND = 4
    round_number = 1
    while choix != 0:
        menu_ecran = AffichageMenu()
        menu_ecran.display_menu()
        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print(f"Valeur {choix} non valide. Faites un autre choix.")
            if choix < 0 or choix > 8:
                print("La valeur doit être comprise 0 et 8\n")
        else:
            if choix < 1 or choix > 7:
                print("\nLe choix doit être un entier compris entre 0 et 7\n")
            if choix >= 0 and choix < 9:
                if choix == 1:
                    nouveau_tournoi = False
                    while nouveau_tournoi == False:

                        print("Pour charger le tournoi en cours, sélectionnez le choix 2")
                        print
                        nouveauT = str(input("Etes-vous sur de vouloir creer un nouveau tournoi (O/N) ?"))
                        if nouveauT == "o":
                            nouveau_tournoi = True

                    print("Création du tournoi\n")
                    controleur_tournoi = TournoiControleur()
                    controleur_tournoi.create()
                    #tournoi_cree=True
                    # affichage_tournoi=afficher_tournoi() ne trouve pas afficher_tournoi
                    #nouveau_tournoi = Tournoi()
                    #nouveau_tournoi.afficher_tournoi()
                    print()
                    """print(f"Saisie des {NBRE_JOUEURS} joueurs\n")
                    controleur_joueur = JoueurControleur()
                    controleur_joueur.create()  #affichage de la liste des données tournoi depuis controleurs/creation_tournoi
                    #Affectation des matchs joués avant le premier tour pour éviter qu'un joueur puisse se rencontrer lui-même lors du premier tour (ou d'un tour suivant).MAJ après chaque match
                    matchs_joues = []
                    rows, cols = (NBRE_JOUEURS, NBRE_JOUEURS)
                    for i in range(cols):
                        col = []
                        for j in range(rows):
                            if i == j:
                                col.append(1)
                            else:
                                col.append(0)
                        matchs_joues.append(col)
                    print(matchs_joues)  #  à fin d'information seulement"""

                elif choix == 2:
                    print(f"Saisie des {NBRE_JOUEURS} joueurs\n")
                    controleur_joueur = JoueurControleur()
                    controleur_joueur.create()  #affichage de la liste des données tournoi depuis controleurs/creation_tournoi
                    #Affectation des matchs joués avant le premier tour pour éviter qu'un joueur puisse se rencontrer lui-même lors du premier tour (ou d'un tour suivant).MAJ après chaque match
                    matchs_joues = []
                    rows, cols = (NBRE_JOUEURS, NBRE_JOUEURS)
                    for i in range(cols):
                        col = []
                        for j in range(rows):
                            if i == j:
                                col.append(1)
                            else:
                                col.append(0)
                        matchs_joues.append(col)
                    print(matchs_joues)  #  à fin d'information seulement

                elif choix == 3:
                    # définition des matchs du premier tour selon le classement ELO des joueurs (système suisse) ou des tours suivants
                    print()
                    with open('data_joueurs.json', 'r') as file:
                        data = json.loads(file.read())
                        dao = JoueurDAO()
                        joueurs = dao.load()
                        joueurs.sort(key=lambda j: j.rating, reverse=True)

                    if round_number == 1:
                        print(f"Matchs du tour {round_number}\n")
                        for i in range(0, 2):
                            print(f"Match  {i+1} : ")
                            print(joueurs[i].nom + " vs " + joueurs[i+2].nom)
                            match = ([joueurs[i].nom, joueurs[i].rating], [joueurs[i+2].nom, joueurs[i+2], joueurs[i+2].rating])
                        print()
                    
                    elif round_number > 1 and round_number < MAX_ROUND:
                        print(f"Matchs du tour {round_number}\n")
                        round_number += 1
                        joueurs.sort(key=lambda j: j.score)
                        j=0
                        for i in range(0, 2):
                            print(f"Match  {i+1} : ")
                            print(joueurs[j].nom + " vs " + joueurs[j+1].nom)
                            match = ([joueurs[j].nom], [joueurs[j+1].nom])
                            j += 2
                        print()

                elif choix == 4:
                    print("Pour les résultats, 1=gain premier joueur, 2=gain second joueur, 0=match nul\n")

                    print(f"Résultats du tour {round_number}\n")
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
                    
                    elif round_number > 1 and round_number < 5: 
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
                    
                    #round_number += 1
                    
                    # maj des matchs disputés
                    rows, cols = (NBRE_JOUEURS, NBRE_JOUEURS)
                    for i in range(cols):
                        #col = []
                        for j in range(rows):
                                col.append(1)
                        matchs_joues.append(col)
                    print(matchs_joues)  #  à fin d'information seulement

                    #enregistrement après saisie dees résultats du tour achevé
                    with open('data_joueurs.json', 'w') as file:
                        data_joueurs = json.dumps([j.to_dict() for j in joueurs], indent=4)
                        file.write(data_joueurs)

                    # actualisation du tableau des matchs joués
                    rows, cols = (NBRE_JOUEURS, NBRE_JOUEURS)
                    for i in range(cols):
                        #col = []
                        for j in range(rows):
                            col.append(1)
                        matchs_joues.append(col)
                        #print("Matchs joués {matchs_joues}")

                    #classement
                    joueurs.sort(key=lambda j: j.score, reverse=True)

                    print(f"Classement après le tour {round_number}\n")
                    for i in joueurs:
                        print(i.nom, i.prenom, i.score)
                    print()

                    round_number += 1

                    """# enregistrement du fichier AJOUT DU 17 MARS AU SOIR A VERIFIER
                    with open('data_joueurs.json', 'w') as file:
                        data_joueurs = json.dump(file)
                        file.write(data_joueurs)"""

                elif choix == 5:
                    if round_number < MAX_ROUND:
                        print(f"Matchs du tour {round_number}\n")
                        round_number += 1
                        j=0
                        for i in range(0, 2):
                            print(f"Match  {i+1} : ")
                            print(joueurs[j].nom + " vs " + joueurs[j+1].nom)
                            match = ([joueurs[j].nom], [joueurs[j+1].nom])
                            j += 2
                    print()

                elif choix == 6:
                    dao = JoueurDAO()
                    joueurs = dao.load()
                    joueurs.sort(key=lambda j: j.rating, reverse=True)
                    #print(joueurs)
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
                    for i in joueurs:
                        print(i.nom, i.prenom, i.score)
                    print()

                elif choix == 8:
                    dao_tournoi = TournoiDAO()
                    print("Tournoi actuel :\n")
                    donnees_tournoi = dao_tournoi.load()
                    for i in donnees_tournoi:
                        print(f"Nom du tournoi : {i.nom_tournoi}\nLieu du tournoi : {i.lieu_tournoi}\nDate de debut du tournoi : {i.date_debut_tournoi}\nDate de fin de tournoi : {i.date_fin_tournoi}\n")
                    print()

                elif choix == 0:
                    exit()


if __name__ == "__main__":
    main()
