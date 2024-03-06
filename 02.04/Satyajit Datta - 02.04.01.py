price_of_item = input()

# Converts the input into a float
price_of_item = float(price_of_item)
tax_rate = 0.13 # Defining our tax rate as 13%


# Defining our final price as the price of the item, + the tax on the price.
final_price = price_of_item + (tax_rate * price_of_item)

print("The final price of the item is $", final_price)