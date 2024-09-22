s = int(input('Enter the size of the pattern: '))

i = 0
while i < s:
    j = 0
    while j < s:
        print('*', end="")
        j += 1
    print()
    i += 1
