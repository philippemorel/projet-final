from personnage import Personnage

class Marine(Personnage):

    def __init__(self, nom, job, age, size, use_fruit, fruit, vivant):
        super().__init__(nom, job, age, size, use_fruit, fruit, vivant)
    
    def caculer_puissance_age(self) :
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
    
    def calculer_puissance_job(self) :
        """Méthode pour calculer la puissance selon la jobdd'un persoe fruit

        Args:
            force (int): La force d'un perso

        Returns:
            int: La nouvelle force du perso
        """
        force_job = 0  
        if self.job == "Chief Admiral" :
            force_job += 4000
        elif self.job == "Admiral" :
            force_job += 3000
        elif self.job == "Vice-Admiral" :
            force_job += 1000
        elif self.job == "Sub-Admiral" :
            force_job += 250
        elif self.job == "Rear Admiral" :
            force_job += 250
        return force_job

    def calculer_puissance_fruit(self, force):
        """Méthode pour calculer la puissance selon le type de fruit

        Args:
            force (int): La force d'un perso

        Returns:
            int: La nouvelle force du perso
        """
            #todo calcul avec les type de fruit     
        if self.use_fruit :

            match self.fruit["fruit_type"]:
                case "Paramecia" :
                    force *= 2

                case "Zoan" :
                    force *= 1.5

                case "Logia" :
                    force *= 2.5

                case "Zoan Mythique" :
                    force *= 3

                case "Smile" :
                    force *= 1.75

                case "Clone" :
                    force *= 3
        return int(force)
            
    def calcul_force_total(self) :
        """Méthode pour calculer le total de la force

        Returns:
            int: Le total de la force
        """
        age = self.caculer_puissance_age()
        job = self.calculer_puissance_job()
        force = age + job
        fruit = self.calculer_puissance_fruit(force)
        total = fruit

        return total