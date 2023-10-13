import tkinter

window=tkinter.Tk()
window.title("MY_APPLICATION")
window.minsize(600,500)

def print_name():
   # input_data=input_element.get()
    label2.config(text=input_element.get())
    
input_element=tkinter.Entry()
input_element.pack()

b=tkinter.Button(text="SUBMIT",command=print_name)
b.pack()

label2=tkinter.Label(text=" ")
label2.place(x=100,y=400)

window.mainloop()