import tkinter
window=tkinter.Tk()
window.title("App1")
window.minsize(900,500)
label1=tkinter.Label(text="Enter the name")
label1.grid(row=15,column=30)

button3=tkinter.Button(text="button3")
button3.grid(row=9,column=9)
window.mainloop()
