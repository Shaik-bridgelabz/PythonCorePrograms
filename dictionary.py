# Creating a Dictionary
my_dict = {}  # empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java', 3: 'SQL', 4: 'HTML'}  # dictionary with elements
print(my_dict)

# Changing and Adding Elements into Dictionary
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'C++'  # changing element
print(my_dict)
my_dict['Third'] = 'Ruby'  # adding key-value pair
my_dict['Four'] = '.Net'  # adding key-value pair
print(my_dict)

# Deleting Elements from Dictionary
my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
a = my_dict.pop('Third')  # pop element
print('Value:', a)
print('Dictionary:', my_dict)
b = my_dict.popitem()  # pop the key-value pair
print('Key, value pair:', b)
print('Dictionary', my_dict)
my_dict.clear()  # empty dictionary
print('empty', my_dict)

# Accessing Elements
my_dict = {'First': 'Python', 'Second': 'Java'}
print(my_dict)
print(my_dict['First'])  # access elements using keys
print(my_dict.get('Second'))
