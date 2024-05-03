import tkinter

window = tkinter.Tk()
window.geometry("600x600") 
canvas = tkinter.Canvas(window, width=600, height=600)


ellipse1 = canvas.create_oval(0, 0, 50, 50, fill="blue")
ellipse2 = canvas.create_oval(150, 70, 400, 500, fill="red")
ellipse3 = canvas.create_oval(450, 10, 550, 90, width=2)
ellipse4 = canvas.create_oval(450, 300, 550, 500, fill="Green")





canvas.pack()
window.mainloop()