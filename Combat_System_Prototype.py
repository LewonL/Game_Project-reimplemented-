import random
import time


#  ----- all Characters + unique -----
class Entity:
    def __init__(self, name, health, attack1, attack2, attack3, description):
        """
        Initial function, functions and other classes use these attributes.
        All entity classes have these things in common
        @type name: str
        @type health: int
        @type attack1: int
        @type attack2: int
        @type attack3: int
        @type description: str
        @rtype: None
        >> enemy2 = Entity(name="Zomb-E", health=10, attack1=5, attack2=5, attack3=5, description="A basic enemy")
        Zombie:
        name = Zombie
        health = 10
        attack = 5
        description: a basic enemy
        >> enemy3 = Entity(name=Undead dead, health=10, attack1=5, attack2=5, attack3=5, description="A basic enemy")
        ERROR (name should be in "___", because it is in str
        """
        self.name = name
        self.health = health
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.description = description

    def receive_damage(self, damage):
        """
        The damage being inflicted by attack, this function will not be used directly, but by attack functions only
        @type self: Entity
        @type damage: var
        @rtype: None
        >> self.attack = 3
        >> enemy1.receive_damage(self.attack)
        enemy1 received 3 atk damage
        >> self.attack = 4
        >> enemy2.receive_damag(self.attack)
        ERROR (typo in 'receive damag', therefore function cannot be called)
        """
        self.health -= damage

    def receive_heal_ability(self, gain_health):
        """
        All entities have this function, but only the Player class uses it.
        @type self: Entity
        @type gain_health: var
        @rtype: None
        >> self.attack = 3
        >> player1.receive_heal_ability(self.heal)
        enemy1 received 3 atk damage
        >> self.attack = 4
        >> enemy2.receive_hea_ability(self.heal)
        ERROR (typo in 'receive hea ability', therefore function cannot be called)
        """
        self.health += gain_health


# ----- enemy class -----
class Enemy(Entity):
    def __init__(self, name, health, attack1, attack2, attack3, description, attack4, attack5):
        """
        This class is the class for all enemies. This is an initial function that adds attributes in its own class from
        a pre-existing class called 'Entity'. Of which are 'attack4' and 'attack5'.
        @type attack4: int
        @type attack5: int
        @rtype: None
        >> Enemy7 = Entity(name="Big Boy Bob", health=70, attack=10, attack2=12, attack3=15, attack4=1, attack5=20,
        description="A complex class enemy")
        Big Boy Bob:
        name = Big Boy Bo
        health = 70hp
        attack = 10, 12, 15, 1, 20 atk
        Description = A complex class enemy.
        >> Enemy5 = Entity(name=Big Bob, health=40, attack=8, attack2=10, attack3=17, description=A complex class enemy)
        ERROR (name and description should be 'type: str')
        """
        Entity.__init__(self, name, health, attack1, attack2, attack3, description)
        self.attack4 = attack4
        self.attack5 = attack5

    def enemy_attack(self, Character):
        """
        Randomly plays out a series of attacks that can be done. Meaning that when the enemy attacks, the damage that
        is done may be different.
        @type self: Enemy
        @type Character: var
        @rtype: str, int
        >> self.attack = 4
        >> self.attack2 = 8
        >> self.attack3 = 9
        >> self.attack4 = 12
        >> self.attack5 = 14
        >> enemy7.attack_random_complex(player)
        enemy7 dealt 4/8/9/12/14 attack of damage onto the player
        or
        missed...
        >> self.attack = 4
        >> self.attack2 = 2
        >> self.attack3 = 7
        >> self.attack4 = 1
        >> self.attack5 = 14
        >> enemy7_attack_random_complex(player)
        ERROR (enemy5<_>attack_random_complex(player) '<>', this should be a '.')
        """
        print("The enemy attacks:")
        time.sleep(1)
        if random.randint(1, 15) == 1:
            print("The attack does a total damage of:", self.attack5)
            Character.receive_damage(self.attack5)
            time.sleep(1)
            print("Player_Health:", p.health)
        elif random.randint(1, 7) == 1:
            print("The attack does a total damage of:", self.attack4)
            Character.receive_damage(self.attack4)
            time.sleep(1)
            print("Player_Health:", p.health)
        elif random.randint(1, 5) == 1:
            print("The attack does a total damage of:", self.attack3)
            Character.receive_damage(self.attack3)
            time.sleep(1)
            print("Player_Health:", p.health)
        elif random.randint(1, 4) == 1:
            print("The attack does a total damage of:", self.attack2)
            Character.receive_damage(self.attack2)
            time.sleep(1)
            print("Player_Health:", p.health)
        elif random.randint(1, 2) == 1:
            print("The attack does a total damage of:", self.attack1)
            Character.receive_damage(self.attack1)
            time.sleep(1)
            print("Player_Health:", p.health)
        else:
            print("The attack missed...")
            time.sleep(1)
            print("Player_Health:", p.health)


