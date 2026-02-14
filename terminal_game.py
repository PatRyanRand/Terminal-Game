import pyfiglet


ascii_art = pyfiglet.figlet_format("Welcome to the Arena!")
print(ascii_art)

#asks the user for their fighter's name weapon choice, armor choice, their main stat, and thier armor rating, and then creates a fighter object with those attributes.
input_name = input("What is your fighter's name? \n")

input_weapon = ""
input_armor = ""
input_stat = ""

while input_stat != "strength" and input_stat != "dexterity":
    input_stat = input("What is your fighter's main stat, strength or dexterity? (Main stat will be assigned a 5, while the other will be assigned a 2) \n").lower()

if input_stat == "strength":
    input_str = 5
    input_dex = 2
else:
    input_str = 2
    input_dex = 5

while input_weapon != "sword" and input_weapon != "bow":
    input_weapon = input("What weapon do you choose? For list of weapons, type 'weapon_list'. ").lower()
    if input_weapon == "weapon_list":
        print("Sword - 1d8 + strength\nBow - 1d8 + dexterity")

while input_armor != "leather" and input_armor != "plate":
    input_armor = input("What armor do you choose? For list of armors, type 'armor_list'. ").lower()
    if input_stat == "dexterity" and input_armor == "plate":
        print("You cannot wear plate armor because your main stat is dexterity.")
        input_armor = ""
    if input_armor == "armor_list":
        print("Leather - 13 + dexterity armor rating. Leather can be work by either strength or dexterity fighters.\nPlate - 16 + dexterity armor rating. Plate can only be worn by strength fighters.")

if input_armor == "leather":
    input_armor_rating = 13 + input_dex
else:
    input_armor_rating = 16 + input_dex

print("Your fighter's name is " + input_name + ", their weapon is a " + input_weapon + ", their armor is " + input_armor + ", their strength is " + str(input_str) + ", their dexterity is " + str(input_dex) + ", and their armor rating is " + str(input_armor_rating) + ".")
print("\n")

#creates the fighter class, which will be used to create the player and the enemyfighters. It has the attributes of name, weapon, armor, main stat, and armor rating.
class Fighter:
    def __init__(self, input_name, input_weapon, input_armor, input_dex, input_str, input_armor_rating, input_health = 60):
        self.name = input_name
        self.weapon = input_weapon
        self.armor = input_armor
        self.dexterity = input_dex
        self.strength = input_str
        self.armor_rating = input_armor_rating
        self.health = input_health

