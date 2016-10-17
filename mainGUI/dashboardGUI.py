import Tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        
def main ():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
