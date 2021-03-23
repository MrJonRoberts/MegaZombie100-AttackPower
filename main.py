#MegaZombie 100% Attack
import random

def getRandomWeakness(weaponList):
    weakness = []
    for w in weaponList:
        weakness.append(w['power'])
    
    return random.choice(weakness)

def createWeaponList():
    weaponList = []
    sword = { "name": "Mighty Sword", "damage": 10, "power": "slice"}
    gun = {"name": "BFG", "damage": 5, "power": "headshot"}
    bat = {"name": "Slugger", "damage": 7, "power": "homerun"}
    weaponList.append(sword)
    weaponList.append(gun)
    weaponList.append(bat)
    return weaponList

def generateZombie(weapons):
    zombie = dict()
    zombie['health'] = random.randint(1,10)
    zombie['weakness'] = getRandomWeakness(weapons)
    return zombie


def generateWeapon(name, weapons):
    weapon = { "name": name, "damage": random.randint(4,10),
               "power": getRandomWeakness(weapons)}
    return weapon


weapons = createWeaponList()
zombie = generateZombie(weapons)


print("You have encountered a zombie, prepare to fight!")
print("You have the following weapons: ")
for weapon in weapons:
    print(f"\t {weapon['name']}")

choice = int(input("Enter 1 to select a weapon, 2 to pick your own"))
if choice == 1:
    goodChoice = False
   
    while goodChoice == False:
        weaponChoice = input("Enter the name of a weapon... quick")
        for w in weapons:
           
            if w['name'] == weaponChoice:
                goodChoice = True
                weaponChoice = w 
                break;
else:
    weaponName = input("Please enter a name for your weapon")
    weaponChoice = generateWeapon(weaponName, weapons)
    weapons.append(weaponChoice)
    
print(f"You have chosen: {weaponChoice['name']}")

# calc battle
if zombie['weakness'] == weaponChoice['power']:
    print(f"Using {weaponChoice['name']}' power of {weaponChoice['power']}")
    print(f"You successfully hit the zombie for {weaponChoice['damage']}")
    if zombie['health'] - weaponChoice['damage'] <= 0:
        print(f"You killed the zombie")
    else:
        print(f"You damaged the zombie")
else:
    print(f"{weaponChoice['name']} is ineffective against the zombie")
    print(f"(if only your weapon had {zombie['weakness']} as a power!")