#  ----- enemies -----
enemy1 = Enemy(name="Zombie", health=15, attack1=10, attack2=10, attack3=10, attack4=10,
                      attack5=10, description="A basic enemy")
enemy2 = Enemy(name="Skeleton", health=20, attack1=8, attack2=8, attack3=8, attack4=8,
                      attack5=8, description="A basic enemy")
enemy3 = Enemy(name="Ghost", health=25, attack1=15, attack2=15, attack3=15, attack4=15,
                      attack5=15, description="A basic enemy")
enemy4 = Enemy(name="Blind Man", health=30, attack1=5, attack2=8, attack3=10, attack4=12,
                      attack5= 15, description="A complex enemy")
enemy5 = Enemy(name="Jeffrey", health=40, attack1=3, attack2=4, attack3=14, attack4=15,
                      attack5=18, description="A complex enemy")
enemy6 = Enemy(name="Tall Ghost", health=45, attack1=2, attack2=10, attack3=12, attack4=30,
                      attack5=32, description="A complex enemy")
enemy7 = Enemy(name="Tiger's Eye", health=30, attack1=15, attack2=2, attack3=15, attack4=2,
                      attack5=40, description="A complex enemy")
enemy8 = Enemy(name="Memento Mori", health=100, attack1=6, attack2=9, attack3=12, attack4=4,
                      attack5=30, description="A complex enemy")
enemy9 = Enemy(name="AlphaGhost", health=80, attack1=12, attack2=8, attack3=16, attack4=14,
                      attack5=1, description="A complex enemy")


#  ----- player class -----
class Player(Entity):
    def __init__(self, name, health, attack1, attack2, attack3, description, player_heal, player_instant_death):
        """
         This is an initial function that adds attributes in its own class from a pre-existing
         class called 'Entity'. Adds 'heal' attribute and 'instant_death' attribute
         @type self: Player
         @type attack2: int
         @type attack3: int
         @rtype: None
         >> Player1 = Entity(name="Player_1", health=100, attack=8, attack2=20, attack3=30,
         description="The character you control")
         Player1. The character you control.
         --------
         health: 100hp
         attack: 8, 20, 30 atk
         >> Player2 = Entity(name=Big Bob, health=40, attack=8, attack2=10, attack3=17,
         description=The character you control)
         ERROR (name and description should be 'type: str')
         """
        Entity.__init__(self, name, health, attack1, attack2, attack3, description)
        self.player_heal = player_heal
        self.player_instant_death = player_instant_death

    def first_attack(self, Character):
        """
        The first and weakest attack the player can do
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.player_attack1 = 10
        >> player1.first_attack(enemy1)
        player1 dealt 10 attack of damage onto enemy1
        >> self.player_attack2 = 6
        >> player.first_attack(enemy1)
        ERROR (This function is for the first attack, calling 'first_attack' won't do anything because
        self.player_attack2 was defined, but not self.player_attack1)
        """
        print("You try your weak attack:")
        time.sleep(1)
        print("The attack did a total damage of:", self.attack1, "\n")
        Character.receive_damage(self.attack1)
        time.sleep(1)
        print("Enemy_Health:", e.health, "\n")

    def second_attack(self, Character):
        """
        For a second attack. Normal attack, 75% chance of success.
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.player_attack2 = 22
        >> player1.second_attack(enemy1)
        player1 dealt 22 attack of damage onto enemy1
        or
        you missed...
        >> self.player_first_attack = 6
        >> player1.player_second_attack(enemy1)
        ERROR (This function is for the second attack, calling 'player_second_attack' won't do anything
        because self.player_first_attack was defined, but not self.attack2)
        """
        print("You try your normal attack:")
        time.sleep(1)
        if random.randint(1, 4) == 1:
            print("You missed...")
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")
        else:
            print("The attack did a total damage of:", self.attack2)
            Character.receive_damage(self.attack2)
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")

    def third_attack(self, Character):
        """
        For a third attack. Strong attack, 33.33% chance of success.
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.attack3 = 30
        >> player1.third_attack(enemy4)
        player1 dealt 30 attack of damage onto enemy1
        or
        you missed...
        >> self.player_attack2 = 32
        >> player1.third_attack(enemy4)
        ERROR (This function is for the third attack, calling 'player_third_attack' won't do anything because
        self.player_attack2 was defined, but not self.player_attack3)
        """
        print("You try your strong attack:")
        time.sleep(1)
        if random.randint(1, 3) == 1:
            print("The attack did a total damage of:", self.attack3)
            Character.receive_damage(self.attack3)
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")
        else:
            print("You missed...")
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")

    def heal_attack(self, Character):
        """
        The player heals himself/herself, 25% chance of success
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.player_heal = 30
        >> player1.heal_attack(player1)
        Player1 healed 30 health
        >> self.player_heal = 20
        >> player1.heal_attack(enemy1)
        enemy1 healed 20 health (the point of the heal attack is to heal yourself, not the enemy)
        """
        print("You try to heal yourself:")
        time.sleep(1)
        if random.randint(1, 4) == 1:
            print("A total of", self.player_heal, "health had been healed")
            Character.receive_heal_ability(self.player_heal)
            time.sleep(1)
            print("Player_Health:", p.health, "\n")
        else:
            print("You were unable to heal")
            time.sleep(1)
            print("Player_Health:", p.health, "\n")

    def instant_death_attack(self, Character):
        """
        10% chance of success, instantly kills enemy
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.instant_death = 999999999999
        >> player1.instant_death_attack(enemy4)
        Player1 defeated enemy4
        or
        The attack failed
        >> self.attack3 = 23
        >> player1.instant_death_attack(enemy4)
        ERROR (This function is for the instant deaath attack, calling 'instant_death_attack'
        won't do anything because self.attack3 was
        defined, but not self.instant_death)
        """
        print("You try the instant death attack:")
        time.sleep(1)
        if random.randint(1, 10) == 1:
            print("The attack was a success")
            Character.receive_damage(self.player_instant_death)
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")
        else:
            print("The attack failed")
            time.sleep(1)
            print("Enemy_Health:", e.health, "\n")


