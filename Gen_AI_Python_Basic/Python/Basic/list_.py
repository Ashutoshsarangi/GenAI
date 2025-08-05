l1 = [1,2,3,4]
l1.extend([5,6,7])
print(l1) # [1, 2, 3, 4, 5, 6, 7]
l1.append([8,9])
print(l1) # [1, 2, 3, 4, 5, 6, 7, [8, 9]]

l1 = list('xyz') #['x', 'y', 'z']
print(l1 * 3)
# ['x', 'y', 'z', 'x', 'y', 'z', 'x', 'y', 'z']

#iterate over a list
ip_list = ['1.1.1', '2.2.2', '3.3.3']
for ip in ip_list:
    print(f'IP Address, connecting: {ip} ...')

#List Gotchas
l1.copy() # shallow copy
# while doing iteration in list it is not a good idea to modify the list, 
# so we can create a list [] and append based on condition

l1 = [1,2,3,4, 1, 1,2, 2]
while 1 in l1:
    l1.remove(1)
print(l1) # [2, 3, 4]
print(f'Total no of 1 present {l1.count(2)}') # 0

l1.sort() # sort the list in place
l1.sort(reverse=True) # sort the list in place
l2 = sorted(l1) # return a new sorted list

# List Comprehension
clicks = [1, 2, 3, 4, 5]
double_clicks = []
for i in clicks:
    double_clicks.append(i * 2)
double_clicks = [i * 2 for i in clicks]
print(double_clicks) # [2, 4, 6, 8, 10]
# List Comprehension with condition
clicks = [1, 2, 3, 4, 5]
double_clicks_condition = []
for i in clicks:
    if i % 2 == 0:
        double_clicks_condition.append(i * 2)
double_clicks_condition = [i * 2 for i in clicks if i % 2 == 0]
print(double_clicks_condition) # [4, 8]
# List Comprehension with condition and nested loops
clicks = [1, 2, 3, 4, 5]
double_clicks_condition_nested = []
for i in clicks:
    for j in clicks:
        double_clicks_condition_nested.append(i * j)
double_clicks_condition_nested = [i * j for i in clicks for j in clicks]
print(double_clicks_condition_nested) # [1, 2, 3, 4, 5, 2, 4, 6, 8, 10, 3, 6, 9, 12, 15]