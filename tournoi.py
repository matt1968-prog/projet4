import re

class Tournoi:
	def __init__(self, name_tournoi, lieu_tournoi, date_tournoi, joueurs, nombre_tours=4, controle_temps="", description=""):
		self.name_tournoi=name_tournoi
		self.lieu_tournoi=lieu_tournoi
		self.date_tournoi=date_tournoi
		self.nombre_tours=nombre_tours
		self.controle_temps=controle_temps
		self.description=description
		self.joueurs=joueurs

	def afficher_tournoi(self):
			print(self.name_tournoi)
			print(self.lieu_tournoi)
			print(self.joueurs)
			
class Joueur:
	def __init__(self, nom, prenom, date_naissance, sexe, rating, score=0):
		self.nom=nom
		self.prenom=prenom
		self.date_naissance = date_naissance
		self.sexe=sexe
		self.rating=rating
		self.score=score

	def __str__(self):
		return self.nom, self.prenom, self.rating
        
	def __repr__(self):
		return str(self)

	
	def afficher_joueur(self):
	   	print(self.nom + "\n" +self.prenom+ "\n"+self.sexe+"\n"+self.rating)

class Tour:
	tours=[]
	def __init__(self,round_number,matchs):
		self.round_number=round_number

	def creation_tour():
		print(f"Tour numéro {self.round_number}")

class Match:
	matchs=[]
	def __init__(self):
		#self.joueur1=joueur1
		#self.joueur2=joueur2
		pass

	"""for i in range(0,4):
		match[i]=([joueurs[i], score], [joueur[i+4], score])
		Un match unique doit être stocké sous la forme d'un tuple
		contenant deux listes, chacune contenant deux éléments : 
		une référence à une instance de joueur et un score.
		Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour."""

def main():

	# MENU
	#1 Nouveau tournoi
	#2 Saisie des joueurs -> MODELE
	#3 Saisie tour (appareillement selon indice)
	#4 Saisie résultats d'un tour
	#5 Afficher classement
	#6 Quitter


	print("1. Nouveau tournoi")
	print("2. Saisie des joueurs")
	print("3. Saisie d'un tour")
	print("4. Résultats du tour")
	print("5. Afficher classement")


	"""NOUVEAU TOURNOI

	Création d'un nouveau tournoi et de la liste des joueurs, classés par ELO"""
	
	joueurs=[]

	x=range (1,9)

	for i in x:

		print(f"#Entrer le joueur {i}\n")
    	
		nom=input ("Nom  du joueur\n")
    	
		prenom=input("Prénom du joueur : \n")
    	
		date_naissance=input ("Date de naissance (format JJ/MM/AAA :)") #vérif dans la VUE
		#date=re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(./-)([1-9] |1[0-2])(./-|)19[0-9][0-9]$",date_naissance)
		#print(date)

		sexe=input("Sexe du joueur (H/F) :")

		while True:
			try:
				rating=int(input("Classement ELO (nombre entier: )"))
				if rating>1599:
					break
			except ValueError:
				print("Le classement doit être un chiffre entier, positif et au moins égal à 1600")
		
		joueur=Joueur(nom, prenom, date_naissance, sexe, rating)
		joueurs.append(joueur)
		 
	for i in joueurs:
		#print(f'{i.nom} {i.prenom} {i.date_naissance} {i.sexe}, {i.rating}')
		print(f'{i.nom} {i.rating}')
	
	"""Descending sorting players by rank

	2 loops go though the players' rankings and intervert players where needed"""
	
	for j in range(0,7):
		#table_sorted=true
		for i in range(0,7):
			joueur=joueurs[i].rating
			"""# possibilité d'optimiser le tri en commançant dernier élément du tableau
			sans intérêt pour un petit tableau"""
			print(f'Joueur {joueurs[i].nom} Classement {joueurs[i].rating} index {i}')
			if joueurs[i+1].rating>joueur:
				joueurs[i], joueurs[i+1]=joueurs[i+1], joueurs[i]
				
	print("\nClassement après tri : \n")		
	for i in joueurs:
		print(i.nom, i.prenom, i.rating)

	#Création d'un tournoi

	nom_tournoi=input("Nom du tournoi : ")
	lieu_tournoi=input("Lieu du tournoi : ")
	date_tournoi=input("Date du tournoi : ")
	#self_tournees= ?

	
	tournoi=Tournoi(nom_tournoi,lieu_tournoi,date_tournoi,joueurs)
	tournoi.afficher_tournoi()

	"""Creating 1 roudn (premier match), list of matches
	Add to the index of each of the 4 top players to determine opponent for 1st round"""

	match=[]
	for i in range(0,4):
		match[i]=((joueurs[i],0),(joueurs[i+4],0))
		print(match[i])


if __name__ == "__main__":
    main()