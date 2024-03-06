print("Convert to Base 10")
print("This program will accept a number in a non-base 10")
print("representation, and convert it to its base 10 equivalent.")

base = int(input("Base: "))
number = input("Number: ")

print("Number (denary):", int(number, base))