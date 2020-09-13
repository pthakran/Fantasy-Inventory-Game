def totalInventory():
    total = 0
    for k, v in inventory.items():
        total = total + inventory.get(k, v)
    return total

def displayInventory():
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
    print('Total number of items: ' + str(totalInventory()))

def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k, 0)
        inventory[k] += 1
    return inventory

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory()

