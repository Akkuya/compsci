grade = input("Enter a letter grade: ")
if grade == "A":
    print("A\t80-100")
elif grade == "B":
    print("B\t70-79")
elif grade == "C":
    print("C\t60-69")
elif grade == "D":
    print("D\t50-59")
elif grade == "E":
    print("E\t0-49")
else:
    print("Invalid letter grade.")