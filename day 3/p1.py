import tkinter as tk

# Top level window 
frame = tk.Tk() 
frame.title("TextBox Input") 
frame.geometry('400x200') 
# Function for getting Input 
# from textbox and printing it 
# at label widget 

def printInput(): 
	inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp)
	
label1=tk.Label(text="Enter the name")
label1.pack()
label1.place(x=0.5,y=1)
# TextBox Creation 
inputtxt = tk.Text(frame, 
				height = 5, 
				width = 20) 

inputtxt.pack() 

# Button Creation 
printButton = tk.Button(frame, 
						text = "submit", 
						command = printInput) 
printButton.pack() 

# Label Creation 
lbl = tk.Label(frame, text = "") 
lbl.pack() 
frame.mainloop() 
