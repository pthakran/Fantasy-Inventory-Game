stuff={'rope':1,'gold coin':42}
dragonloot = ['gold coin','dagger','gold coin','gold coin','ruby']

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(str(v)+' '+str(k))
        item_total += v
    print("Total number of Items: "+str(item_total))
    
def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] +=1
    return inventory

inv= addToInventory(stuff,dragonloot)
displayInventory(inv)
