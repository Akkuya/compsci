import tkinter

print("Welcome to the Typer")
print("The two items that will be in stock will be apples and oranges.")
print("Input a negative number in the quantity section, to terminate the program.")

running = True

apples1 = 0
apples2 = 0
oranges1 = 0
oranges2 = 0

characteristic1 = input("Enter the first characteristic.  ")
characteristic2 = input("Enter the second characteristic.  ")

total = 0

while running:
    apple = input("Apple (Y/N): ")
    orange = input("Orange (Y/N): ")
    
    c1 = input(characteristic1 + ": (Y/N): ")
    c2 = input(characteristic2 + ": (Y/N): ")
    print()
    quantity = int(input("Quantity: "))
    print()
    if quantity <=0:
        running = False
        continue

    if apple == "Y":
        if c1 == "Y":
            apples1 += quantity
        elif c2 == "Y":
            apples2 += quantity
    if orange == "Y":
        if c1 == "Y":
            oranges1 += quantity
        elif c2 == "Y":
            oranges2 += quantity

    total += quantity


apples1_floor =  (apples1/total*100 // 10) * 10
apples2_floor =  (apples2/total*100 // 10) * 10

oranges1_floor =  (oranges1/total*100 // 10) * 10
oranges2_floor =  (oranges2/total*100 // 10) * 10




print("Apples/" + characteristic1 + ": " + str(apples1) + ";", str(apples1_floor) + "%")
print("Apples/" + characteristic2 + ": " + str(apples2)+ ";", str(apples2_floor) + "%")

print("Oranges/" + characteristic1 + ": " + str(oranges1)+ ";", str(oranges1_floor) + "%")
print("Oranges/" + characteristic2 + ": " + str(oranges2)+ ";", str(oranges2_floor) + "%")


window = tkinter.Tk()
window.geometry("600x600")  #You enter the window dimensions for nnn
                            #the "x" must be small letter


canvas = tkinter.Canvas(window, width=600, height=600)
                            

x_axis = canvas.create_line(10,590,590,590)
y_axis = canvas.create_line(10,10,10,590)

max_height = 580

bar1 = canvas.create_rectangle(30, 590, 150, 590-(580*apples1/total), fill = 'red')
bar2 = canvas.create_rectangle(170, 590, 290, 590-(580*apples2/total), fill = 'orange')

bar3 = canvas.create_rectangle(310, 590, 430, 590-(580*oranges1/total), fill = 'blue')
bar4 = canvas.create_rectangle(450, 590, 570, 590-(580*oranges2/total), fill = 'green')

text1 = canvas.create_text(70, 100, text=("Apples, " + str(characteristic1)))
text2 = canvas.create_text(210, 100, text=("Apples, " + str(characteristic2)))
text3 = canvas.create_text(350, 100, text=("Oranges, " + str(characteristic1)))
text4 = canvas.create_text(490, 100, text=("Oranges, " + str(characteristic2)))



#Code for creating graphical shapes


#Flips the shapes from memory onto the monitor
canvas.pack()


window.mainloop()