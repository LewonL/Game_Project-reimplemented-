import random
import time


#  ----- all Characters + unique / basic enemy class -----
class Entity:
    def __init__(self, name, health, attack, description):
        """
        The purpose of this class is to provide a template for all of the requirements of every enemy, Character,
        or Player. This is also the class used for basic enemies
        @type self: Entity
        @type name: str
        @type health: int
        @type attack: int
        @type description: str
        @rtype: None
        >> Enemy1 = Entity(name="Goblin", health=50, attack=15, description="A basic class enemy")
        Goblin. A basic class enemy.
        --------
        health: 50hp
        attack: 15 atk
        >> Enemy2 = Entity(name=Bob, health=30, attack=8, description=A basic class enemy)
        ERROR (name and description should be 'type: str')
        """
        self.name = name
        self.health = health
        self.attack = attack
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

    def initial_attack(self, Character):
        """
        'Character' in parenthesis is filled in by whatever character is chosen. This is the initial attack, which is
        the player's first and weakest attack as well as a basic enemy's only attack. Other enemies don't use this.
        @type self: Entity
        @type Character: var
        @rtype: str, int
        >> self.attack = 5
        >> player.initial_attack(enemy3)
        player dealt 5 attack of damage onto enemy3
        >> self.attack = 4
        >> player2_initial_attack(enemy4)
        ERROR (player2<_>initial_attack(enemy4) '<>', this should be a '.')
        """
        print("The attack did a total damage of:", self.attack)
        Character.receive_damage(self.attack)

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


