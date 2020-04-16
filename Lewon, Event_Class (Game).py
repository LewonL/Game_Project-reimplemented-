import random
import time


class BuffAndDebuff:
    def __init__(self, heal_buff_a, strength_buff_a, poison_debuff_a, weakness_debuff_a, name, description):
        """
        Initial function for buff and debuffs. Methods use these attributes tooo create different types of buffs
        and debuffs. All buffs and debuffs have these attributes but use only one, with exception to.
        name and description.
        @type heal_buff_a: int
        @type strength_buff_a: int
        @type poison_debuff_a: int
        @type weakness_debuff_a: int
        @type name: str
        @type description: str
        @rtype: None
        >> buff = BuffAndDebuff(heal_buff_a=5, strength_buff_a=0, poison_debuff_a=0, weakness_debuff_a=0,
        name="heal", description="heals 5 player hp")
        Heal_buff:
        name = heal
        description = "heals 5 player hp
        heals: 5 hp
        >> buff1 = BuffAndDebuff(heal_buff_a=10, strength_buff_a=0, poison_debuff_a=0, weakness_debuff_a=0,
        name=heal, description=heals 10 player hp)
        ERROR ('name' and 'description' should be data type: 'str')
        """
        self.heal_buff_a = heal_buff_a
        self.strength_buff_a = strength_buff_a
        self.poison_debuff_a = poison_debuff_a
        self.weakness_debuff_a = weakness_debuff_a
        self.name = name
        self.description = description

    def receive_heal_buff(self, receive_heal_buff_variable):
        """
        This function is used only as a part of the 'heal_buff' function.
        @type self: BuffAndDebuff
        @type receive_heal_buff_variable: var
        @rtype: None
        >> self.heal_buff_a = 6
        >> p.receive_heal_buff(self.heal_buff_a)
        player1 healed 6 hp
        >> self.heal_buff_a = 4
        >> p.receive_heal_buf(self.heal_buff_a)
        ERROR (typo in 'receive heal buf', therefore function cannot be called)
        """
        p.health += receive_heal_buff_variable

    def heal_buff(self, Character):
        """
        A buff that heals the player would use this function.
        @type self: BuffAndDebuff
        @type Character: var
        @rtype: var, int
        >> buff1 = 10
        >> buff1.heal_buff(p)
        player1 healed 10 hp
        >> buff2 = 6
        >> buff2.heal_buff()
        ERROR (Nothing is in parameters)
        """
        print("You have been healed")
        time.sleep(2)
        print("A total of", self.heal_buff_a, "health had been healed\n")
        Character.receive_heal_buff(self.heal_buff_a)

    def receive_poison_debuff(self, receive_poison_debuff_variable):
        """
        This function is used only as a part of the 'poison_debuff' function.
        @type self: BuffAndDebuff
        @type receive_poison_debuff_variable: var
        @rtype: None
        >> self.poison_debuff_a = 4
        >> p.receive_poison_debuff(self.poison_debuff_a)
        player1 received 4 atk damage
        >> self.poison_debuff_a = 3
        >> p.receive_poison_debuf(self.poison_debuff_a)
        ERROR (typo in 'receive poison buf', therefore function cannot be called)
        """
        p.health -= receive_poison_debuff_variable

    def poison_debuff(self, Character):
        """
        A buff that poisons/hurts the player would use this function.
        @type self: BuffAndDebuff
        @type Character: var
        @rtype: var, int
        >> buff1 = 10
        >> buff1.poison_debuff(p)
        player1 lost 10 hp
        >> buff2 = 6
        >> buff2.poison_debuff()
        ERROR (Nothing is in parameters)
        """
        print("You have been affected with poison")
        time.sleep(2)
        print("You lost", self.poison_debuff_a, "health\n")
        Character.receive_poison_debuff(self.poison_debuff_a)

    def receive_strength_buff(self, receive_attack_buff_variable):
        """
        This function is used only as a part of the 'strength_buff' function.
        @type self: BuffAndDebuff
        @type receive_attack_buff_variable: var
        @rtype: None
        >> self.strength_buff_a = 8
        >> p.receive_strength_buff(self.strength_buff_a)
        player1 received 8 attack for all attacks
        >> self.strength_buff_a = 4
        >> p.receive_strength_buf(self.strength_buff_a)
        ERROR (typo in 'receive strength buf', therefore function cannot be called)
        """
        p.attack1 += receive_attack_buff_variable
        p.attack2 += receive_attack_buff_variable
        p.attack3 += receive_attack_buff_variable

    def strength_buff(self, Character):
        """
        A buff that increases the player's attack would use this function.
        @type self: BuffAndDebuff
        @type Character: var
        @rtype: var, int
        >> buff1 = 10
        >> buff1.strength_buff(p)
        player1 gained 10 atk for all attacks
        >> buff2 = 6
        >> buff2.strength_buff()
        ERROR (Nothing is in parameters)
        """
        print("You got a strength buff")
        time.sleep(2)
        print(self.strength_buff_a, "atk has been added to all of your attacks\n")
        Character.receive_strength_buff(self.strength_buff_a)

    def weapon_function(self, Character):
        """
        This function is for weapons, but they use they 'strength_buff' function because weapons and strength buffs do
        the same thing.
        @type self: BuffAndDebuff
        @type Character: var
        @rtype: var, int
        >> weapon1 = 12
        >> weapon.strength_buff(p)
        player1 gained 12 atk for all attacks
        >> weapon2 = 6
        >> weapon2.strength_buff()
        ERROR (Nothing is in parameters)
        """
        print("You got a", Character.name)
        time.sleep(2)
        print(self.strength_buff_a, "atk has been added to all of your attacks\n")
        Character.receive_strength_buff(self.strength_buff_a)

    def receive_weakness_buff(self, receive_attack_debuff_variable):
        """
        This function is used only as a part of the 'weakness_debuff' function.
        @type self: BuffAndDebuff
        @type receive_attack_debuff_variable: var
        @rtype: None
        >> self.weakness_buff_a = 8
        >> p.receive_weakness_buff(self.weakness_buff_a)
        player1 lost 8 attack for all attacks
        >> self.weakness_buff_a = 4
        >> p.receive_weakness_buf(self.strength_buff_a)
        ERROR (typo in 'receive weakness buf', therefore function cannot be called)
        """
        p.attack1 -= receive_attack_debuff_variable
        p.attack2 -= receive_attack_debuff_variable
        p.attack3 -= receive_attack_debuff_variable

    def weakness_debuff(self, Character):
        """
        A buff that increases the player's attack would use this function.
        @type self: BuffAndDebuff
        @type Character: var
        @rtype: var, int
        >> buff1 = 10
        >> buff1.weakness_debuff(p)
        player1 lost 10 atk for all attacks
        >> buff2 = 6
        >> buff2.weakness_debuff()
        ERROR (Nothing is in parameters)
        """
        print("You have been affected by weakness...")
        time.sleep(2)
        print(self.weakness_debuff_a, "atk has been taken away from all of your attacks\n")
        Character.receive_strength_buff(self.weakness_debuff_a)


