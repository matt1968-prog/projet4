class NouveauTournoi:

    def __init__(self, nom_tournoi, lieu_tournoi, date_tournoi, joueurs: int, type_tournoi:  int, description: str):
        self.nom_tournoi = input("Nom du tournoi :\n")
        self.lieu_tournoi = input("Lieu du tournoi :\n")
        self.date_tournoi = input("Date du tournoi : ")
        self.nombre_tours = 4
        self.type_tournoi = int(input("Type de tournoi : Rapide(1), Blitz(2), Bullet(3) (Rapide par défaut) : \n"))
        self.description = input("Description (facultatif, taper sur Entrée pour ne pas mettre de description) \n")
        nouveau_tournoi = NouveauTournoi(nom_tournoi, lieu_tournoi, date_tournoi, joueurs, type_tournoi, description)
        
    def afficher_tournoi():
        print(nouveau_tournoi.nom_tournoi)
        print(lieu_tournoi)
        print(date_tournoi)
        print(joueurs)
        print(nombre_tours)
        print(type_tournoi)
        print(description)
    