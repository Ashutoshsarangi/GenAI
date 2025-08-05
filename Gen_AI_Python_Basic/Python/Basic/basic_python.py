import numpy as np

random_num = np.random.rand(10)
print("Random number generated:", random_num)

#variable Example

age, name = 25, 'Ashutosh'
print(age, name)


# PEP 8 -> guideline for proper naming convention in Python
# https://peps.python.org/pep-0008/

#List:- Ordered, Mutable, Allows duplicates
person = ['Ashutosh', 25, 'India']
# Dictionary:- Unordered, Mutable, No duplicates
person_dict = {'name': 'Ashutosh', 'age': 25, 'country': 'India'}
# Tuple:- Ordered, Immutable, Allows duplicates (Can't be changed)
person_tuple = ('Ashutosh', 25, 'India')
# Set:- Unordered, Mutable, No duplicates
person_set = {'Ashutosh', 25, 'India'}
#Frozenset:- Unordered, Immutable, No duplicates (Immutable Set)
person_frozenset = frozenset({'Ashutosh', 25, 'India'})

#Operators

print(8 / 2, 8 // 2)

#Mutability vs Immutability
a = 2
print('Id of a --> ', id(a))

a = 3
print('Address will change of a --> ', id(a))

num_list = [1,2,3]
print('Address of list --> ', id(num_list));

num_list.append(10);

print('Address of updated num_list --> ', id(num_list));
