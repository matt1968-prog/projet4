class AffichageMenu:
    def __init__(self):
        self.menu = ['1. Nouveau tournoi et saisie des joueurs', '2. Affichage des matches','3. Saisie des resultats du tour',
        '4. Match du tour suivant', '5. Afficher classement', '6. Affichage des joueurs', '7. Quitter']
        
    def display_menu(self):
        for i in self.menu:
            print(i)
