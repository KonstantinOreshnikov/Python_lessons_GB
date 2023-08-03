### Написать функцию выявления уникальных значений из списка ###

def find_dubl(my_list):
    print(list(set([x for x in my_list if my_list.count(x) > 1])))
    return list(set(my_list))

my_list = [2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 5, 6]
print(find_dubl(my_list))
