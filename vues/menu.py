class AffichageMenu:
    def __init__(self):
        self.menu = ['1. Nouveau tournoi et saisie des joueurs', '2. Affichage des matches', '3. Saisie des resultats du tour',
                     '4. Matchs du tour suivant', '5. Affichage du classement', '6. Affichage des joueurs', '7. Affichage du tournoi', '0. Quitter']

    def display_menu(self):
        for i in self.menu:
            print(i)