buff1 = BuffAndDebuff(heal_buff_a=40, strength_buff_a=0, poison_debuff_a=0, weakness_debuff_a=0,
                      name="heal", description="Heals you by 40hp")
buff2 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=5, poison_debuff_a=0, weakness_debuff_a=0,
                      name="strength", description="Increases your atk by 5")
weapon1 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=10, poison_debuff_a=0, weakness_debuff_a=0,
                      name="baseball_bat", description="Increases your attack by 10")
weapon2 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=17, poison_debuff_a=0, weakness_debuff_a=0,
                      name="crowbar", description="Increases your attack by 17")
debuff1 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=0, poison_debuff_a=20, weakness_debuff_a=0,
                        name="poison, I", description="Damages you by 20hp")
debuff2 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=0, poison_debuff_a=30, weakness_debuff_a=0,
                        name="poison, II", description="Damages you by 30hp")
debuff3 = BuffAndDebuff(heal_buff_a=0, strength_buff_a=0, poison_debuff_a=0, weakness_debuff_a=5,
                        name="weakness", description="Decreases your attack by 5")


class Event:

    def event_call(self):
        """
        This function is activated when an event is to be inserted.
        Initializes a random event. The __init__ function, but just called 'event_call' so it is usable.
        5 events in total
        1) Item
        2) Monster
        3) Trap
        4) Blessing
        5) Your choice (Puzzle)
        @type self: Event
        @rtype: None
        >> event_call()
        *Function randomly picks an event out of the 5 listed*
        >> event_call[]
        ERROR (square brackets should not be used for calling out a function
        """
        event_choice = random.randint(1, 5)

        if event_choice == 1:
            self.event = self.event_item()
        elif event_choice == 2:
            self.event = self.event_monster
        elif event_choice == 3:
            self.event = self.event_trap
        elif event_choice == 4:
            self.event = self.event_blessing
        elif event_choice == 5:
            self.event = self.event_quiz

    def event_item(self):
        """
        Randomly called out by the 'event_call' function. You do not call this one out separately.
        1) Crowbar
        2) Heal
        3) Strength
        4) Poison I
        5) Baseball Bat
        6) Poison II
        7) Nothing
        8) Nothing
        9) Nothing
        10) Nothing
        11) Nothing
        @type self: Event
        @rtype: int, str
        >> event_item()
        function works
        >> event_item[]
        ERROR (square brackets should not be used for calling out a function)
        """
        time.sleep(1)
        item_choice = random.randint(1, 11)

        item_dict = {1: weapon2.weapon_function(p), 2: buff1.heal_buff(p), 3: buff2.strength_buff(p),
                     4: debuff1.poison_debuff(p), 5: weapon1.weapon_function(p), 6: debuff2.poison_debuff(p),
                     7: debuff3.weakness_debuff(p), 8: 'Nothing', 9: 'Nothing', 10: 'Nothing', 11: 'Nothing'}

        return item_dict[item_choice]

    def event_monster(self):
        """
        Randomly called out by the 'event_call' function. You do not call this one out separately.
        @type self: Event
        @rtype: lst
        >> event_monster()
        function works
        >> event_monster[]
        ERROR (square brackets should not be used for calling out a function)
        """
        if random.randint(1, 22) == 1:
            enemies = [enemy1, enemy3, enemy4, enemy7, enemy1]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 14) == 1:
            enemies = [enemy1, enemy8, enemy9]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 12) == 1:
            enemies = [enemy1, enemy2, enemy9]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 12) == 1:
            enemies = [enemy5, enemy7]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 12) == 1:
            enemies = [enemy4, enemy6]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 7) == 1:
            enemies = [enemy3, enemy2]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 7) == 1:
            enemies = [enemy1, enemy2]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 7) == 1:
            enemies = [enemy3, 1]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 7) == 1:
            enemies = [enemy9]
            e = enemies.pop(0)
            # import combat system
        elif random.randint(1, 4) == 1:
            enemies = [enemy2, enemy2]
            e = enemies.pop(0)
            # import combat system
        else:
            enemies = [enemy1, enemy1]
            e = enemies.pop(0)
            # import combat system

    def event_trap(self):
        """
        Randomly called out by the 'event_call' function. You do not call this one out separately.
        @type self: Event
        @rtype: str, int
        >> event_trap()
        function works
        >> event_trap[]
        ERROR (square brackets should not be used for calling out a function)
        """
        time.sleep(0.5)
        print("It's a trap!!!")
        time.sleep(1)
        print("To get out, you must solve a question: ")
        time.sleep(1)
        correct_trap = "Correct. You get out of the trap"
        incorrect_trap = "Incorrect. You don't get out of the trap"
        trap_questions = True
        while trap_questions:
            if random.randint(1, 2) == 1:
                trap_question_1 = input("When was the year in which the Statute of Westminister was signed?: ")
                if trap_question_1 == "1931":
                    print(correct_trap, "\n")
                    trap_questions = False
                else:
                    print(incorrect_trap, "\n")
                    debuff1.poison_debuff(p)
            else:
                trap_question_2 = input("What is 5 / 2?: ")
                if trap_question_2 == "2.5":
                    print(correct_trap, "\n")
                    trap_questions = False
                else:
                    print(incorrect_trap, "\n")
                    debuff2.poison_debuff(p)

    def event_blessing(self):
        """
        Randomly called out by the 'event_call' function. You do not call this one out separately.
        @type self: Event
        @rtype: int
        >> event_blessing()
        function works
        >> event_blessing[]
        ERROR (square brackets should not be used for calling out a function)
        """
        time.sleep(1)
        if random.randint(1, 4):
            print("You have been blessed", buff1.heal_buff, "health increase.")
            buff1.heal_buff(p)
        elif random.randint(1, 5):
            print("You have been blessed", buff2.strength_buff, "atk increase.")
            buff2.strength_buff(p)
        else:
            print("You have not been blessed anything")

    def event_quiz(self):
        """
        Randomly called out by the 'event_call' function. You do not call this one out separately.
        @type self: Event
        @rtype: str, int
        >> event_quiz()
        function works
        >> event_quiz[]
        ERROR (square brackets should not be used for calling out a function)
        """
        time.sleep(1)
        correct_quiz = "Correct. You get a buff"
        incorrect_quiz = "Incorrect. You get a debuff"
        quiz_questions = True
        while quiz_questions:
            if random.randint(1, 2) == 1:
                question_1 = input("Who was the 44th US President? (Last_name): ")
                if question_1 == "Obama":
                    print(correct_quiz, "\n")
                    quiz_questions = False
                    buff1.heal_buff(p)
                else:
                    print(incorrect_quiz, "\n")
                    debuff1.poison_debuff(p)
            else:
                question_2 = input("What is 10 * 2 - 2?: ")
                if question_2 == "18":
                    print(correct_quiz, "\n")
                    quiz_questions = False
                    buff1.heal_buff(p)
                else:
                    print(incorrect_quiz, "\n")
                    debuff1.poison_debuff(p)
