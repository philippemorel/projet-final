from personnage import Personnage
from pirate import Pirate
from marine import Marine

class Equipage():
    
    def __init__(self, nom, is_yonko):
        self.nom = nom
        self.is_yonko = is_yonko
        self.lst_membres : list[Personnage] = []

    def __eq__(self, autre_equipage):
        if self.nom == autre_equipage.nom:
            return True
        else :
            return False
        
    def to_dict(self):
        list_membres_dico = []

        for membre in self.lst_membres:
            dico_membre = membre.to_dict()
            list_membres_dico.append(dico_membre)

        return {
            "nom": self.nom,
            "yonko": self.is_yonko,
            "membres": list_membres_dico
        }
        
    def force_total_equipe(self) -> int:
        """Méthode pour calculer la force total d'une équipe
        
        Returns:
            int: La force de l'équipage
        """
        force_total = 0

        for membre in self.lst_membres:
            force_total += membre.calcul_force_total()

        print(force_total)
        return force_total
        
                


