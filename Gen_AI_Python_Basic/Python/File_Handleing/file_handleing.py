f = open('Public/text-files/setting.txt', 'rt')
content = f.read(5);

print(content)

content_2 = f.read(3)
print(content_2)

print(f.tell()) #It will say where is my current cursor in the opened file --> 8

f.seek(2) #Moving cursor to 2nd position

f.close()

print('#' * 50)

f_configure = open('Public/text-files/configure.txt', 'rt');

print(f_configure.read())


print('*' * 50)
f_configure.seek(0) # after 1st reed cursor position was at the end so I moved the cursor to 0
#before I read next time

print(f_configure.read())

f_configure.close()