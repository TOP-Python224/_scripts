from sys import argv, platform

print(platform)
for i, arg in enumerate(argv):
    print(f'{i}: {arg}')


