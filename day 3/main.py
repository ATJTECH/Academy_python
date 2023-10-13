import tkinter
#creates gui

window=tkinter.Tk()#Tk class of tkinder,here window is created;inshort time span window opened and closed
#code b/t Tk() and mainloop()
window.title("App")#title of window
#window width to 900
window.minsize(900,500)#(width,height)
#Event loop-monitors all activities(mouse click etc)


label1=tkinter.Label(text="Application")#(keyword=)this fn accepts only keyword argument
#layout manager-pack()-helps to put something on window
label1.pack()

label2=tkinter.Label(text="Application program",font=('Times New Roman',24))#font
#label2.pack(side='right')#positioning of label

#grid,place

label3=tkinter.Label(text="Application program",font=('Times New Roman',15))
label3.place(x=20,y=40)#x and y axis specified
#Button creation
B=tkinter.Button(text ="click here")
B.place(x=100,y=150)

def printing():
    print("clicked")

#prompt while clicking button
B1=tkinter.Button(text ="click here",command=printing)#command=printing-on clicking the respective fn will be called and run 
B1.place(x=100,y=150)

#changing label texts
label1["text"]="Hey"
label1.config(text="Hello")

def changing_label():
    label1.config(text="changed on clicking")
    
    
B2=tkinter.Button(text ="click here to change label",command=changing_label)#command=printing-on clicking the respective fn will be called and run 
B2.place(x=150,y=200)

window.mainloop()#to make window visible;keeps the window running

