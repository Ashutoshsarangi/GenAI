#---------------------------------------SET--------------------------------------------
# We can't access set via index, but we can check if an element is present in the set
# Only way to create empty set is by using set() constructor

my_set = {1, 2, 3, 4, 5}

print(f'type of {type({})=}')

var1, var2 = [1, 2, 3], {1, 2, 3}
print(var1 == [2, 3, 1], var2 == {2, 3, 1}) #False True
# [2, 3, 1] is not equal to [1, 2, 3] as list order matters, while {2, 3, 1} is equal to {1, 2, 3} 
# because sets are unordered collections where the order of elements does not matter.

# Which data structure has the fastest lookup time?
# "set," is correct because sets in Python are implemented as hash tables, which provide efficient O(1) average-time complexity for lookups

# NOTE:-
# We can't add List into set, because it is mutable, we can add tuple into set, because it is immutable

#Set Comprehension
names = {'Alice', 'Bob', 'Charlie'}
formated_names = {name.upper() for name in names}
print(formated_names)  # {'ALICE', 'BOB', 'CHARLIE'}
#---------------------------------------DICTIONARY---------------------------------------------

# we can add tuple as a key in dictionary, but we can't add list as a key in dictionary
dict_demo = {
    (1, 2): 'tuple',
    1: 'int',
    1.0: 'float',
    '1': 'string',
    True: 'bool'
}
print(dict_demo)

#Dictionary merge (|) and Update (|=) operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3_merge = dict1 | dict2
print(dict3_merge)  # {'a': 1, 'b': 3, 'c': 4}
dict1 |= dict2 #directly update in dict1
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# Dictionary comprehension
# Create a dictionary with keys as numbers from 1 to 5 and values as their squares
params = {'layers': 3, 'units': 256,}
adjusted_params = {k: v * 2 for k, v in params.items()}
print(adjusted_params)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# Dictionary comprehension with condition
# Create a dictionary with keys as numbers from 1 to 10 and values as their squares, but only for even numbers
adjusted_params_conditions = {key: key.upper() for key, value in params.items() if value > 2}
print(adjusted_params_conditions)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

zip()
# Zipping two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print(zipped_dict)  # {'a': 1, 'b': 2, 'c': 3}
# Unzipping a dictionary into two lists
zipped_keys, zipped_values = zip(*zipped_dict.items())
print(zipped_keys)  # ('a', 'b', 'c')
print(zipped_values)  # (1, 2, 3)

#profit calculation
sales = {2022: 1000, 2023: 1500, 2024: 2000}
profit = {year: amount + amount*0.15 for year, amount in sales.items()}

print(profit)  # {2022: 150.0, 2023: 225.0, 2024: 300.0}

sample_dict = {
    'Alice': 25,
    'Bob': 30,
    'Charlie': 22,
    'Diana': 28
}

print(sample_dict)

# Sorting the dictionary by keys
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
# Sorting the dictionary by values
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

#maximum by key & Value

older_person_by_age = max(sample_dict, key=sample_dict.get)
print(f'Older person by age: {older_person_by_age}')
#maximum by key
older_person_by_key = max(sample_dict)
#maximum by key length
older_person_by_name = max(sample_dict, key=lambda x: len(x))
print(f'Older person by name: {older_person_by_name}')