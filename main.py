
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

        
def afficher_perso():
    for x in gestionnaire.lst_equipage:
        for perso in x.lst_membres:
            lst_membre.append(perso)

statistiques = Statistiques(gestionnaire.lst_equipage, lst_membre)
arene = Arene(gestionnaire.lst_equipage, lst_membre)

choix = 1000000
while choix != 0:
    print("""
    ╔══════════════════════════════════════════════╗
    ║          GRAND LINE - MENU PIRATE            ║
    ╠══════════════════════════════════════════════╣
    ║  1    Voir la puissance des équipages        ║ 
    ║  2    Statistiques vivants / morts           ║
    ║  3    Voir les primes des personnages        ║
    ║  4    Force en fonction de l'âge             ║
    ║  5    Lancer un combat dans l'arène          ║
    ║  6    Afficher les boxplots des stats        ║
    ║  7    combat de ffa                          ║
    ║  0    Quitter le monde de One Piece          ║
    ╚══════════════════════════════════════════════╝
    """)
    try:
        choix = int(input("Quel est votre choix: "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue
    match choix :
        case 1 :
            for equipage in gestionnaire.lst_equipage:
                tot = equipage.force_total_equipe()
                print(f"{tot} de puissance dans l'equipage {equipage.nom}")
        case 2:
            #? fait 
            print()
            print(" Génération des boxplots des statistiques...")
            statistiques.pie_vivant_mort_inconue()
        case 3:
            #? fait 
            print()
            print(" Génération des boxplots des statistiques...")
            statistiques.nb_perso_range_prime()
        case 4:
            #? fait 
            print()
            print(" Génération des boxplots des statistiques...")
            statistiques.force_en_fonction_age()
        
        case 5:
            print("══════ ARÈNE DES PIRATES ══════")
            print("═════════combat de 1v1═════════")
            arene.combat(lst_membre)
            print()
            print(" Fin du combat du Nouveau Monde!")
        case 6 :
            print()
            print(" Génération des boxplots des statistiques...")
            statistiques.graph_boxplot_stats()
        case 7 : 
            print("══════ ARÈNE DES PIRATES ══════")
            print("════════ combat de ffa ════════")  
            arene.battle_royal()
            arene.nettoyage_arene()
        #? les top
        case 8:
            #? fait
            statistiques.top_10_age()
        case 9:
            #? fait
            statistiques.top_10_size()

        #? les moyenne
        case 10:
            #? fait
            statistiques.moyenne_age()
        case 11:
            #? fait
            statistiques.moyenne_size()
        case 0:

            print("""
            ╔══════════════════════════════╗
            ║    One Piece est terminé     ║
            ║      Merci capitaine         ║
            ╚══════════════════════════════╝
            """)
