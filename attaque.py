from personnage import Personnage
from marine import Marine
from pirate import Pirate
class Attaque(Personnage):





    def calcul_ataque(self,nom_attaque):

       
        puissance = len(nom_attaque)
        puissance *= 6

        for lettre in len(nom_attaque):
            if nom_attaque(lettre) == "a" :
                multi += 2

        attaque_final = puissance * multi
        return attaque_final
