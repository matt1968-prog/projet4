class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1=joueur1
        self.joueur2=joueur2
        
        
        
    def display_match():
        for i in range(0,3):
            print(f"Match  {i} : ")
            print(joueurs[i].nom +" vs "+ joueurs[i+3].nom)
            match=([joueurs[i].nom, joueurs[i].score], [joueurs[i+3].nom, joueurs[i+3], joueurs[i+3].score])
