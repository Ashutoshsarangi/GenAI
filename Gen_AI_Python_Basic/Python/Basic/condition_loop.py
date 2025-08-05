some_data = [1,2,3,4,5,6,7,8,9,10]

for item in some_data:
    if item % 2 == 0 and item > 5:
        print(f"{item} is even and greater than 5")
    elif item % 2 == 0:
        print(f"{item} is even")
    else:
        print(f"{item} is odd")