class Joueur:
	def __init__(self, nom, prenom, date_naissance, sexe, id, rating, score=0):
		self.nom=nom
		self.prenom=prenom
		self.date_naissance = date_naissance
		self.sexe=sexe
        self.id = id
		self.rating=rating
		self.score=score
    
	"""def __repr__(self):
		return str(self)"""


"""joueurs=[]
    
    #classement par ELo (descendant)
    def tri_elo(joueurs):
		joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)

	 #classement alphabétique
    def tri_alpha(joueurs):
		joueurs.sort(key=lambda j: j.name, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
        print(i.name, i.f_name, i.rating)"""