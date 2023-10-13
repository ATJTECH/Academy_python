import tkinter
window=tkinter.Tk()
window.title("App1")
window.minsize(900,500)
label1=tkinter.Label(text="Enter the name")
label1.pack()

'''def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp)'''
    
# TextBox Creation 
inputtxt = tkinter.Text(frame, 
                   height = 5, 
                   width = 20)

# Button Creation 
printButton = tkinter.Button(frame, 
                        text = "Print",  
                        command = printInput) 
    
window.mainloop()