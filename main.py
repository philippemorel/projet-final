
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
╔══════════════════════════════════════════════════════════╗
║                   GRAND LINE - MENU PIRATE               ║
╠══════════════════════════════════════════════════════════╣
║  1  │ Voir la puissance des équipages                    ║
║  2  │ Statistiques vivants / morts                       ║
║  3  │ Voir les primes des personnages                    ║
║  4  │ Force en fonction de l'âge                         ║
║  5  │ le plus grand et le plus petit                     ║
║  6  │ Afficher les boxplots des stats                    ║
║  7  │ Combat de FFA                                      ║
║  8  │ Top 10 âge                                         ║
║  9  │ Top 10 taille                                      ║
║ 10  │ Moyenne âge                                        ║
║ 11  │ Moyenne taille                                     ║
║  0  │ Quitter le monde de One Piece                      ║
╚══════════════════════════════════════════════════════════╝
""")

    try:
        choix = int(input(" Quel est votre choix : "))
    except ValueError:
        print(" Veuillez entrer un nombre valide.")
        continue

    match choix:

        case 1:
            for equipage in gestionnaire.lst_equipage:
                tot = equipage.force_total_equipe()
                print(f" {tot} de puissance dans l'équipage {equipage.nom}")

        case 2:
            print(" Génération des statistiques...")
            statistiques.pie_vivant_mort_inconue()

        case 3:
            print(" Génération diagrame a bande des statistiques...")
            statistiques.nb_perso_range_prime()

        case 4:
            print(" Génération des statistiques force et âges...")
            statistiques.force_en_fonction_age()

        case 5:
            print(" Génération des statistiques du plus grand et du plus petit...")
            statistiques.premier_dernier_size()
            
        case 6:
        
            print(" Génération des boxplots des stats...")
            statistiques.graph_boxplot_stats()

        case 7:
            print("══════ ARÈNE DES PIRATES ══════")
            print("══════════ COMBAT FFA ══════════")
            arene.battle_royal()
            

        case 8:
            print(" TOP 10 - ÂGE")
            print("────────────────────────────")
            statistiques.top_10_age()

        case 9:
            print(" TOP 10 - TAILLE")
            print("────────────────────────────")
            statistiques.top_10_size()

        case 10:
            print(" MOYENNE D'ÂGE")
            print("────────────────────────────")
            statistiques.moyenne_age()

        case 11:
            print(" MOYENNE DE TAILLE")
            print("────────────────────────────")
            statistiques.moyenne_size()

        case 0:
            print("""
                ╔══════════════════════════════════════╗
                ║      ONE PIECE EST TERMINÉ           ║
                ║        Merci capitaine               ║
                ╚══════════════════════════════════════╝
                """)
