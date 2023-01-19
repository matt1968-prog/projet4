class Tournoi:

	def __init__(self, nom_tournoi, lieu_tournoi, date_tournoi, joueurs, nombre_tours=4, controle_temps="Rapide", description=""):
		self.name_tournoi=name_tournoi
		self.lieu_tournoi=lieu_tournoi
		self.date_tournoi=date_tournoi
		self.nombre_tours=nombre_tours
		self.controle_temps=controle_temps
		self.description=description
		self.joueurs=joueurs

	def afficher_tournoi(self):
		print(self.nom_tournoi)
		print(self.lieu_tournoi)
		print(self.date_tournoi)
		print(self.joueurs)
		print(self.nombre_tours)
		print(self.controle_temps)
		print(self.description)
