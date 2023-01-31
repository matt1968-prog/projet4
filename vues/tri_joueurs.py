class TriJoueurs:

    def __init__(self, joueurs)):
        self.joueurs = joueurs
     #classement alphabétique   
    def tri_alpha(joueurs):    
        joueurs.sort(key=lambda j: j.nom, reverse=False)
        print("\nClassement par ordre alphabétique : \n")        
        for i in joueurs:
            print(i.nom, i.prenom, i.rating)
    
    """#classement par ELO   
    def tri_elo(joueurs):
        joueurs.sort(key=lambda j: j.rating, reverse=True)
        print("\nClassement par ELO : \n")        
        for i in joueurs:
            print(i.nom, i.prenom, i.rating)
            # Convert into the JSON object after sorting
    # Sort the JSON data based on the value of the brand key
    data.sort(key=lambda x: x["nom"])"""

    # Print the sorted JSON data
    print("The sorted JSON data based on the value of the brand:\n{0}".format(datas))