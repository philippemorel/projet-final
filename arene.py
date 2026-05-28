from personnage import Personnage
from pirate import Pirate
from marine import Marine
from equipage import Equipage
import random
import copy
class Arene():


    def __init__(self, lst_equipage , lst_perso):
        self.lst_equipage : list[Equipage] = lst_equipage
        self.lst_perso : list[Personnage] = lst_perso




    def choix_move(self, personnage : object):
        """Méthode pour choisir quel mouve entre attaque, défense, regen et attaque fruité va faire le perso en question

        """
        


        print(f"Tour de {personnage.nom}")

        #todo Si le personnage possède un fruit
        if personnage.use_fruit:

            choix = input(
                "Que voulez-vous faire ?-------"

                "1 - Attaque normale--------"

                "2 - Défense---------"

                "3 - Régénération--------"

                "4 - Attaque fruitée--------"
            )
        #todo Si le perso ne possède pas de fruit
        else:

            choix = input(
                "Que voulez-vous faire ?--------"

                "1 - Attaque normale-------"

                "2 - Défense--------"
                
                "3 - Régénération-------"
            )
        #todo les possibiliter de choix
        match choix:
            
            #todo Attaque normale
            case "1":

                damage = personnage.attaque()

                print(f"{personnage.nom} utilise une attaque normale")
                print(f"Dégâts infligés : {damage}")

                return float(damage)

            #todo Défense
            case "2":

                print(f"{personnage.nom} se met en position défensive")

                return "defense"

            #todo Régénération
            case "3":
                """
                ancien_pv = personnage.pv
                pv_apres = personnage.regen()

                print(f"{personnage.nom} se régénère")
                print(f"PV avant : {ancien_pv}")
                print(f"PV après : {pv_apres}")
                """
                return "regen"

            #todo Attaque fruitée
            case "4":

                if personnage.use_fruit:

                    damage = personnage.attaque_fruite()

                    print(f"{personnage.nom} utilise son fruit du démon !")
                    print(f"Dégâts infligés : {damage}")

                    return int(damage)
                #todo protection pour si erreur tres special
                else:

                    print("Ce personnage ne possède pas de fruit")

                    return 1

            case _:

                print("Choix invalide")

                return 1
    #? la force et le pv ne sont pas actualiser 
    #? et ne rentre pas dans la boucle du combat ses comme si il n'a pas de pv
    defense1 = False 
    defense2 = False 
    def combat(self, lst_perso: list):

        #todo Calcul des PV
        for person in lst_perso:

            if isinstance(person, (Marine, Pirate)):
                force_total = person.calcul_force_total()

            person.pv = person.calculer_pv()

        #todo Affichage des personnages
        print("===== LISTE DES PERSONNAGES =====")

        for perso in lst_perso:
            print(f"- {perso.nom}")

        personnage1 = None
        personnage2 = None

        nom1 = input("Nom du premier personnage : ")
        nom2 = input("Nom du deuxième personnage : ")

        #todo Recherche des personnages
        for perso in lst_perso:

            if perso.nom == nom1:
                personnage1 = perso
                personnage1_nom = perso.nom
                personnage1_pv = perso.pv
                personnage1_force = perso.force
                teste = personnage1.calcul_force_total()
                print(f"la force de votre personage {personnage1_nom} est de {teste} ")
                
            if perso.nom == nom2:
                personnage2 = perso
                personnage2_nom = perso.nom
                personnage2_pv = perso.pv
                personnage2_force = perso.force
                teste_force_total = personnage2.calcul_force_total()
                print(f"la force de votre personage {personnage2_nom} est de {teste_force_total} ")

    
        #todo Vérification
        if personnage1_nom is None or personnage2_nom is None:
            print("Un des personnages n'existe pas.")
            return

        nombre_tour = 1
        defense2 = False
        defense1 = False
        #todo Combat
        while personnage1.pv > 0 and personnage2.pv > 0:

            print(f"========== TOUR {nombre_tour} ==========")

            #? =========================
            #? TOUR DU PERSONNAGE 1
            #? =========================

            action1 = self.choix_move(personnage1)

            action2 = self.choix_move(personnage2)

            #?###############################
            #? section dess attaque
            #?###############################
            #todo action si le perso 1 attaque
            if isinstance(action1, float):
                #todo si le perso 2 as defendue
                if action2 == "defense":
                    print(f"{personnage2.nom} est prêt à bloquer la prochaine attaque")
                                    
                    degats_reduits = personnage2.defense(action1)

                    personnage2.pv -= degats_reduits

                    print(f"{personnage2.nom} bloque une partie des dégâts !")
                    print(f"{personnage2.nom} subit {degats_reduits} dégâts")
                    print(f"PV restants : {personnage2.pv}")

                #todo si le perso 2 ne defend pas
                else :
                    print(f"le personage 1 fait {action1} domage a {personnage2.nom}")
                    personnage2.pv -= action1
                    print(f"le personnage {personnage2_nom} est rendu a {personnage2.pv} pv")
            #todo action si le perso 2 attaque
            if isinstance(action2, float):
                #todo si le perso 1 as defendue
                if action1 == "defense":
                    print(f"{personnage1.nom} est prêt à bloquer la prochaine attaque")
                                    
                    degats_reduits = personnage1.defense(action1)

                    personnage1.pv -= degats_reduits

                    print(f"{personnage1.nom} bloque une partie des dégâts !")
                    print(f"{personnage1.nom} subit {degats_reduits} dégâts")
                    print(f"PV restants : {personnage1.pv}")

                #todo si le perso 1 ne defend pas    
                else :
                    print(f"le personage {personnage2.nom} fait {action2} domage a {personnage1.nom}")
                    personnage1.pv -= action2
                    print(f"le personnage {personnage1.nom} est rendu a {personnage1.pv} pv")
               
            #?###############################
            #? section des regen
            #?###############################
            #todo si le perso 1 regen
            if action1 == "regen":
                print(f"le personage {personnage1_nom} regen")
                print(f"le personage {personnage1_nom} a {personnage1.pv} pv avant la regen")
                print()
                personnage1.regen()
                print(f"le personage {personnage1_nom} a {personnage1.pv} pv apres la regen")

            #todo si le perso 2 regen
            if action2 == "regen":
                print(f"le personage {personnage2_nom} regen")
                print(f"le personage {personnage2_nom} a {personnage2.pv} pv avant la regen")
                print()
                personnage2.regen()
                print(f"le personage {personnage2_nom} a {personnage2.pv} pv apres la regen")

            #todo Vérification victoire
            if personnage2.pv <= 0:
                print(f"{personnage1.nom} a gagné le combat !")
                break
            #todo Vérification victoire
            if personnage1.pv <= 0:

                print(f"{personnage2.nom} a gagné le combat !")
                break

            nombre_tour += 1
            
    def __len__(self):
        compteur = 0
        for personnage in self.lst_personnage:
            if personnage.pv > 0:
                compteur += 1
        return compteur
    




    def battle_royal(self):
        """permet de faire combatre tout le monde et savoir le dernier survivant

        """
        #todo deepcopy permet de copier tout l'objet
        lst_verif = copy.deepcopy(self.lst_perso)

        #todo Reset des PV
        for personnage in self.lst_perso:
            personnage.pv = personnage.calculer_pv()

        for personnage in self.lst_perso :
            if personnage.pv > 0 :
                lst_verif.append(personnage)

        nombre_tour = 1                

        while len(lst_verif) > 1 :

            print(f" ____tour {nombre_tour}____")

            index_personnage1 = random.randint(0,len(lst_verif) - 1)
            index_personnage2 = random.randint(0,len(lst_verif) - 1)

            while index_personnage1 == index_personnage2:
                index_personnage2 = random.randint(0, len(lst_verif) - 1)

            personnage1 = lst_verif[index_personnage1]
            personnage2 = lst_verif[index_personnage2]
                    
            #todo attaque du perso1
            degat = personnage1.attaque()
            personnage2.pv -= degat

            print(f"le personnage {personnage2.nom} a subis {degat} degat de {personnage1.nom}")

            if personnage2.pv <= 0 :

                print(f"personnage {personnage1.nom} a gagner contre {personnage2.nom}")

                lst_verif.remove(personnage2)
                
            else :

                #todo attaque du perso2 
                degat = personnage2.attaque()
                personnage1.pv -= degat

                print(f"le personnage {personnage1.nom} a subis {degat} degat de {personnage2.nom}")

            if personnage1.pv <= 0 :

                print(f"personnage {personnage2.nom} a gagner contre {personnage1.nom}")

                lst_verif.remove(personnage1)

            nombre_tour += 1

        print(f"Le gagnant est {lst_verif[0].nom}")





                            




                        




                        