#  ----- complex enemy class -----
class ComplexEnemy(Entity):
    def __init__(self, name, health, attack, description, attack2, attack3, attack4, attack5):
        """
        Complex enemies are enemies that can do more than 3 different attacks and are enemies with a
        large amount of health. This is an initial function that adds attributes in its own class from a pre-existing
        class called 'Entity'
        @type attack2: int
        @type attack3: int
        @type attack4: int
        @type attack5: int
        @rtype: None
        >> Enemy7 = Entity(name="Big Boy Bob", health=70, attack=10, attack2=12, attack3=15, attack4=1, attack5=20,
        description="A complex class enemy")
        Big Boy Bob. A complex class enemy.
        --------
        health: 70hp
        attack: 10, 12, 15, 1, 20 atk
        >> Enemy5 = Entity(name=Big Bob, health=40, attack=8, attack2=10, attack3=17, description=A complex class enemy)
        ERROR (name and description should be 'type: str')
        """
        Entity.__init__(self, name, health, attack, description)
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.attack5 = attack5

    def enemy_complex_attack(self, Character):
        """
        Randomly plays out a series of attacks that can be done. Meaning that when the enemy attacks, the damage that
        is done may be different.
        @type self: ComplexEnemy
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
            print("The attack does a total damage of:", self.attack5, "\n")
            Character.receive_damage(self.attack5)
        elif random.randint(1, 7) == 1:
            print("The attack does a total damage of:", self.attack4, "\n")
            Character.receive_damage(self.attack4)
        elif random.randint(1, 5) == 1:
            print("The attack does a total damage of:", self.attack3, "\n")
            Character.receive_damage(self.attack3)
        elif random.randint(1, 4) == 1:
            print("The attack does a total damage of:", self.attack2, "\n")
            Character.receive_damage(self.attack2)
        elif random.randint(1, 2) == 1:
            print("The attack does a total damage of:", self.attack, "\n")
            Character.receive_damage(self.attack)
        else:
            print("The attack missed...")
        print("\n")


#  ----- basic enemies -----
enemy1 = Entity(name="Zombie", health=15, attack=10, description="An basic enemy")
enemy2 = Entity(name="Skeleton", health=20, attack=8, description="A basic enemy")
enemy3 = Entity(name="Ghost", health=25, attack=15, description="A basic enemy")


#  ----- complex enemies -----
enemy4 = ComplexEnemy(name="Blind Man", health=30, attack=5, attack2=8, attack3=10, attack4=12,
                      attack5= 15, description="A complex enemy")
enemy5 = ComplexEnemy(name="Jeffrey", health=40, attack=3, attack2=4, attack3=14, attack4=15,
                      attack5=18, description="A complex enemy")
enemy6 = ComplexEnemy(name="Tall Ghost", health=45, attack=2, attack2=10, attack3=12, attack4=30,
                      attack5=32, description="A complex enemy")
enemy7 = ComplexEnemy(name="Tiger's Eye", health=30, attack=15, attack2=2, attack3=15, attack4=2,
                      attack5=40, description="A complex enemy")
enemy8 = ComplexEnemy(name="Memento Mori", health=100, attack=6, attack2=9, attack3=12, attack4=4,
                      attack5=30, description="A complex enemy")
enemy9 = ComplexEnemy(name="AlphaGhost", health=80, attack=12, attack2=8, attack3=16, attack4=14,
                      attack5=1, description="A complex enemy")

enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]
e = enemies.pop(0)


#  ----- player class -----
class Player(Entity):
    def __init__(self, name, health, attack, description, attack2, attack3, heal, instant_death):
        """
        This is an initial function that adds attributes in its own class from a pre-existing
        class called 'Entity'
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
        Entity.__init__(self, name, health, attack, description)
        self.attack2 = attack2
        self.attack3 = attack3
        self.heal = heal
        self.instant_death = instant_death


    def second_attack(self, Character):
        """
        For a second attack. Normal attack, 75% chance of success.
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.attack2 = 22
        >> player1.second_attack(enemy1)
        player1 dealt 22 attack of damage onto enemy1
        or
        you missed...
        >> self.attack = 6
        >> player1.second_attack(enemy1)
        ERROR (This function is for the second attack, calling 'second_attack' won't do anything because self.attack was
        defined, but not self.attack2)
        """
        print("You try your normal attack:")
        if random.randint(1, 4) == 1:
            print("You missed...\n")
        else:
            print("The attack did a total damage of:", self.attack2, "\n")
            Character.receive_damage(self.attack2)

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
        >> self.attack2 = 32
        >> player1.third_attack(enemy4)
        ERROR (This function is for the third attack, calling 'third_attack' won't do anything because self.attack2 was
        defined, but not self.attack3)
        """
        print("You try your strong attack:")
        time.sleep(1)
        if random.randint(1, 3) == 1:
            print("The attack did a total damage of:", self.attack3, "\n")
            Character.receive_damage(self.attack3)
        else:
            print("You missed...")

    def heal_attack(self, Character):
        """
        The player heals himself/herself, 25% chance of success
        @type self: Player
        @type Character: var
        @rtype: str, int
        >> self.heal_attack = 30
        >> player1.heal_attack(player1)
        Player1 healed 30 health
        >> self.heal_attack = 20
        >> player1.heal_attack(enemy1)
        enemy1 healed 20 health (the point of the heal attack is to heal yourself, not the enemy)
        """
        print("You try to heal yourself:")
        time.sleep(1)
        if random.randint(1, 4) == 1:
            print("A total of", self.heal, "health had been healed\n")
            Character.receive_heal_ability(self.heal)
        else:
            print("You were unable to heal\n")

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
            print("The attack was a success\n")
            Character.receive_damage(self.instant_death)
        else:
            print("The attack failed\n")


# ----- the player -----
player1 = Player(name="player1", health=100, attack=10, attack2=15, attack3=40,
                 heal=30, instant_death=999999999999999, description="The Player you control")


# ----- combat, example -----

# Player attack enemy:
player1.initial_attack(enemy1)
player1.second_attack(enemy1)
player1.third_attack(enemy1)
player1.instant_death_attack(enemy1)

# Basic, Medium, Complex enemy attack Player:
enemy1.initial_attack(player1)
enemy4.enemy_complex_attack(player1)

# Player heal ability:
player1.heal_attack(player1)
