from cs50 import get_int

# Get the prompt once first then check if its between 1 nad 8.
while(True):
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break

# Print the pyramid
j = 1
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("#", end="")
    print()