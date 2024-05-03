import tkinter

window = tkinter.Tk()
window.geometry("600x600") 
canvas = tkinter.Canvas(window, width=600, height=600)


rectangle1 = canvas.create_rectangle(0, 0, 50, 50, fill="blue")
rectangle2 = canvas.create_rectangle(150, 70, 400, 500, fill="red")
rectangle3 = canvas.create_rectangle(450, 10, 550, 90, width=2)
rectangle4 = canvas.create_rectangle(450, 300, 550, 500, fill="Green")





canvas.pack()
window.mainloop()