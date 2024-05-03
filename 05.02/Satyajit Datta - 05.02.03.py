nums = 0
sum = 0

while True:
    number = int(input("Enter number"))
    if number == 0:
        break
    sum += number
    nums += 1
print(sum/nums)