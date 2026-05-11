from personnage import Personnage
from pirate import Pirate
from marine import Marine
import random
class Arene():


    def __init__(self):
        pass





    def choix_mouve(self, personnage : object):
        
        #todo si il a un fruit
        if personnage.use_fruit == True :
            choix = input("que voulez vous faire  (attaquer) (defendre) (regenerer) (attaque fruitée)")
            match choix :
                #todo attaque
                case 1 :

                    attaque = personnage.puissance


                    print(f"vous attaquer et avec attaque coup de point")
                    print(f"et faite 30 de degas")


    






    
    def __init__(self):
        
        self.lst_personnage : list[Personnage] = []




            



    def afficher_personnages(self):
        index = 0
        for personnage in self.lst_personnage:
            print(f"{index} - {personnage}")
            index += 1



    def combat (self):


        index_personnage1 = int(input("quel premier personnage voulez vous faire combatre : "))
        index_personnage2 = int(input("quel deuxieme personnage voulez vous faire combatre : "))

        personnage1 = self.lst_personnage[index_personnage1]
        personnage2 = self.lst_personnage[index_personnage2]

        nombre_tour = 0
        while personnage1.vie >= 0 and personnage2.vie >= 0 :
            
            #todo attaque du perso1
            damage = personnage1.attaquer()
            personnage2.pv -= damage
            print(f"le personnage {personnage2.nom} a subis {damage} degat de {personnage1.nom}")
            if personnage2.vie <= 0 :
                print(f"personnage {personnage1.nom} a gagner")
                break
            #todo attaque du perso2 
            damage = personnage2.attaquer()
            personnage1.subir_degat(damage)
            print(f"le personnage {personnage1.nom} a subis {damage} degat de {personnage2.nom}")

            if personnage1.vie <= 0 :
                print(f"personnage {personnage2.nom} a gagner")
                break

            nombre_tour += 1
            
    #todo nombre de personnage encore avec de la vie
    def __len__(self):
        compteur = 0
        for personnage in self.lst_personnage:
            if personnage.vie > 0:
                compteur += 1
        return compteur
    
    def nettoyage_arene(self):

        for personnage in self.lst_personnage :
            if personnage.vie <= 0 :
                self.lst_personnage.remove(personnage)



    def battle_royal(self):
        lst_verif : list[Personnage|Pirate|Marine]= []

        for personnage in self.lst_personnage :
            if personnage.vie > 0 :
                lst_verif.append(personnage)

        nombre_tour = 1                


        while len(lst_verif) > 1 :

            print(f" ____tour {nombre_tour}____")

            index_personnage1 = random.randint(0,len(lst_verif) - 1)
            index_personnage2 = random.randint(0,len(lst_verif) - 1)

            personnage1 = lst_verif[index_personnage1]
            personnage2 = lst_verif[index_personnage2]
                
            #todo attaque du perso1
            degat = personnage1.attaquer()
            personnage2.subir_degat(degat)
            print(f"le personnage {personnage2.nom} a subis {degat} degat de {personnage1.nom}")
            if personnage2.vie <= 0 :
                print(f"personnage {personnage1.nom} a gagner contre {personnage2.nom}")
                lst_verif.remove(personnage2)
            
            else :        
                #todo attaque du perso2 
                degat = personnage2.attaquer()
                personnage1.subir_degat(degat)
                print(f"le personnage {personnage1.nom} a subis {degat} degat de {personnage2.nom}")

            if personnage1.vie <= 0 :
                print(f"personnage {personnage2.nom} a gagner contre {personnage1.nom}")
                lst_verif.remove(personnage1)
            nombre_tour += 1






                        




                    




                    