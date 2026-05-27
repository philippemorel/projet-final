from gestionnaire import Gestionnaire
import matplotlib.pyplot  as plt
from personnage import Personnage
from equipage import Equipage
from marine import Marine
from pirate import Pirate
import matplotlib.pyplot as plt
class Statistiques():


    def __init__(self, lst_equipage , lst_perso):
        self.lst_equipage : list[Equipage] = lst_equipage
        self.lst_perso : list[Personnage] = lst_perso

    #? fait 
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
    #? fait 
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
                prime_str = str(person.prime).replace('.', '')
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
                elif prime > 5000000000 :
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



    #? fait 
    def force_en_fonction_age(self):
        """Méthode pour faire un graphique qui classe les personnages en fonction de la force et l'age
        """
        ages = []
        forces = []

        for person in self.lst_perso:

            #todo calcul de la force réelle selon le type
            if isinstance(person, Marine):
                person.force = person.calcul_force_total()

            elif isinstance(person, Pirate):
                person.force = person.calcul_force_total()

            try:
                ages.append(int(person.age))
                forces.append(int(person.force))

            except (ValueError, TypeError):
                continue
            
        

        

        plt.scatter(ages, forces)

        plt.title("Force en fonction de l'âge")
        plt.xlabel("Âge")
        plt.ylabel("Force")

        plt.show()

#!laurent

    def Recherche_dicho(self, id):
            debut = 0
            fin = len(self.lst_perso) - 1

            trouve = False

            while debut <= fin:
                milieu = (debut + fin) // 2
                perso = self.lst_perso[milieu]

                if perso.id == id:
                    return perso

                elif perso.id < id:
                    debut = milieu + 1

                else:
                    fin = milieu - 1

                trouve = True 

            if not trouve:
                print("Aucun personnage trouvée avec cet ID.")

                
    @staticmethod
    def tri_rapide(lst_perso: list[Personnage], element_a_trier : object ):
        """trie rapidement les liste a un element precis

        Args:
            lst_perso (list[Personnage]): est une liste des objet personnage
            element_a_trier (object): est l'objet a trier

        Returns:
            info:  ce qui fait marcher le trie rapide
        """

        lst_tri = lst_perso.copy()

        #todo si la liste est vide ou contient 1 élément
        if len(lst_tri) <= 1:
            return lst_tri

        pivot = lst_tri[-1]

        petits = []
        grands = []

        for i in range(len(lst_tri) - 1):

            #todo AGE
            if element_a_trier == "age":

                valeur_actuelle = lst_tri[i].age or 0
                valeur_pivot = pivot.age or 0

            #todo SIZE
            elif element_a_trier == "size":

                valeur_actuelle = lst_tri[i].size or 0
                valeur_pivot = pivot.size or 0

            #todo PRIME
            elif element_a_trier == "prime":

                valeur_actuelle = lst_tri[i].prime or 0
                valeur_pivot = pivot.prime or 0

            else:
                return lst_tri

            if valeur_actuelle < valeur_pivot:
                petits.append(lst_tri[i])
            else:
                grands.append(lst_tri[i])

        return (
            Statistiques.tri_rapide(petits, element_a_trier)
            + [pivot]
            + Statistiques.tri_rapide(grands, element_a_trier)
        )


    #todo TOP 10 AGE
    def top_10_age(self):
        """permet de savoir le top 10 des ages
        """

        lst_tri = Statistiques.tri_rapide(self.lst_perso, "age")

        for personnage in reversed(lst_tri[-10:]):
            print(f"{personnage.nom} : {personnage.age} ans")


    #todo TOP 10 GRANDEUR
    def top_10_size(self):
        """permet de savoir le top 10 des plus grand
        """

        lst_tri = Statistiques.tri_rapide(self.lst_perso, "size")
        #todo 
        for personnage in reversed(lst_tri[-10:]):
            print(f"{personnage.nom} : {personnage.size} cm")

    #todo savoit max min de la grandeur
    def premier_dernier_size(self):
        """prend le plus grand et le plus petit et les affiche
        """

        lst_tri = Statistiques.tri_rapide(self.lst_perso, "size")

        #todo Plus grand
        plus_grand = lst_tri[-1]

        print(f"Plus grand : {plus_grand.nom} : {plus_grand.size} cm")

        for perso in lst_tri:
            if perso.size is not None:
                print(f"Plus petit : {perso.nom} : {perso.size} cm")
                break
        

    #todo MOYENNE AGE
    def moyenne_age(self):
        """ permet le calcule de la moyenne d'age
        """

        total = 0

        for personnage in self.lst_perso:
            total += personnage.age or 0

        moyenne = total / len(self.lst_perso)

        print(f"L'âge moyen est de {moyenne:.2f} ans")


    #todo MOYENNE GRANDEUR
    def moyenne_size(self):
        """ permet le calcule de la moyenne de grandeur
        """
        total = 0

        for personnage in self.lst_perso:
            total += personnage.size or 0

        moyenne = total / len(self.lst_perso)

        print(f"La grandeur moyenne est de {int(moyenne):} cm")

    #? fait
    def graph_boxplot_stats(self):

        forces = []
        pvs = []
        ages = []
        tailles = []
        for person in self.lst_perso:

            #todo calcul de la force réelle selon le type
            if isinstance(person, Marine):
                person.force = person.calcul_force_total()

            elif isinstance(person, Pirate):
                person.force = person.calcul_force_total()

            try:
                forces.append(int(person.force))

            except (ValueError, TypeError):
                continue


        
#!#######################################
            #todo calcul de la force réelle selon le type
            if isinstance(person, Marine):
                person.pv = person.calculer_pv()

            elif isinstance(person, Pirate):
                person.pv = person.calculer_pv()

            try:
                pvs.append(int(person.pv))

            except (ValueError, TypeError):
                continue
    
            try:
                forces.append(int(person.force))
                pvs.append(int(person.pv))
                ages.append(int(person.age))
                tailles.append(int(person.size))


            except (ValueError, TypeError, AttributeError):
                continue


        data = [
            forces,
            pvs,
            ages,
            tailles
        ]


        plt.figure(figsize=(10,6))

        plt.boxplot(data)

        plt.xticks(
            [1, 2, 3, 4],
            ["Force", "PV", "Âge", "Taille"]
        )

        plt.title("Distribution des statistiques des personnages")
        plt.ylabel("Valeurs")

        plt.grid()

        plt.show()