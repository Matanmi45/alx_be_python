pattern = int(input("Enter the size of the pattern: "))
num = 1

while num <= pattern:
     for i in range(pattern):
        print("*", end="")
     print()
     num = num + 1


