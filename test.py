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
        



#!#############################################################



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

        print(f"Le gagnant est {lst_verif[0].nom}")



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

        lst_tri = Statistiques.tri_rapide(self.lst_perso, "age")

        # du plus vieux au plus jeune
        top_10 = lst_tri[-10:]

        # affichage inversé pour avoir le plus grand âge en premier
        for personnage in reversed(top_10):
            print(personnage)
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
  

    #! marche pas si pas reparer supprimer
                print(" ══════ ARÈNE DES PIRATES ══════")
                print("══════════ COMBAT 1v1 ══════════")
                arene.combat(lst_membre)
                print(" Fin du combat du Nouveau Monde!")
