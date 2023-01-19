class TriJoueurs:

    def __init__(self, joueurs):
        #self.joueurs=joueurs[]

 #classement alphabétique   
    def tri_alpha(joueurs):    
        joueurs.sort(key=lambda j: j.name, reverse=False)
        print("\nClassement par ordre alphabétique : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)
    
  #classement par ELO   
    def tri_elo(joueurs):
        joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.name, i.f_name, i.rating)