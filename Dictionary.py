def get_keys(dictionary): 
    return list(dictionary.items())

my_dict = {'Pizza': 500, 'Burger': 600, 'Broast': 800, 'Pasta': 550}

items_list = get_keys(my_dict)

print(items_list)