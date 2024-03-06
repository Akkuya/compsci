hours_worked = int(input("Enter the amount of hours the employee has worked: "))

regular_hours = 0
overtime_hours = 0

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    regular_hours = hours_worked

hourly_wage = float(input("Enter the hourly wage of the employee: "))
overtime_wage = hourly_wage * 1.5

pay = regular_hours * hourly_wage + overtime_hours * overtime_wage


message = "No Taxes Deducted"

exempt = input("Is the employee exempt from taxes? y/n: ")
if exempt != "y" or exempt != "Y":
    pay *= (1 - 0.18)
    message = "None"

pay = round(pay, 2)

print("Hours worked:", hours_worked, "\tHourly Pay:", hourly_wage, "\tExempt:", exempt)
print("Pay: $", pay, "Message:", message)
