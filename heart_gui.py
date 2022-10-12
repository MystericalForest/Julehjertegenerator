import tkinter as tk
import tkinter.messagebox as msg
import christmas_heart

win=tk.Tk() #creating the main window and storing the window object in 'win'
win.title('SVG Heart Generator') #setting title of the window
win.geometry('500x200') #setting the size of the window

def generate():#function of the button
    width=int(ent1.get())
    no_of_strains=int(ent2.get())
    gap_width=int(ent3.get())
    filename=ent4.get()
    heart=christmas_heart.BraidedChristmasHeart(width, no_of_strains, gap_width=gap_width)
    heart.generate(filename)
    msg.showinfo("File generated","The file " + filename+ " is generated")

btn=tk.Button(win,text="Generate file", width=10,height=1,command=generate)
btn.place(x=350,y=30)

tk.Label(win, text='Width of the heart').grid(row=0, column=0) 
tk.Label(win, text='No of strains').grid(row=1, column=0)  
tk.Label(win, text='Gap width').grid(row=2, column=0)  
tk.Label(win, text='File name').grid(row=3, column=0) 
ent1 = tk.Entry(win)
ent1.insert(0, "100") 
ent2 = tk.Entry(win)
ent2.insert(0, "4") 
ent3 = tk.Entry(win)
ent3.insert(0, "3")  
ent4 = tk.Entry(win)
ent4.insert(0, "output\\heart.svg")  
ent1.grid(row=0, column=1) 
ent2.grid(row=1, column=1) 
ent3.grid(row=2, column=1) 
ent4.grid(row=3, column=1) 
tk.Label(win, text='mm').grid(row=0, column=2) 
tk.Label(win, text='mm').grid(row=2, column=2) 

win.mainloop()
