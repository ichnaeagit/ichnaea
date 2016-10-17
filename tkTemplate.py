import Tkinter as tk

class mainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.master.title("Template name")
        # self.navbar = navbar(self,....) << extra classes
        self.parent = parent
 

        # Rest of GUI here

# class navbar(tk.Frame):.... << Extra classes for diff sections
        
if __name__ == '__main__':
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()
