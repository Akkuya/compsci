print("1: Area of Rectangle")
print("2: Area of Circle")
print("3: Area of Ellipse")

choice = int(input("Which option do you want to pick? (1/2/3)"))

if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length*width
    print("The area of the rectangle is", area)
elif choice == 2:
    radius = float(input("Enter the radius: "))
    area = radius**2 * 3.141892654
    print("The area of the circle is", round(area, 2))
elif choice == 3:
    major = float(input("Enter the semi-major length: "))
    minor = float(input("Enter the semi-minor length : "))
    area = major * minor * 3.141592654
    print("The area of the ellipse is", round(area, 2))

