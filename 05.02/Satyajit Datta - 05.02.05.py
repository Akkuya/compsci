n = int(input("Enter number of terms: "))
term = float(input("Enter term: "))
count = 0
sum = 0
while count < n:
    sum += (term ** count)
    count += 1
print(sum)