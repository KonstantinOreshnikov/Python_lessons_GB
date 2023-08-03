### Определить что влезет в рюкзак из списка вещей ###

def bag_capacity(items, max_weight):
    in_bag_now = []
    for item, weight in items.items():
        if weight <= max_weight:
            in_bag_now.append(item)
            max_weight -= weight
    return in_bag_now

items = {'вода': 3, 'еда': 4, 'аптечка': 1,'одежда': 2, 'фонарик': 2, 'спальный мешок': 5}
max_weight = 10
print(bag_capacity(items, max_weight))