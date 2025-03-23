import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

class PaintApp:

    def __init__(self):
        self.root = tk.Tk()

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.b1 = ttk.Button(self.frame, text = "Pen", command = lambda n = 1 : self.change_type(n))
        self.b2 = ttk.Button(self.frame, text = "Eraser", command = lambda n = 0 : self.change_type(n))
        self.b1.grid(row=0, column = 0)
        self.b2.grid(row = 0, column = 1)
        self.type = True

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        self.width_slider = ttk.Scrollbar(self.frame, command= self.change_width)
        self.width_slider.grid(row = 0, column= 3)
        self.width = 1

        self.b_c = ttk.Button(self.frame, text = "Pick a colour", command = self.change_colour)
        self.b_c.grid(row = 0, column= 4)
        self.colour = "#ffffff"

        self.canvas.bind("<ButtonPress-1>", self.activate)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.root.mainloop()

    def change_colour(self):
        self.colour = askcolor(color = self.colour)[1]
        print(self.colour)

    def change_width(self):
        pass    

    def activate(self, event):
        self.active = True

    def draw(self, event):
        if not self.x and self.y:
            self.x, self.y = event.x, event.y
        
        colour = self.colour if self.type else self.background_colour
        self.canvas.create_line(self.x, self.y, event.x, event.y, width= self.width)
        
        
        self.x, self.y = event.x, event.y

    def reset(self, event):
        self.x = self.y = None
            
    
    def change_type(self, n):
        self.type = n
    



if __name__ == "__main__":
    PaintApp()