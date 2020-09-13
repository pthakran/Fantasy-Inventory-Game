#A simple random simulator that gives you loots.
import random
inventory = {
    'Wooden Sword': '1',
    'Gold coins': '500',
    'Basic Health Potion': '2'
}

itemGenerator = {
    'Weapon': ['Stone Sword', 'Diamond Sword', 'Hokuto Bow'],
    'Materials': ['Ruby', 'Gold', 'Crystal'],
    'Gold coins': ''
}

def displayInventory():
    for k, v in inventory.items():
        print('You have: ' + v + 'x ' + k + '.')

def randomLoot():
    newLoot = {}
    for k in itemGenerator.items():
        k = random.choice(list(itemGenerator.keys()))
        if k == 'Weapon':
            v = random.choice(list(itemGenerator[k]))
            newLoot.setdefault(k, random.randint(1, 3))
            break
        elif k == 'Materials':
            v = random.choice(list(itemGenerator[k]))
            newLoot.setdefault(k, random.randint(1, 25))
            break
        elif k == 'Gold coins':
            newLoot.setdefault(k, random.randint(50, 500))
            break
    print(newLoot)

print('Welcome new player!')
print('What is your name?')
name = input()
print('Great! ' + str(name) + ',' + ' here is your starting items: ')
displayInventory()
randomLoot()


