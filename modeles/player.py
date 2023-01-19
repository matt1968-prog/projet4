class Joueur:
    def __init__(self, nom, prenom, dob, rating, score=0):
        self.nom = nom
        self.prenom = prenom
        self.dob = dob
        self.rating=rating
        self.score=score
        """serialized_player = {'name': self.name, 'first name': self.f_name, 'dob' : self.dob,
        'rating' :self.rating, 'sex' : self.sex, 'score' : self.score}
        print(serialized_player)"""