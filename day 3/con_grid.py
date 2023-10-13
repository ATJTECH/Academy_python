import tkinter as tk
window= tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("375x200")
    
label1 = tk.Label(window, text="Enter Miles:")
label1.grid(row=0,column=0,padx=5,pady=5) 
    
label2 = tk.Label(window, text="Kilometers:")
label2.grid(row=30,column=0,padx=5,pady=5)
   
textbox1 = tk.Entry(window, width=12)
textbox1.grid(row=0,column=90,padx=5,pady=5)

textbox2= tk.Entry(window, width=12)
textbox2.grid(row=30,column=90,padx=5,pady=5)
    



def btn1_click():
        kilometers = round(float(textbox1.get()) * 1.60934,2)
        textbox2.insert(0,kilometers)
        
btn1 = tk.Button(window, text="Convert", command=btn1_click)
    
btn1.grid(row=15,column=120,padx=5,pady=5)
window.mainloop()
