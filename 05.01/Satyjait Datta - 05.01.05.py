n= int(input("Enter a number: "))

for i in range(1, n+1):
    print(i**2)

print()

for i in range(n+1):
    for j in range(1, i+1):
        if (i/j)**2 == i:
            print(i/j)
            