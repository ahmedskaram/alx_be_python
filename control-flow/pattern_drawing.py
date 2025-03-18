############################################################################

# Use a while loop for rows and a for loop for columns to print a square of stars
size = int(input("Enter the size of the pattern: "))
i = 0

while i < size:
    
    for j in range(1, size + 1):
        print("*", end="")
    
    print()
    i += 1

############################################################################

# Use nested while loops to create a square pattern of stars

size = int(input("Enter the size of the pattern: "))

i = 1
while i <= size:

    j = 0
    while j <= size:
        print('*', end="")
        j += 1
    
    print()
    i += 1

############################################################################

# Use nested for loops to generate a square star pattern

size = int(input("Enter the size of the pattern: "))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print("*", end="")
    print()

############################################################################