#  ----- players -----
player1 = Player(name="Player.1", health=1000, attack1=10, attack2=15, attack3=40,
                 player_heal=30, player_instant_death=999999999999999, description="The Player you control")

players = [player1]
p = players.pop(0)


enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]

for i in range(len(enemies)):  # for loop so all enemies in the list must be played out before exiting the
    # enemy encounter
    e = enemies.pop(0)  # pop out the first enemy, then the next in the list
    print("You encounter an enemy...\n")
    time.sleep(0.7)  # time delay between code
    print("Name:", e.name, "\nHealth:", e.health, "\nAttacks:", e.attack1, e.attack2, e.attack3, e.attack4, e.attack5,
          "\nDescription:", e.description, "\n--------------------------")  # enemy descriptions and stats
    time.sleep(1)
    fight_or_flee = True
    fight_condition = True  # must be true for loops to work
    while fight_or_flee:  # will keep playing until a valid message is typed
        fight_or_flee_input = input("Would you like to fight or flee? (type 'fight' or 'flee): ")
        if fight_or_flee_input == 'fight':  # engage in battle
            time.sleep(0.2)
            print("You engage in battle with the", e.name)
            fight_or_flee = False
        elif fight_or_flee_input == 'flee':  # run away from enemy
            if random.randint(1, 3) == 1:
                time.sleep(0.2)
                print("You flee successfully...")
                fight_or_flee = False
                fight_condition = False  # leave battle entirely, you don't have to fight
            else:
                time.sleep(0.2)  # you failed to flee, and receive damage as a punishment
                print("You were unable to flee...\n")
                fight_or_flee = False
                e.enemy_attack(p)
        else:
            time.sleep(0.2)  # the reason why there is a while loop in the first place
            print("Unknown command... Try again.\n")

    while fight_condition:  # while loop for the actual combat
        time.sleep(1)
        if p.health < 1:  # if you die, entire game shuts down
            print("\nYou died...")
            raise SystemExit
        elif e.health < 1:  # if enemy dies, combat stops
            print("\nYou have successfully defeated the", e.name)
            fight_condition = False
        else:  # list of attacks you can do
            print("\nName:", p.name, "\nHealth:", p.health, "\nWeak_Attack:", p.attack1, "| 100% success rate",
                  "\nMedium_Attack:", p.attack2, "| 75% success rate", "\nStrong_Attack:", p.attack3,
                  "| 33% success rate", "\nHeal:", p.player_heal, "| 25% success rate", "\nInstant_Death:",
                  "infinite", "| 10% success rate", "\n--------------------------")
            time.sleep(1)
            player_attack_choice = input("Choose an attack to do. (type 'weak_attack', 'medium_attack', "
                                         "'strong_attack', 'heal', 'instant_death'): ")  # choices
            if player_attack_choice == 'weak_attack':  # what is played out by these choices
                p.first_attack(e)
            elif player_attack_choice == 'medium_attack':
                p.second_attack(e)
            elif player_attack_choice == 'strong_attack':
                p.third_attack(e)
            elif player_attack_choice == 'heal':
                p.heal_attack(p)
            elif player_attack_choice == 'instant_death':
                p.instant_death_attack(e)

            if e.health > 0:  # only if the enemy doesn't die from your attack, can they attack you
                e.enemy_attack(p)
