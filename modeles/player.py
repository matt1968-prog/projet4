class Joueur:
    def __init__(self, nom, prenom, dob, sexe, rating, score=0):
        self.nom = nom
        self.prenom = prenom
        self.dob = dob
        self.rating = rating
        self.sexe = sexe
        self.score = score
        
    def to_dict(self):
        return {'nom':self.nom, 'prenom': self.prenom, 'Date de naissance': self.dob, 'ELO': self.rating, 'Sexe': self.sexe, 'Score': self.score}