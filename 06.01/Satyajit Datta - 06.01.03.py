import tkinter

window = tkinter.Tk()
window.geometry("600x600") 
canvas = tkinter.Canvas(window, width=600, height=600)


head = canvas.create_oval(250, 150, 350, 250, fill="beige")
body = canvas.create_rectangle(280, 250, 320, 450)
arm = canvas.create_line(280, 280, 220, 190) 
arm = canvas.create_line(320, 280, 390, 190)
leg = canvas.create_line(280, 420, 220, 550) 
leg = canvas.create_line(320, 420, 390, 550)  



canvas.pack()
window.mainloop()