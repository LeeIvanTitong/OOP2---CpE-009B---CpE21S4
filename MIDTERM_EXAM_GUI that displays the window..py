from tkinter import *

class MyWindow:
    
    def __init__(self, window):
        self.label1 = Label(window, fg="red", text="Enter your fullname:")
        self.label1.place(x=20, y=50)
        
        self.entry1 = Entry(window, bd=2)
        self.entry1.place(x=220, y=50)
        
        self.button = Button(window, fg="red", text="Click to display your Fullname", command=self.display)
        self.button.place(x=20, y=100)
    
        
        self.entry2 = Entry(window, bd=2)
        self.entry2.place(x=220, y=100)
        
    def display(self):
        self.entry2.delete(0, "end")
        self.entry2.insert(END, self.entry1.get())
        
window = Tk()
MyWin = MyWindow(window)
window.title("Midterm Exam in OOP")
window.geometry("400x200+50+50")
window.mainloop()