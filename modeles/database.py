import json
from modeles.player import Joueur
#from modeles.tour import Round
from modeles.tournoi import Tournoi
from typing import List
from uuid import UUID


class Database:
    def __init__(self, joueurs: List[Joueur], tournois: List[Tournoi]):
        self.joueurs = joueurs
        self.tournois = tournois

    """def get_joueur_by_id(self, id: UUID) -> Joueur | None:
        for j in self.joueurs:
            if j.id == id:
                return j

        return None"""

    def to_dict(self) -> dict:
        return {
            "joueurs": [j.to_dict() for j in self.joueurs],
            "tournois": [t.to_dict() for t in self.tournois],
        }

    def save(self, filename: str):
        with open(filename, "w") as file:
            file.write(json.dumps(self.to_dict(), indent=4))

    @classmethod
    def load(cls, filename: str) -> "Database":
        with open(filename, "r") as file:
            data = json.loads(file.read())
            joueurs = [Joueur(**data_joueur) for data_joueur in data["joueurs"]]
            tournois = []
            for data_tournoi in data["tournois"]:
                tournoi = Tournoi(data_tournoi["id"], data_tournoi["nom_tournoi"], [])
                # ajout des joueurs dans l'instance tournoi
                for joueur_id in data_tournoi["joueurs"]:
                    selected_joueur = [j for j in joueurs if j.id == joueur_id]
                    if len(selected_joueur) > 0:
                        tournoi.add_joueur(selected_joueur[0])
                # --
                tournois.append(tournoi)

            return Database(joueurs, tournois)