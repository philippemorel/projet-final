from fruit import Fruit

class Personnage():
    #! doc docstring

    def __init__(self, nom :str, job :str, age :int, size :int, use_fruit :bool, fruit :Fruit, vivant :str) :
        self.nom = nom
        self.job = job
        self.force = 1000
        self.age = age
        self.size = size
        self.use_fruit = use_fruit
        self.fruit = fruit
        self.pv = 2000
        self.vivant = vivant

    def __str__(self) :
        if self.use_fruit == False :    
            return f"Nom: {self.nom}, Job: {self.job}, Force: {self.force}, Age: {self.age}, Taille: {self.size}, À un fruit: {self.use_fruit}, Point de vie: {self.pv}"
        else :
            return f"Nom: {self.nom}, Job: {self.job}, Force: {self.force}, Age: {self.age}, Taille: {self.size}, À un fruit: {self.use_fruit}, Type de fruit: {self.fruit.fruit_type}, Point de vie: {self.pv}"
        
    def to_dict(self) : 
        return {
            "nom" : self.nom,
            "job" : self.job,
            "force" : self.force,
            "age" : self.age,
            "size" : self.size,
            "use_fruit" : self.use_fruit,
            "fruit" : self.fruit.to_dict(),
            "pv" : self.pv,
            "vivant" : self.vivant
        }
    
    def caculer_puissance_age(self) -> int :
        """Méthode pour calculer la puissance selon l'âge

        Returns:
            int: La puissance calculer
        """
        force_age = 0
        try:
            if "captain" in self.job :
                force_age += 500
        except TypeError:
            pass

        #todo calcul avec l'âge  
        try:
            if self.age < 18 :
                force_age -= 100
            elif self.age < 30 :
                force_age += 100
            elif self.age < 60 :
                force_age += 50
            elif self.age > 60 :
                force_age += 50
        except TypeError:
            pass
        return force_age

    def calculer_puissance_fruit(self, force) -> int:

        if self.use_fruit:

            match self.fruit["fruit_type"]:

                case "Paramecia":
                    force *= 2

                case "Zoan":
                    force *= 1.5

                case "Logia":
                    force *= 2.5

                case "Zoan Mythique":
                    force *= 3

                case "Smile":
                    force *= 1.75

                case "Clone":
                    force *= 3

        return int(force)
    
    def calcul_force_total(self) -> int:
        """Méthode pour calculer le total de la force"""

        age = self.caculer_puissance_age()

        force = age + self.force

        total = self.calculer_puissance_fruit(force)

        return total

    def calculer_pv(self) -> None :
        """Méthode pour calculer le total de pv
        """
        self.pv = self.force * 5

    def attaque(self) -> int :
        """Méthode pour calculer le nombre de dégâts causé par une attaque

        Returns:
            int: Le nombre de dommge
        """
        dammage = self.force * 0.8

        return dammage
    
    def defense(self, dammage) -> int:
        """Méthode pour calculer le total de dégat moins le nombre de dégat bloqué

        Args:
            dammage (int): dommage

        Returns:
            int: dommage 
        """
        dammage *= 0.60

        return dammage
    
    def regen(self, pv_act) -> int :
        
        dammage = self.pv - pv_act

        pv_act += (dammage * 0.7)
        
        return pv_act

    def attaque_fruite(self) -> int:
    
        dammage = self.force * 1.1

        return dammage