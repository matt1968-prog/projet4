from contrôleurs.creation_joueurs import CreationJoueurView 

class ListeJoueurs:
    pass

    def__init__(self, joueurs)
        
    self.joueurs=joueurs

    def affichage_liste(self, joueurs):
        print("Liste alphabétique des joueurs\n")
        joueurs.sort(key=lambda j: j.nom, reverse=False)      
        print(joueurs)
        for i in joueurs:
            print("Nom : {i.nom} Prénom {i.prenom)}")

    def affichage_liste_ELO(self, joueurs):
        print("Liste des joueurs par classement ELO\n")
        joueurs.sort(key=lambda j: j.nom, reverse=False)      
        print(joueurs)
        for i in joueurs:
            print("Nom : {i.nom} Prénom {i.prenom) ELO : {i.rating)}")