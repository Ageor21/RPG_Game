import random

# A list of alignment choices
alignment = ["Law", "Neutral", "Chaos"]

# A list of classes that the user can choose from
classes = ["warrior", "knight", "mage", "thief", "cleric", "pyromancer"]

# Weapon selection
weapons = ["sword", "spear", "spell staff", "knives", "wand", "mace"]

# Health for the user's character, will display when in battle
health = 40

# Enemies that you have a chance of encountering and the health that they will be assign
enemies = ["Slime", "Goblin", "Gorgon", "Ghoul", "Orc"]
enemies_health = [10, 20, 30, 40, 50]

# List of attacks the enemy can do
enemy_actions = ["attack", "spell", "defend"]


def rpg_char():
    # Defining the alignment and Class variable globally
    global alignment
    global classes

    # The alignment choices will be completely random
    align_choice = random.choice(alignment)

    # A dictionary of stats that randomly distribute points from a range of 0-10
    stats = {"Strength": random.randint(0, 10), "Defense": random.randint(0, 10), "Magic": random.randint(0, 10),
             "Accuracy": random.randint(0, 10), "Speed": random.randint(0, 10)}

    # Begins the game
    input("Press Enter to begin the game: ")

    # Once the random alignment is picked, the program informs the user of said alignment
    print("\nAlignment choice: " + align_choice)
    print("You are now " + align_choice)

    try:
        # If the user is of Law alignment, the program will give a brief summary of the chose
        if align_choice == "Law":
            print("\nYou are the divine messenger of fate, a righteous warrior of light")

            # User is expected to input a name, then a welcome message with their name is printed, and stats are assign
            global name

            name = input("Pick a name for your character: ")
            print(f"\nHello {name}, lets customize yourself."
                  " Here are your pre-determined stats: ")
            print(stats)

            # User needs to pick a class from the selection
            class_choice = str(input("\nPick a class for you character:"
                                     " Warrior, Knight, Mage, Thief, Cleric, Pyromancer: "))

            if class_choice in classes:
                    print(f"\nLet your journey begin, young {class_choice} of {align_choice}\n")
            else:
                print("Not a class in the list\n")
                rpg_char()

        # If the user is of Neutral alignment, the program will give a brief summary of the chose
        if align_choice == "Neutral":
            print("\nYou are person of equal value, you take part in no sides, but see the truth of both")

            # User is expected to input a name, then a welcome message with their name is printed, and stats are assign
            name = input("Pick a name for your character: ")
            print(f"\nHello {name}, lets customize yourself."
                  " Here are your pre-determined stats: ")
            print(stats)

            # User is expected to choose a class for their character
            class_choice = str(input("\nPick a class for you character: "
                                     "Warrior, Knight, Mage, Thief, Cleric, Pyromancer: "))

            if class_choice in classes:
                print(f"\nLet your journey begin, young {class_choice} of {align_choice}\n")
            else:
                print("Not a class in the list\n")
                rpg_char()

        # If the user is of Chaos alignment, the program will give a brief summary of the chose
        if align_choice == "Chaos":
            print("\nYou are the bringer of death, you destroy anything in your path")

            # User is expected to input a name, then a welcome message with their name is printed
            name = input("Pick a name for your character: ")
            print(f"\nHello {name}, lets customize yourself."
                  " Here are your pre-determined stats: ")
            print(stats)

            # User is expected to choose a class for their character
            class_choice = str(input("\nPick a class for you character: "
                                     "Warrior, Knight, Mage, Thief, Cleric, Pyromancer: "))

            if class_choice in classes:
                print(f"\nLet your journey begin, young {class_choice} of {align_choice}\n")
            else:
                print("Not a class in the list\n")
                rpg_char()

    # For any exceptions that may occur
    except ValueError:
        print("Oops, not a letter. try again ")
        rpg_char()
    except Exception as e:
        print(e)
        print("That method was wrong, please try again")
        rpg_char()


def char_weapon():
    # Defining the weapons variable globally and asking the user to choose a weapon
    global weapons
    weapon_choice = input("What weapon will you choose:\n" + ", ".join(weapons))

    # It will iterate through the weapons list and if true the user will obtain that weapon
    if weapon_choice in weapons:
        print(f"\nUse your {weapon_choice} in battle the upcoming enemies, ")
    else:
        print("\nThat is not a weapon in the list, nice try")
        char_weapon()

    # Will start your first battle
    print("\nNow it is time to fight your first enemy")


