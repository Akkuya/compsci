type_of_shape = input("Area of rectangle or volume of rectangular prism? A/V: ")

if type_of_shape == "A":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    print("The area of the rectangle is:", round(length*width, 2))
if type_of_shape == "V":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    height = float(input("Enter the height: "))


    print("The volume of the rectangular prism is:", round(length*width*height, 2))
    
