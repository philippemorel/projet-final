from personnage import Personnage


class Pirate(Personnage):
    #! doc docstring


    def __init__(self, nom, job, age, size, use_fruit, fruit, vivant, prime: int):
        super().__init__(nom, job, age, size, use_fruit, fruit, vivant)
        self.prime = prime

    def __str__(self) :
        if self.use_fruit == False :    
            return f"Nom: {self.nom}, Job: {self.job}, Force: {self.force}, Age: {self.age}, Taille: {self.size}, À un fruit: {self.use_fruit}, Point de vie: {self.pv}, Prime: {self.prime}"
        else :
            return f"Nom: {self.nom}, Job: {self.job}, Force: {self.force}, Age: {self.age}, Taille: {self.size}, À un fruit: {self.use_fruit}, Type de fruit: {self.fruit.fruit_type}, Point de vie: {self.pv}, Prime: {self.prime}"

    def to_dict(self): 
        return {
            "nom" : self.nom,
            "job" : self.job,
            "force" : self.force,
            "age" : self.age,
            "size" : self.size,
            "use_fruit" : self.use_fruit,
            "fruit" : self.fruit.to_dict(),
            "pv" : self.pv,
            "vivant" : self.vivant,
            "prime" : self.prime
        }
    



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
    
    
    def calcul_puissance_prime(self):
        force_prime = 0

        if not self.prime:
            return 0

        try:
            prime_str = self.prime.replace('.', '')
            prime = int(prime_str)

            if prime > 5_000_000_000:
                force_prime += 5000
            elif prime > 3_000_000_000:
                force_prime += 3000
            elif prime > 1_000_000_000:
                force_prime += 1000
            elif prime > 1_000_000:
                force_prime += 100

        except ValueError:
            return 0

        return force_prime
        
    
        
        
    def calculer_puissance_fruit(self, force) -> int:
        """Méthode pour calculer la puissance selon le type de fruit

        Args:
            force (int): La force d'un perso

        Returns:
            int: La nouvelle force du perso
        """
                #todo calcul avec les type de fruits
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
    
    def calcul_force_total(self):
        """Méthode pour calculer le total de la force

        Returns:
            int: Le total de la force
        """
        prime = self.calcul_puissance_prime()

        age = self.caculer_puissance_age()
        force = prime + age + self.force
        total = self.calculer_puissance_fruit(force)

        return total
    
        
        

        