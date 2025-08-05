file_relative_path = 'Public/text-files/devices.txt'
with open(file_relative_path, 'rt') as f:
    content = f.read().splitlines()[1:] # Skip the header line
    devices = [device.split(':') for device in content]
    
    print(f'{devices}')