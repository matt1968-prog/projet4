import json


class Joueur:
    def __init__(self, nom, prenom, dob, sexe, id, rating, score=0):
        self.nom = nom
        self.prenom = prenom
        self.dob = dob
        self.id = id
        self.rating = rating
        self.sexe = sexe
        self.score = score

    def to_dict(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'dob': self.dob, 'rating': self.rating, 'sexe': self.sexe, 'id': self.id, 'score': self.score}


class JoueurDAO:
    """def to_dict(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'dob': self.dob, 'rating': self.rating, 'sexe': self.sexe, 'id :': self.id, 'score': self.score}"""

    def save(self, joueurs):
        with open('data_joueurs.json', 'w') as file:
            data_joueurs = json.dumps([j.to_dict() for j in joueurs], indent=4)
            file.write(data_joueurs)

    def load(self):
        with open('data_joueurs.json', 'r') as file:
            data_joueurs = json.loads(file.read())
            joueurs = []
            for d in data_joueurs:
                j = Joueur(**d)
                joueurs.append(j)
            #print(joueurs)
            return joueurs
