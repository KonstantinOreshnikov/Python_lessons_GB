###  Изменить словарь  на типа: ключ - значение на значение - ключ  ###

my_dict = {'cat': 5, 'dog': 7, 'elephant': 20, 'rabbit': 3, 10: 'ten'}

def rev_dict():
    return {value : key for key, value in my_dict.items()}

print(my_dict)
print(rev_dict())