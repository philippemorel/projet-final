import json
from personnage import Personnage
from equipage import Equipage
from pirate import Pirate
from marine import Marine
import requests
from fruit import Fruit
import re
class Gestionnaire():

    def __init__(self):
        self.lst_equipage : list[Equipage] = []

    def call_api(self)-> None :
        """Méthode pour calculer le total de dégat moins le nombre de dégat bloqué
        """
        url = f"https://api.api-onepiece.com/v2/characters/en/"

        response = requests.get(url)
        size = 0
        age = 0 
        if response.status_code == 200:
            data = response.json()

            for personnage in data:
                #todo age
                age_str = personnage.get("age")
                if age_str:
                    nombre = re.findall(r"\d+", age_str)
                    if nombre:
                        age = int("".join(nombre))
                    else:
                        age = None
                else:
                    age = None
                #todo size
                size_str = personnage.get("size")
                if size_str:
                    nombre = re.findall(r"\d+", size_str)
                    if nombre:
                        size = int("".join(nombre))
                    else:
                        size = None
                else:
                    size = None
                

                fruit=personnage.get("fruit")
                if fruit:
                    use_fruit = True
                    fruit = personnage["fruit"]
                    new_fruit = Fruit(fruit["name"],fruit["type"])

                else :
                    use_fruit = False
                #todo bounty
                bounty_str = personnage.get("bounty")
                if bounty_str:
                    nombre = re.findall(r"\d+", bounty_str)
                    if nombre:
                        bounty = int("".join(nombre))
                    else:
                        bounty = None
                else:
                    bounty = None
                if bounty:
                    perso = Pirate(
                    nom= personnage.get("name"),
                    job=personnage.get("job"),
                    age=age,
                    size=size,
                    use_fruit=use_fruit,
                    fruit=new_fruit,
                    vivant=personnage.get("status"),
                    prime=bounty
                
                    ) 
                else :
                    perso = Marine(
                    nom=personnage.get("name"),
                    job=personnage.get("job"),
                    age=age,
                    size=size,
                    use_fruit=use_fruit,
                    vivant=personnage.get("status"),
                    fruit=new_fruit
                    )

                equipage_dico = personnage.get("crew")

                if equipage_dico:
                    new_equipage = Equipage(equipage_dico["name"],equipage_dico["is_yonko"])
                    self.ajouter_equipage_et_perso(new_equipage, perso)
                else:
                    new_equipage = Equipage("autre",False)
                    self.ajouter_equipage_et_perso(new_equipage, perso)

        self.sauvegarde_perso()


    def ajouter_equipage_et_perso(self, equipage_to_add : Equipage, personnage : Personnage) :
        """Méthode pour créer la liste des équipages et des membres

        Args:
            equipage_to_add (Equipage): Les équipages
            personnage (Personnage): Les membres
        """
        if equipage_to_add not in self.lst_equipage:
            self.lst_equipage.append(equipage_to_add)

        for equipage in self.lst_equipage:
            if equipage == equipage_to_add:
                equipage.lst_membres.append(personnage)
                
    

    def sauvegarde_perso(self) -> None :
        """Méthode pour sauvegarder la liste des équipages et leurs membres dans un json
        """
        equpage_dico = []

        for equipage in self.lst_equipage:
            equpage_dico.append(equipage.to_dict())

        with open("sauvegarde_perso.json", "w", encoding="utf-8") as fichier:
            json.dump(equpage_dico, fichier, indent=4, ensure_ascii=False)
        print("sauvegarde terminer")
        self.charger_donnees()


    def charger_donnees(self) :
        """Méthode pour charger le json contenant les équipages et leurs membres
        """
        with open("sauvegarde_perso.json", "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)
            
            for dico in donnees:
                equipage = Equipage(
                    #todo equipage
                    dico["nom"],
                    dico["yonko"]
                    )
                

                for membre in dico["membres"]:

                    fruit = membre["fruit"] 
                    if fruit == True :
                        Fruit(
                        fruit["nom_fruit"],
                        fruit["fruit_type"]
                        )

                
                    perso = None

                    if "prime" in membre:
                        perso = Pirate(
                        #todo le perso
                        membre["nom"],
                        membre["job"],
                        membre["age"],
                        membre["size"],
                        membre["use_fruit"],
                        fruit,
                        membre["vivant"],
                        membre["prime"]
                        )
                    else:
                        perso = Marine(
                        #todo le perso
                        membre["nom"],
                        membre["job"],
                        membre["age"],
                        membre["size"],
                        membre["use_fruit"],
                        fruit,
                        membre["vivant"]
                        )

                    equipage.lst_membres.append(perso)
                    
                self.lst_equipage.append(equipage)
