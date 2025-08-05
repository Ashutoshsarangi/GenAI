with open('Public/text-files/setting.txt', 'rt') as f:
    content = f.read()
    print(content)

print(f'Is file closed ? --> {f.closed}')

