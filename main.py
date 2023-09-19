# back end combat de monstres
# Romain Cavalieri-Bélanger, sept 2023

import random


# structure de data des Entity sous forme de classe
class Entity():

    def __init__(self, force, nom):
        self.nom = nom
        self.force = int(force)


############  add une boucle qui tourne tant que 1 des 2 est mort
    def combat(self, adversaire, victoire):
        if self.force > adversaire.force:
            self.vie += adversaire.force
            victoire += 1
            print("""

              Combat Gagné!!

              Niveau de vie : """, player.vie, """
              Nombre de victoires consécutives : """, victoire, """

          """)

        elif self.force == adversaire.force:
            print("c'est égalité")

        else:
            print(adversaire.nom, "à gagné...")
            self.vie -= adversaire.force


class Living_entity(Entity):
    def __init__(self, force, nom, vie):
        super().__init__(force, nom)
        self.vie = vie

    def combat(self, adversaire, victoire):
        if self.force > adversaire.force:
            self.vie += adversaire.force
            victoire += 1
            print("""
            
              Combat Gagné!!

              Niveau de vie : """, player.vie, """
              Nombre de victoires consécutives : """, victoire, """

          """)

        elif self.force == adversaire.force:
            print("c'est égalité")
            adversaire.vie -= adversaire.force
        else:
            print(adversaire.nom, "à gagné...")
            self.vie -= adversaire.force


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

while alive:
    boss = Living_entity(random.randint(0, 10), monstreNom[random.randint(0, 6)], 5)

    print("Vous tombez face à face avec un adversaire de difficulté : ", boss.force)
    choix = int(input("""

  Que voulez-vous faire ? 
	1- Combattre cet adversaire
	2- Contourner cet adversaire et aller ouvrir une autre porte
	3- Afficher les règles du jeu
	4- Quitter la partie

"""))
    if choix == 1:
        player.force = random.randint(0, 10)
        print("""

    Adversaire : """, boss.nom, """
    Force de l’adversaire : """, boss.force, """
    Niveau de vie de l’usager : """, player.vie, """
    Combat numero_combat : nombre victoire X

    lancé du dé : """, player.force, """
    """)
        player.combat(boss, 6)

    elif choix == 2:
        player.vie -= 1
    elif choix == 3:
        print(regleJeux)
    elif choix == 4:
        print("fin de partie, vous avez accumulé X victoire")

    if player.vie <= 0:
        print("game over")
        alive = False








