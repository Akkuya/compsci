
print("\n#############")
print("THE CHICKENER")
print("#############\n")
print("This program will calculate unit conversions based on perches, as well as calculate chicken tax.\n")


subject = input("Enter the name of the subject: ")
perches = int(input("Enter perches: "))
print()

# -------------  FIRST 85%   ---------------
print("############## FIRST 85% #################\n")

roods = perches // 40
remaining = perches - (roods*40)

print("Roods:", roods, "Remaining Perches:", remaining)

acres = perches // (40 * 4)
remaining = roods - (acres*4)

print("Acres:", acres, "Remaining Roods:", remaining)

square_miles = perches // (40 * 4 * 640)
remaining = acres - (square_miles*640)

print("Square Miles:", square_miles, "Remaining Acres:", remaining)
print()

# -------------  SECOND 10%  ---------------

print("############## NEXT 10% #################\n")
print("The following is the simplest measurement.")


# This is the original amount we keep, to be added in the output statement, as we modify the other variable.
original_amount = perches


# Each of the following blocks calculates the maximum amount of given
# units that can be converted, the subtracts the corresponding amount
# of perches from the total, which is reused for each of the other
# units of area.

# The reason I added the "simple" prefix to these variables is because I wanted to 
# reuse the original roods variable for my last 5%.
simple_square_miles = perches // (40 * 4 * 640)
perches = perches - (simple_square_miles * (40 * 4 * 640))


simple_acres = perches // (40 * 4)
perches = perches - (simple_acres * (40 * 4))


simple_roods = perches // 40
perches = perches - (simple_roods * 40)

print(str(original_amount) + " perches can be converted into:", 
      simple_square_miles, "square miles,", 
      simple_acres, "acres,", 
      simple_roods, "roods and", 
      perches, "perches.")
print()
# -------------   LAST 5%   ----------------

print("############## LAST 5% #################\n")

sections_of_land = roods // 500
tax_rate = 0.5

total_tax = tax_rate * sections_of_land

print(roods, "roods evaluates to",
      sections_of_land, "sections of land, and at 0.5 chickens per section, the total taxed amount is",
      total_tax, "chickens.")

input()