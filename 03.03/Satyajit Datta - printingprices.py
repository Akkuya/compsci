copies = int(input("Enter the number of copies to be printed: "))

if copies < 500:
    print("Price per copy: $0.30")
    print("Total Price:", 0.3*copies)
elif copies < 750:
    print("Price per copy: $0.28")
    print("Total Price:", 0.28*copies)
elif copies < 1000:
    print("Price per copy: $0.27")
    print("Total Price:", 0.27*copies)
else:
    print("Price per copy: $0.25")
    print("Total Price:", 0.25*copies)