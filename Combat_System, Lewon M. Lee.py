for i in range(len(enemies)):  # for loop so all enemies in the list must be played out before exiting the
    # enemy encounter
    e = enemies.pop(i)  # pop out the first enemy, then the next in the list
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
