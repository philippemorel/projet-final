    def combats(self, lst_perso: list):

        # calcul des pv
        for person in lst_perso:
            if isinstance(person, (Marine, Pirate)):
                person.pv = person.calculer_pv()

        # affichage des persos
        for i, perso in enumerate(lst_perso, start=1):
            print(f"{i}: {perso.nom}")

        personnage1 = None
        personnage2 = None

        nom1 = input("Nom du premier personnage : ")
        nom2 = input("Nom du deuxième personnage : ")

        # recherche
        for perso in lst_perso:
            if perso.nom == nom1:
                personnage1 = perso
            if perso.nom == nom2:
                personnage2 = perso

        if personnage1 is None or personnage2 is None:
            print("Un des personnages n'existe pas.")
            return

        # combat
        while personnage1.pv > 0 and personnage2.pv > 0:

            damage = personnage1.attaque()
            personnage2.pv -= damage
            print(f"{personnage2.nom} subit {damage} dégâts de {personnage1.nom}")

            if personnage2.pv <= 0:
                print(f"{personnage1.nom} a gagné !")
                break

            damage = personnage2.attaque()
            personnage1.pv -= damage
            print(f"{personnage1.nom} subit {damage} dégâts de {personnage2.nom}")

            if personnage1.pv <= 0:
                print(f"{personnage2.nom} a gagné !")
                break