from views.player import Joueur
from models.player_before_first_round import JoueursPremierTour
from views.tournoi import Tournoi
#from views.match import Match
from views.round import Tour
from views.menu import Affichage_Menu
import re
from tinydb import TinyDB

def main():

    #MENU Vue ? Traitement du choix du menu dans Controlers et affichage du menu dans View ?

    menu=Affichage_Menu
    #for i in menu:
        #print(menu[i])

    """NOUVEAU TOURNOI ET SAISIE DES JOUEURS (6 joueurs pour test)

    Création d'un nouveau tournoi et de la liste des joueurs, classés par ELO, donc pour le 1er tour"""
            
    joueurs=[]
    db = TinyDB('db.json')
    players_table = db.table('players')
    players_table.truncate()# clear the table
    
    #def saisie_joueurs()
    for i in range (1,7):
        score=0
        print(f"Saisie du joueur {i}\n")
        
        name=input (f"Nom  du joueur {i} :\n")
        
        f_name=input(f"Prénom du joueur {i} : \n")
        
        dob=input ("Date de naissance :") #vérif dans la VUE
        #date=re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(./-)([1-9] |1[0-2])(./-|)19[0-9][0-9]$",date_naissance)
        #print(date)

        sex=input("Sexe du joueur (H/F), par défaut H :")

        while True:
            try:
                rating=int(input("Classement ELO (nombre entier :) "))
                if rating>1599:
                    break
            except ValueError:
                print("Le classement doit être un entier, positif et au moins égal à 1600")
        
        joueur=Joueur(name, f_name, dob, rating, sex, score=0)
        joueurs.append(joueur)
        
        """Insertion des joueurs dans la BdD Jjon"""
        players_table.insert({'nom': name, 'prénom': f_name, 'date de naissance' : dob,
        'rating' : rating, 'sexe' : sex, 'score' : 0}) 
    
    serialized_players=players_table.all()
    
    for i in joueurs:
        print(f'{i.name} {i.rating} {i.score}')
    
    """Descending sorting players by rank Contrôleur ou modèle ou View ?

    2 loops go though the players' rankings and intervert players where needed"""
    
    """for j in range(0,5):# utiliser sort -> dans Views
        for i in range(0,5):
            joueur=joueurs[i].rating
            if joueurs[i+1].rating>joueur:
                joueurs[i], joueurs[i+1]=joueurs[i+1], joueurs[i]"""
    
    #classement alphabétique
    
    joueurs.sort(key=lambda j: j.name, reverse=False)
    print("\nClassement par ordre alphabétique : \n")        
    for i in joueurs:
        print(i.name, i.f_name, i.rating)
    #print(joueurs)
    
    #classement par ELo (descendant)
    
    joueurs.sort(key=lambda j: j.rating, reverse=True)
    print("\nClassement par ELO : \n")        
    for i in joueurs:
        print(i.name, i.f_name, i.rating)
    #print(joueurs)
    
    #initialisation du tableau des matchs disputés. O si match non joué entre deux joueurs, 1 si match joué (ou i=j)
    matchs_joues=[]
    rows, cols = (6, 6)
    for i in range (cols):
        col=[]
        for j in range(rows):
            if i==j:
                col.append(1)
            else:
                col.append(0)
        matchs_joues.append(col)
    print(matchs_joues) 
    
    j=0
    """for i in range(0,6):
        for j in range(6):
            print(matchs_joues[i][j])
            #print(j)
            #if i!=j:
                #matchs_joues.append(0)
                #matchs_joues[i][j]=0
            #j+=1"""
    
    """#Crating 1st round of a tournament
    Add 3 to the index of each of the 3 top players to determine opponent for 1st round"""

    matchs=[]
    tour=[]
    nbre_joueurs=6
    for i in range(0,3):
        print(f"Match  {i} : ")
        print(joueurs[i].name +" vs "+ joueurs[i+3].name)
        match=([joueurs[i].name, joueurs[i].score], [joueurs[i+3].name, joueurs[i+3], joueurs[i+3].score])
        matchs.append(match)
        tour.append(match)
        matchs_joues[i][i+3]=1
        for i in matchs:
            print(i)
        #print(matchs)

    print("Après le 1er tour, tableau des rencontres :")
    print(matchs_joues)
    
    premier_tour=Tour(1, matchs)
    print(premier_tour)


    #New tournament    
    nouveau_tournoi=[]
    nom_tournoi=input("Nom du tournoi :\n")
    lieu_tournoi=input("Lieu du tournoi :\n")
    date_tournoi=input("Date du tournoi : ")
    nombre_tours=int(input("Nombre_tours (4 par défaut, taper sur Entrée pour 4) :\n"))
    type_tournoi=input("Type de tournoi : Rapide, Blitz, Bullet (Rapide par défaut) : \n")
    description=input("Description (facultatif, taper sur Entrée pour ne pas mettre de description) \n")
    nouveau_tournoi=Tournoi(nom_tournoi,lieu_tournoi,date_tournoi,joueurs,type_tournoi,description)
    nouveau_tournoi.afficher_tournoi()

    #Résultats des matchs et modification des scrores et classements#-> Controler
    print("Pour les résultats, 1=gain premier joueur, 2=gain du second joueur, 0=match nul")
    #saisie des résultats dans la vue
    for i in range(0,3):
        z=i
        print(joueurs[i].name +" vs "+ joueurs[i+3].name) 
        resultat=int(input("Résultat : "))
        if resultat==1:
            joueurs[i].score+=1            
        elif resultat==2:
            joueurs[i+3].score+=1
        elif resultat==0:
            joueurs[i].score+=0.5
            joueurs[i+3].score+=0.5
            matchs_joues[i][z+3]+=0.5
            matchs_joues[i][z+3]+=0.5
        else:
            print("Donnée non valide")    
        print(str(joueurs[i].score) +" " +str(joueurs[i+3].score))# -> vue pour l'affichage, controler pour modif des scores
        matchs_joues[i][z+3]=1
        
    # Affichage du tableau des matchs joueués ou non (0=non joué)
    """for i in range(6):
        for j in range(6):
            print(matchs_joues[i,j])"""
    
    #actualisation des scores des joueurs
    for j in range(0,5):# utiliser sort -> dans Views
        for i in range(0,5):
            joueur=joueurs[i].score
            if joueurs[i+1].score>joueur:
                joueurs[i], joueurs[i+1]=joueurs[i+1], joueurs[i]
                
    print("\nClassement après le 1er match : \n")        
    """for i in range (cols):
        col=[]
        for j in range(rows):
            if i==j:
                col.append(1)
            else:
                col.append(0)
        matchs_joues.append(col)"""
    print(matchs_joues) 
            
if __name__ == "__main__":
    main()