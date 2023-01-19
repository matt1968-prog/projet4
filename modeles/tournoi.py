class Tournoi:

	def __init__(self, nom_tournoi, lieu_tournoi, date_debut, date_fin, joueurs, controle_temps: str, description: str, nombre_tours=4):
		self.nom_tournoi = nom_tournoi
		self.lieu_tournoi = lieu_tournoi
		self.date_debut = date_debut
		self.date_fin = date_fin
		self.nombre_tours = nombre_tours
		self.controle_temps = controle_temps
		self.description = description
		self.joueurs = joueurs
        