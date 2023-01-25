class Tournoi:

	def __init__(self, nom_tournoi, lieu_tournoi, date_tournoi, type_tournoi: int, description: str, nombre_tours=4):
		self.nom_tournoi = nom_tournoi
		self.lieu_tournoi = lieu_tournoi
		self.date_tournoi = date_tournoi
		#self.date_fin = date_fin
		self.nombre_tours = nombre_tours
		self.type_tournoi = type_tournoi
		self.description = description
		#self.joueurs = joueurs
        