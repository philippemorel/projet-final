from gestionnaire import Gestionnaire
import matplotlib.pyplot  as plt
from personnage import Personnage
from equipage import Equipage
from marine import Marine
from pirate import Pirate

class Statistiques():


    def __init__(self, lst_equipage , lst_perso):
        self.lst_equipage : list[Equipage] = lst_equipage
        self.lst_perso : list[Personnage] = lst_perso


    def pie_vivant_mort_inconue(self):
        """Méthode pour faire un pie graph des personnages selon leur status
        """
        #todo name
        #todo unknown
        #todo null
        #todo dead
        #todo  deceased
        #todo vivant et living ses la meme chose
        unknown = 0
        vivant = 0
        dead = 0
        for person in self.lst_perso :
            verif = person.vivant
            #todo si vivant
            if verif == "vivant" :
                vivant += 1
            elif verif == "living":
                vivant +=1
            #todo si mort
            elif verif == "dead":
                dead += 1 
            elif verif == "deceased":
                dead += 1 
            #todo si on sais pas
            elif verif == "null":
                unknown += 1 
            elif verif == "unknown":
                unknown += 1 
            else:
                unknown += 1 
        labels = ["vivant","mort","on_sais_pas"]
        size = [vivant,dead,unknown]
        plt.pie(size, labels=labels, autopct='%1.1f%%')
        plt.title("Graphique circulaire de qui est mort, vivant ou porté disparu")

        plt.show()
        
    def nb_perso_range_prime(self):
        """Méthode pour faire un graphiqe qui classe les perso selon la valeur de leur prime

        Args:
            force (int): La force d'un perso

        Returns:
            int: La nouvelle force du perso
        """
        bande_1 = 0 #? 100 000
        bande_2 = 0 #? 1 000 000
        bande_3 = 0 #? 10 000 000 
        bande_4 = 0 #? 100 000 000
        bande_5 = 0 #? 1 000 000 000
        bande_6 = 0 #? 3 000 000 000
        bande_7 = 0 #? 5 000 000 000
        bande_the_beast = 0
        for person in self.lst_perso :
            try:
                prime_str = person.prime.replace('.', '')
                prime = int(prime_str)

                if prime <= 100_000:
                    bande_1 += 1
                elif prime <= 1_000_000:
                    bande_2 += 1
                elif prime <= 10_000_000:
                    bande_3 += 1
                elif prime <= 100_000_000:
                    bande_4 += 1
                elif prime <= 1_000_000_000:
                    bande_5 += 1
                elif prime <= 3_000_000_000:
                    bande_6 += 1
                elif prime <= 5_000_000_000:
                    bande_7 += 1
                if prime > 5000000000 :
                    bande_the_beast += 1
                    
            except AttributeError:
                pass

        categories = ["100k", "1M", "10M", "100M", "1B", "3B", "5B","the beast"]
        valeurs = [bande_1,bande_2,bande_3,bande_4,bande_5,bande_6,bande_7,bande_the_beast]



        plt.bar(categories, valeurs)

        plt.title("Graphique à bandes")
        plt.xlabel("valeur de la prime")
        plt.ylabel("Nombre de personne dans groupé par valeur de prime")

        plt.show()

    def force_en_fonction_age(self) :
        

        ages = []
        forces = []

        for person in self.lst_perso:
            #todo isinstance permet de savoir si ce personnage est un marine
            if isinstance(person, Marine):
                Marine.calcul_force_total(person)
            #todo isinstance permet de savoir si ce personnage est un pirate
            elif isinstance(person, Pirate):
                Pirate.calcul_force_total(person)
            if person.age and person.force:
                try:
                    age = int(person.age)
                except :
                    continue  



    def force_en_fonction_age(self):
        """Méthode pour faire un graphique qui classe les personnages en fonction de la force et l'age
        """
        ages = []
        forces = []

        for person in self.lst_perso:

            # calcul de la force réelle selon le type
            if isinstance(person, Marine):
                person.force = person.calcul_force_total()

            elif isinstance(person, Pirate):
                person.force = person.calcul_force_total()

            try:
                ages.append(int(person.age))
                forces.append(int(person.force))

            except (ValueError, TypeError):
                continue

        import matplotlib.pyplot as plt

        plt.scatter(ages, forces)

        plt.title("Force en fonction de l'âge")
        plt.xlabel("Âge")
        plt.ylabel("Force")

        plt.show()