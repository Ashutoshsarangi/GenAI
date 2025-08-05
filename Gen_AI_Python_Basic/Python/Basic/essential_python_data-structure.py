# Getting user input

total_hour_training = int(input('Enter Hours of Training : ')) # It will always return string
print ('Total Hours of Training after multiply 2: ', total_hour_training * 2);


# String indexing slicing and concatenating

# String are immutable in python
s = 'hello'
new_str = 'H' + s[1:len(s)]
print('new Str --> ', new_str)

print('version : ' + str(4.0))

#Sliceing string[start:end:step]
s = '0123456789'
print(s[::2]) # 02468
print(s[1::2]) # 13579
print(s[::-1]) # 9876543210, Reverse a String

r = 13.2
PI = 3.14

print(f'The Area of circle {r=} is {PI * r ** 2=:.4f} doing calculation here')
area = PI * r ** 2
print(f'The Area of circle {r=} is {area=:.4f} doing calculation here')
# f{=} is very good for debugging as well. 