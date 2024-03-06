number = int(input("Enter the 4 digit number."))

ones = number % 10
number = number // 10

tens = number % 10
number = number // 10

hundreds = number % 10
number = number // 10

thousands = number % 10

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)
print("Thousands:", thousands)