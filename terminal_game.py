import pyfiglet
import random

ascii_art = pyfiglet.figlet_format("Welcome to the Arena!")
print(ascii_art)

#Asks player for their name. Initially sets empty strings for armor and main stat.
input_name = input("What is your fighter's name? \n")

input_armor = ""
input_stat = ""


#Asks for player's main stat. Input stat the is used to calculate strength and dexterity.
while input_stat != "strength" and input_stat != "dexterity":
    input_stat = input("What is your fighter's main stat, strength or dexterity? (Main stat will be assigned a 5, while the other will be assigned a 2) \n").lower()

if input_stat == "strength":
    input_str = 5
    input_dex = 2
    main_stat = 5
else:
    input_str = 2
    input_dex = 5
    main_stat = 5


#Asks for armor choice. Input armor is used to calculate the player's armor rating. If player types "armor_list", it will print the list of armors and their armor ratings. If player chooses plate armor but has dexterity as their main stat, it will tell them they cannot wear plate armor and ask them to choose again.
while input_armor != "leather" and input_armor != "plate":
    input_armor = input("What armor do you choose? For list of armors, type 'armor_list'. \n").lower()
    if input_stat == "dexterity" and input_armor == "plate":
        print("You cannot wear plate armor because your main stat is dexterity. \n")
        input_armor = ""
    if input_armor == "armor_list":
        print("Leather - 13 + dexterity armor rating. Leather can be work by either strength or dexterity fighters.\nPlate - 16 + dexterity armor rating. Plate can only be worn by strength fighters.")


if input_armor == "leather":
    input_armor_rating = 13 + input_dex
else:
    input_armor_rating = 16 + input_dex

print("Your fighter's name is " + input_name + ", their weapons are a +3 Sword and a +3 Bow, their armor is " + input_armor + ", their strength is " + str(input_str) + ", their dexterity is " + str(input_dex) + ", and their armor rating is " + str(input_armor_rating) + ".")
print("\n")

#creates the fighter class, which will be used to create the player and the enemyfighters. It has the attributes of name, weapon, armor, main stat, and armor rating.
class Fighter:
    def __init__(self, input_name, input_armor, input_dex, input_str, input_armor_rating, main_stat, input_health = 60):
        self.name = input_name
        self.armor = input_armor
        self.dexterity = input_dex
        self.strength = input_str
        self.armor_rating = input_armor_rating
        self.main_stat = main_stat
        self.health = input_health

print("Now that you've created your character, I will explain how the battle system works: \n")
print("Each turn, you will choose to either attack with your sword or bow.")
print("With each attack, you will roll a d20 to determine if your attack hits against your enemy's armor rating.")
print("If you roll a 20, you will get a critical hit and deal double damage. If you roll a 1, you will miss and deal no damage. If you roll a number between 2 and 19, you will hit and deal normal damage.") 
print("The battle continues until either you or the enemy fighter's health reaches 0.")

player = Fighter(input_name, input_armor, input_dex, input_str, input_armor_rating, main_stat)
enemy = Fighter("Dravnok", "leather", 5, 2, 18, 5)

#function for the combat system.
def combat(player, enemy):
    while player.health > 0 and enemy.health > 0:
        input_attack = input("Do you want to attack with your sword or bow? Type 1 for sword or 2 for bow.\n").lower()
        if input_attack == "1":
            damage = player.main_stat + 3
        elif input_attack == "2":
            damage = player.main_stat + 3
        else:
            print("Invalid input. Please choose either '1' for sword or '2' for bow.")
            continue

        roll = random.randint(1, 20)
        if roll == 20:
            print("Critical hit! You deal double damage.")
            damage *= 2
        elif roll == 1:
            print("You missed! You deal no damage.")
            damage = 0
        elif roll + player.main_stat  + 3 >= enemy.armor_rating:
            print("You hit the enemy!")
        else:
            print("You missed! You deal no damage.")
            damage = 0

        enemy.health -= damage
        print(f"You dealt {damage} damage to the enemy. Enemy health is now {enemy.health}. \n")

        if enemy.health <= 0:
            print("You have defeated the enemy!")
            break

        # Enemy's turn to attack
        print("it is now the enemy's turn to attack. \n")
        enemy_damage = random.randint(1, 6) + enemy.dexterity + 3
        enemy_roll = random.randint(1, 20) 
        if enemy_roll == 20:
            print("Enemy lands a critical hit! They deal double damage.")
            enemy_damage *= 2
        elif enemy_roll == 1:
            print("Enemy missed! They deal no damage.")
            enemy_damage = 0
        elif enemy_roll + enemy.main_stat + 3 >= player.armor_rating:
            print("Enemy hits you!")
        else:
            print("Enemy missed! They deal no damage.")
            enemy_damage = 0

        player.health -= enemy_damage
        print(f"The enemy dealt {enemy_damage} damage to you. Your health is now {player.health}. \n")

    if player.health <= 0:
        print("You have been defeated by the enemy.")

combat(player, enemy)