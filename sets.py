# Creating a set
my_set = {1, 2, 3, 4, 5, 5, 5}  # create set
print(my_set)

# Adding Elements
my_set = {1, 2, 3}
my_set.add(4)  # add element to set
my_set.add(8)
print(my_set)

# Operation in Sets
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)
