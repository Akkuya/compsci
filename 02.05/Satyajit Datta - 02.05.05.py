x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))


y_intercept = (x2*y1 - x1*y2)/(x2-x1)

print("The y-intercept is ( 0 ,", y_intercept,").")