def trying_new_fun(a, b):
    '''
        docstring is good in side the function

        PEP 257
    '''
    print("Trying new function")
    x = 10
    print(x ** 2)
    print(a + b)
    
trying_new_fun(10, 20)

#by default function return None

def empty_function():
    pass

# important *args(tuple) and **kwargs(dict)

# packing and unpacking dict

#Packing
def user_info(**user_data):
    print(f'user information is {user_data}')


user_info(name = 'Ashu', age = 30, college = 'NIST')

#unpacking 
obj_1 = {'name': 'Ashu', 'age': 20, 'college': 'NIST'}
obj_2 = {'param': 'xyz', 'age': 30}
obj_3 = {**obj_1, **obj_2}

print(f'Unpacked {obj_3=}')


# NAMESPACE

# 1. Built in Namespace
print(max([1,2,3,4]))

# 2. global Name Space 

accuracy = 23
def fun_check():
    print(accuracy)

# 3. Local name Space 

def fun_check2(text):
    token = len(text.split())
    print(token)

# Python checks LEGB rule

# 1. Local scope
# 2. Enclose scope
# 3. Global scope
# 4. built in scope


# Lambda Expression (Anonymous Function)

# Syntax

# lambda paramters: expressions

square = lambda x: x ** 2

print(square(4))