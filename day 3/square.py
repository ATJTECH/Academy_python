#square of num

import tkinter

window=tkinter.Tk()
window.title("App")
window.minsize(600,500)

def print_name():
    input_data=input_element.get()
    num=int(input_data)
    s=num*num
    label2.config(text=s)
    
input_element=tkinter.Entry()
input_element.pack()


b=tkinter.Button(text="SUBMIT",command=print_name)
b.pack()

label1=tkinter.Label(text="Enter the number to be squared")
label1.place(x=0.5,y=0)

label2=tkinter.Label(text=" ")
label2.place(x=300,y=300)

window.mainloop()