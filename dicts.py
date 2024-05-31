def create_inventory(x):
    newdict = dict()
    for item in x:
        newdict[item] = x.count(item)
    return newdict
create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])


def add_items(x,y):
    if x == {}:
        return create_inventory(y)
    for item in list(set(y)):
        x[item] = y.count(item) + x[item] if item in x else y.count(item)
    return x   
add_items({"coal":1}, ["wood", "iron", "coal", "wood"])


def decrement_items(x,y):
    if x == {}:
        return create_inventory(y)
    for item in list(set(y)):
        if item in x:
            x[item] = x[item] - y.count(item)
            if x[item] < 0:
                x[item] = 0
    return x
decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])


def remove_item(x,y):
    if y in x:
        del x[y]
    return x
remove_item({"coal":2, "wood":1, "diamond":2}, "coal")


def list_inventory(x):
    newlist = []
    for key in x.keys():
        if x[key] > 0:
            newlist.append((key, x[key]))
    return newlist
list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
