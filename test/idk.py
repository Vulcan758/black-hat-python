from sys import argv

for arg in argv:
    print(arg)

print(bool(len(argv[1:])))