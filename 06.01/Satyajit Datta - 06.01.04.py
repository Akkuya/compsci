import tkinter

window = tkinter.Tk()
window.geometry("800x800") 
canvas = tkinter.Canvas(window, width=800, height=800)

num = int(input("Enter grid size: "))

width = 800/num

# for i in range(0,num, 2):

#     # for j in range(num)


# canvas.pack()
# window.mainloop()