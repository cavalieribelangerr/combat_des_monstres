# back end combat de monstres
# Romain Cavalieri-Bélanger, sept 2023

import random


# structure de data des Entity sous forme de classe
class Entity():

    def __init__(self, force, nom):
        self.nom = nom
        self.force = int(force)


    def combat(self, adversaire, nb_victoire):
        winner = 0
        if self.force > adversaire.force:
            self.vie += adversaire.force
            print("""

              Combat Gagné!!

              Niveau de vie : """, player.vie, """
              Nombre de victoires consécutives : """, nb_victoire, """

          """)
            winner = 1

        elif self.force == adversaire.force:
            print("c'est égalité")
            winner = 0

        else:
            print(adversaire.nom, "à gagné...")
            self.vie -= adversaire.force
            winner = 0

        return winner

class Living_entity(Entity):
    def __init__(self, force, nom, vie):
        super().__init__(force, nom)
        self.vie = vie

    def combat_boss(self, adversaire):

        if self.force > adversaire.force:
            self.vie += adversaire.force
            print("""
            
              Combat Gagné!!

              Niveau de vie : """, player.vie, """
              Nombre de victoires consécutives : """, nb_victoire, """

          """)


        elif self.force == adversaire.force:
            print("c'est égalité")
            adversaire.vie -= adversaire.force


        else:
            print(adversaire.nom, "à gagné...")
            self.vie -= adversaire.force
        if adversaire.vie <= 0:
            return 1
        elif self.vie <= 0:
            return 0
        else:
            return 2


# création des entity
# les monstres
monstreNom = ["bigBrother", "Gandalf", "Dani", "Boba", "Golum", "Jack", "iShowSpeed"]
player = Living_entity(5, 'player', 20)
alive = True
regleJeux = ("""


voici les regles: 
Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de 
l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.
Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force 
de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.


La partie se termine lorsque les points de vie de l’usager tombent sous 0.


L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, 
il y a une pénalité de 1 point de vie.


""")


fight_boss = False
nb_victoire = 0

while alive:
    player.force = random.randint(0, 20)
    boss = Living_entity(random.randint(0, 10), monstreNom[random.randint(0, 6)], random.randint(0, 10))
    mob = Entity(random.randint(0, 5), monstreNom[random.randint(0, 6)])



    print("Vous tombez face à face avec un adversaire de difficulté : ", boss.force)
    choix = int(input("""

  Que voulez-vous faire ? 
	1- Combattre cet adversaire
	2- Contourner cet adversaire et aller ouvrir une autre porte
	3- Afficher les règles du jeu
	4- Quitter la partie

"""))

    if choix == 1:

        print("""

    Adversaire : """, mob.nom, """
    Force de l’adversaire : """, mob.force, """
    Niveau de vie de l’usager : """, player.vie, """
    Combat numero_combat : """, nb_victoire, """

    lancé du dé : """, player.force, """
    
    """)
        m = player.combat(mob, nb_victoire)
        if m == 0:
            nb_victoire = 0
        else:
            print('add')
            print(nb_victoire)
            nb_victoire += 1

    elif choix == 2:
        player.vie -= 1
    elif choix == 3:
        print(regleJeux)
    elif choix == 4:
        print("fin de partie, vous avez accumulé ", nb_victoire ," victoire")


    if nb_victoire == 3:
        print("vous allez affronter un BOSS")
        fight_boss = True

        while fight_boss:
            player.combat_boss(boss)
            if player.combat_boss(boss) == 1:
                nb_victoire += 3
                player.vie += 2*boss.vie
                print("""

                    Combat Gagné contre le Boss!!

                    Niveau de vie : """, player.vie, """
                    Nombre de victoires consécutives (bonus boss) : """, nb_victoire, """

                """)
                fight_boss = False
            elif player.combat_boss(boss) == 0:
                fight_boss = False
            elif player.combat_boss(boss) == 2:
                fight_boss = True



    if player.vie <= 0:
        print("game over")
        alive = False








