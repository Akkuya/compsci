first_number = -3.4
second_number = -5.6
third_number = 88.95
fourth_number = 1056

print()
print("THE MATHIFIER")
print("A short program applying different operations to numbers.")
print()


########################### FIRST 85% ###########################

print("############ FIRST 85% ###############\n")


solution = first_number
print(solution, "/", second_number, "=", solution/second_number)
solution = solution/second_number

print(solution, "-", third_number, "=", solution-third_number)
solution = solution-third_number

print(solution, "*", third_number, "=", solution*third_number)
solution = solution*third_number

print("\nThe final solution is", solution, "degrees celsius\n")




####################### NEXT ADDITIONAL 10% #######################

print("############ NEXT 10% ###############\n")

base = first_number * second_number

print("The base will be num1 * num2, which evalutates to the following: ")
print(first_number, "*", second_number, "=", base)

print('The exponent will be the third number:', third_number)

solution = base ** third_number

print()
print(str(base) + "^" + str(third_number) + "=" + str(solution))
print()



####################### FINAL 5% #######################


print("############ FINAL 5% ###############\n")

# Converting all negative values to positive
first_number = first_number/-1
second_number = second_number/-1

gravitational_constant = first_number
mass_1 = second_number
mass_2 = third_number
distance = fourth_number

force = gravitational_constant * ((mass_1 * mass_2) / (distance ** 2))

print("The force is", force, "newtons.")



input()