from personnage import Personnage
from pirate import Pirate
from marine import Marine
from equipage import Equipage
import random
class Arene():


    def __init__(self, lst_equipage , lst_perso):
        self.lst_equipage : list[Equipage] = lst_equipage
        self.lst_perso : list[Personnage] = lst_perso




    def choix_move(self, personnage):

        print(f"Tour de {personnage.nom}")

        # Si le personnage possède un fruit
        if personnage.use_fruit:

            choix = input(
                "Que voulez-vous faire ?\n"
                "1 - Attaque normale\n"
                "2 - Défense\n"
                "3 - Régénération\n"
                "4 - Attaque fruitée\n"
            )
        #! Si il n'en possède pas
        else:

            choix = input(
                "Que voulez-vous faire ?\n"
                "1 - Attaque normale\n"
                "2 - Défense\n"
                "3 - Régénération\n"
            )

        match choix:
            
            # Attaque normale
            case "1":

                damage = personnage.attaque()

                print(f"{personnage.nom} utilise une attaque normale")
                print(f"Dégâts infligés : {damage}")

                return int(damage)

            # Défense
            case "2":

                print(f"{personnage.nom} se met en position défensive")

                return "defense"

            # Régénération
            case "3":

                ancien_pv = personnage.pv
                pv_apres = personnage.regen()

                print(f"{personnage.nom} se régénère")
                print(f"PV avant : {ancien_pv}")
                print(f"PV après : {pv_apres}")
                
                return 0

            # Attaque fruitée
            case "4":

                if personnage.use_fruit:

                    damage = personnage.attaque_fruite()

                    print(f"{personnage.nom} utilise son fruit du démon !")
                    print(f"Dégâts infligés : {damage}")

                    return int(damage)

                else:

                    print("Ce personnage ne possède pas de fruit")

                    return 0

            case _:

                print("Choix invalide")

                return 0

    def combat(self, lst_perso: list):

        # Calcul des PV
        for person in lst_perso:

            if isinstance(person, (Marine, Pirate)):
                person.pv = person.calculer_pv()
                person.pv_max = person.pv

        #todo Affichage des personnages
        print("\n===== LISTE DES PERSONNAGES =====")

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

            if perso.nom == nom2:
                personnage2 = perso

        #todo Vérification
        if personnage1 is None or personnage2 is None:
            print("Un des personnages n'existe pas.")
            return

        nombre_tour = 1

        #todo Combat
        while personnage1.pv > 0 and personnage2.pv > 0:

            print(f"\n========== TOUR {nombre_tour} ==========")

            #? =========================
            #? TOUR DU PERSONNAGE 1
            #? =========================

            action1 = self.choix_move(personnage1)

            # Défense
            if action1 == "defense":

                print(f"{personnage1.nom} est prêt à bloquer la prochaine attaque")

                defense1 = True

            else:

                defense1 = False

                if isinstance(action1, (int,float)):
                    
                    personnage2.pv -= action1

                    print(f"{personnage2.nom} subit {action1} dégâts")
                    print(f"PV restants : {personnage2.pv}")

            # Vérification victoire
            if personnage2.pv <= 0:

                print(f"{personnage1.nom} a gagné le combat !")
                break

            #? =========================
            #? TOUR DU PERSONNAGE 2
            #? =========================

            action2 = self.choix_move(personnage2)

            # Défense
            if action2 == "defense":

                print(f"{personnage2.nom} est prêt à bloquer la prochaine attaque")

                defense2 = True

            else:

                defense2 = False

                if isinstance(action2, (int,float)):

                    # Si personnage1 défend
                    if defense1:
                        
                        degats_reduits = personnage1.defense(action2)

                        print(f"{personnage1.nom} bloque une partie des dégâts !")
                    
                    personnage1.pv -= degats_reduits

                    print(f"{personnage1.nom} subit {action2} dégâts")
                    print(f"PV restants : {personnage1.pv}")

            # Vérification victoire
            if personnage1.pv <= 0:

                print(f"\n{personnage2.nom} a gagné le combat !")
                break

            nombre_tour += 1
            
    def __len__(self):
        compteur = 0
        for personnage in self.lst_personnage:
            if personnage.pv > 0:
                compteur += 1
        return compteur
    
    def nettoyage_arene(self):

        for personnage in self.lst_perso :
            if personnage.pv <= 0 :
                self.lst_perso.remove(personnage)



    def battle_royal(self):
        lst_verif : list[Personnage|Pirate|Marine]= []

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

        print(f"\nLe gagnant est {lst_verif[0].nom}")





                            




                        




                        