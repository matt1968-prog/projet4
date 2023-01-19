class Resultats:
    def __init__(self):
        for i in range(0,4):
            z=i
            print(joueurs[i].name +" vs "+ joueurs[i+3].name) 
            try:
            resultat=int(input("Résultat : "))
            if resultat==1:
                joueurs[i].score+=1            
            elif resultat==2:
                joueurs[i+3].score+=1
            elif resultat==0:
                joueurs[i].score+=0.5
                joueurs[i+3].score+=0.5
                matchs_joues[i][i+3]+=0.5
                matchs_joues[i][i+3]+=0.5
            else:
                print("Donnée non valide")    
            except ValueError:
                print("Vous devez saisir 0, 1 ou 2.")