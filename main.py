
from gestionnaire import Gestionnaire
from equipage import Equipage
from marine import Marine
from pirate import Pirate
from personnage import Personnage
from fruit import Fruit
from arene import Arene

from statistiques import Statistiques


lst_membre : list[Personnage] = []

gestionnaire = Gestionnaire()
arene = Arene()
try :
    gestionnaire.charger_donnees()
    for x in gestionnaire.lst_equipage:
        print(x.nom)
        for perso in x.lst_membres:
            print(perso.nom)
except :
    gestionnaire.call_api()


for x in gestionnaire.lst_equipage:
    for perso in x.lst_membres:
        lst_membre.append(perso)

statistiques = Statistiques(gestionnaire.lst_equipage, lst_membre)

choix = 1000000
while choix != 0:
    choix = int(input("Quel est votre choix: "))
    match choix :
        case 1 :
            for equipage in gestionnaire.lst_equipage:
                tot = equipage.force_total_equipe()
                print(tot)
        case 2:
            statistiques.pie_vivant_mort_inconue()
        case 3:
            statistiques.nb_perso_range_prime()
        case 4:
            statistiques.force_en_fonction_age()
        case 5:
            arene.afficher_personnages()
            arene.combat()
        case 0:
            print("One piece est terminé")