my_list= "coal", "wood", "wood", "diamond", "diamond", "diamond"
def enumerate(my_list):

    inventory = enumerate(my_list)
    for item in inventory:
        index, value = item
    print(index, value)

    for index, value in enumerate(my_list):
        print(index, value)


def add_items(map_inv, list_items, dir=1):
    new_inv = dict()

    if map_inv == {}:
        return create_inventory(list_items)

    for key in map_inv.keys():
        for it in list_items:
            new_inv[key] = map_inv[key]

            new_inv[it] = dir * list_items.count(it) + map_inv[it] if it in map_inv else list_items.count(it)

            if new_inv[it] < 0:
                new_inv[it] = 0
    return new_inv


def decrement_items(inventory, items):
    return add_items(inventory,items,-1)

def remove_item(inventory, item):
    if item in inventory.keys():
        del inventory[item]
    return inventory

def list_inventory(dict_inv):
    new_list = []
    for item in dict_inv.keys():
        if dict_inv[item] > 0:
            new_list.append((item, dict_inv[item]))

    return new_list
