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
            
        

        import matplotlib.pyplot as plt

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

    def tri_rapide(lst_perso: list[Personnage], element_a_trier):

        lst_tri = lst_perso.copy()

        #todo si la liste est vide ou ne contient qu'un élément:
        #todoelle est triée, on revoie directement la liste
        if len(lst_tri) <= 1:
            return lst_tri
            
        pivot = lst_tri[len(lst_tri)-1]  #todo pivot=dernier élément

        petits = []
        grands = []

        for i in range(len(lst_tri)-1):  #todo on parcourt tous les éléments sauf le pivot
            if lst_tri[i].element_a_trier < pivot:
                petits.append(lst_tri[i])  #todo on ajoute les éléments plus petits que le pivot à la liste "petits"
            else:
                grands.append(lst_tri[i])  #todo on ajoute les éléments plus grands ou égaux au pivot à la liste "grands"
            
        #todo Magie : on appelle la fonction tri rapide avec la liste des petits et des grands
        #todoensuite on combine le résultat des listes triées avec le pivot pour obtenir la liste triée finale
        return Statistiques.tri_rapide(petits) + [pivot] + Statistiques.tri_rapide(grands)
    #? fait
    def top_10_age(self):
    
        lst_tri = Statistiques.tri_rapide("age")
        nb_element = len(lst_tri)
        lst_top_10 = []
        for x in range(10):
            lst_top_10.append(lst_tri[nb_element])
            top_10 = lst_top_10.pop()
            print(top_10)
    #? fait
    def top_10_size(self):
    
        lst_tri = Statistiques.tri_rapide("size")
        nb_element = len(lst_tri)
        lst_top_10 = []
        for x in range(10):
            lst_top_10.append(lst_tri[nb_element])
            top_10 = lst_top_10.pop()
            print(top_10)
    #? fait
    def moyenne_age(self):
        ano = 0
        for x in self.lst_perso:
            ano += x.age
        ano / len(self.lst_perso)
        print(f"L'âge moyenne est de {ano}")
    #? fait
    def moyenne_size(self):
        sizo = 0
        for x in self.lst_perso:
            sizo += x.size
        sizo / len(self.lst_perso)
        print(f"La grandeur moyenne est de {sizo}")
  


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