def battle():
    # Defining the needed variables globally
    global enemies
    global enemies_health
    global health

    # Randomizes the enemies, their health, and actions
    ran_enemies = random.choice(enemies)
    ran_health = random.choice(enemies_health)

    # Prints the name of the enemy the user will battle
    print("Your first enemy is a {}".format(ran_enemies))

    # Prints the UI look of yourself and the enemy
    print(f"Name: "
          f"  {name}   {ran_enemies}"
          f"\nHP:  {health}    {ran_health}")
    actions = input("\nAttack  \nSpell"
                    "\nDefend   \nRun:  ")

# The process for the battle, the user takes a turn then the enemy does, etc
    while True:
        global enemy_actions
        list_actions = random.choice(enemy_actions)

        # If the user attacks the enemy is damage for 5 hp, then a message is displayed, the next turn
        if actions == "attack":
            ran_health += -5
            print("The {} took massive damage".format(ran_enemies))
            print(f"\nName: "
                  f"\n{name}     {ran_enemies}"
                  f"\nHP:  {health}    {ran_health} ")
            actions = input("\nAttack  \nSpell"
                            "\nDefend   \nRun: ")

            # The enemy will take either of 3 actions against the user
            if list_actions == "attack" or list_actions == "spell":
                health += -4
                print(f"The {ran_enemies} used {list_actions}")
                print(f"\nName: "
                      f"\n{name}     {ran_enemies}"
                      f"\nHP:  {health}    {ran_health} ")
                actions = input("\nAttack  \nSpell"
                                "\nDefend   \nRun: ")

            # If the enemy defends the user attack's, the enemy takes less damage
            elif list_actions == "defend":
                ran_health += -2
                print(f"The {ran_enemies} defended")
                print(f"\nName: "
                      f"\n{name}     {ran_enemies}"
                      f"\nHP:  {health}    {ran_health} ")
                actions = input("\nAttack  \nSpell"
                                "\nDefend   \nRun: ")

        # Same principle, spell attacks take 5 hp from enemy
        if actions == "spell":
            ran_health += -5
            print("The {} took massive damage".format(ran_enemies))
            print(f"\nName: "
                  f"\n{name}     {ran_enemies}"
                  f"\nHP:  {health}    {ran_health} ")
            actions = input("\nAttack  \nSpell"
                            "\nDefend   \nRun: ")

            # Enemy attacks take 4 hp from user
            if list_actions == "attack" or list_actions == "spell":
                health += -4
                print(f"The {ran_enemies} used {list_actions}")
                print(f"\nName: "
                      f"\n{name}     {ran_enemies}"
                      f"\nHP:  {health}    {ran_health} ")
                actions = input("\nAttack  \nSpell"
                                "\nDefend   \nRun: ")

            # If the enemy defends the user attack's, the enemy takes less damage
            elif list_actions == "defend":
                ran_health += -2
                print(f"The {ran_enemies} defended")
                print(f"\nName: "
                      f"\n{name}     {ran_enemies}"
                      f"\nHP:  {health}    {ran_health} ")
                actions = input("\nAttack  \nSpell"
                                "\nDefend   \nRun: ")

        # If user defends on a turn, it continues and takes less damage
        if actions == "defend":
            ran_health += 0
            print("You blocked the {} attack ".format(ran_enemies))
            print(f"\nName: "
                  f"\n{name}     {ran_enemies}"
                  f"\nHP:  {health}    {ran_health} ")
            actions = input("\nAttack  \nSpell"
                            "\nDefend   \nRun: ")

            if list_actions == "attack" or list_actions == "spell":
                health += -2
                print(f"The {ran_enemies} used {list_actions}")
                print(f"\nName: "
                      f"\n{name}     {ran_enemies}"
                      f"\nHP:  {health}    {ran_health} ")
                actions = input("\nAttack  \nSpell"
                                "\nDefend   \nRun: ")

            elif list_actions == "defend":
                ran_health += 0
            print(f"The {ran_enemies} defended")
            print(f"\nName: "
                  f"\n{name}     {ran_enemies}"
                  f"\nHP:  {health}    {ran_health} ")
            actions = input("\nAttack  \nSpell"
                            "\nDefend   \nRun: ")

        # If both opponents defend no one takes damage
        if list_actions and actions == "defend":
            ran_health += 0
            print(f"You and the {ran_enemies} both defended")
            print(f"\nName: "
                  f"\n{name}     {ran_enemies}"
                  f"\nHP:  {health}    {ran_health} ")
            actions = input("\nAttack  \nSpell"
                            "\nDefend   \nRun: ")

        # If the user runs from the battle, the game instantly ends
        if actions == "run":
            print("You escaped battle, I guess you won?")
            break

        # If either player or enemy's health reaches 0, the game ends
        if ran_health <= 0:
            print("You defeated the enemy congrats!")
            break
        elif health <= 0:
            print("You were defeated!")
            break


if __name__ == "__main__":
    rpg_char()
    char_weapon()
    battle()
