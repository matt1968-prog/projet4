class FirstRound:
    def __init__(self, joueurs, round_number=1):
        matchs = [] 
        self.round_number = round_number
        self.joueurs = joueurs
    
        for i in range(0,4):
            print(f"Tour {round_number} Match {i+1} : ")
            print(joueurs[i].name +" vs "+ joueurs[i+3].name)
            match = ([joueurs[i].name, joueurs[i].score], [joueurs[i+3].name,
            joueurs[i+3].score])
            matchs.append(match)
            round.append(match)
            #matchs_joues[i][i+3]=1
        for i in matchs:
            print(i)