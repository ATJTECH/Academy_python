import tkinter as tk
window= tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("375x200")
    
label1 = tk.Label(window, text="Enter Miles:")
label1.place(x=50,y=30)  
    
label2 = tk.Label(window, text="Kilometers:")
label2.place(x=50,y=100)
   
textbox1 = tk.Entry(window, width=12)
textbox1.place(x=200,y=35)

textbox2= tk.Entry(window, width=12)
textbox2.place(x=200,y=95)
    



def btn1_click():
        kilometers = round(float(textbox1.get()) * 1.60934,5)
        textbox2.insert(0,kilometers)
        
btn1 = tk.Button(window, text="Convert", command=btn1_click)
    
btn1.place(x=90,y=150)
window.mainloop()