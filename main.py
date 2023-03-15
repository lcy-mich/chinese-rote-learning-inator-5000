from tkinter import Tk, Label, Button, TOP

class main:
    def __init__(self, tk):
        self.master = tk
        self.master.title("早上好中国我现在有bing chilling")
        self.master.configure(bg="black")
        
        Label(self.master, fg="white", bg="black", text="Incomprehensive Compendium for your common sinophile", font=("Comic Sans MS", 25)).pack(side=TOP)

if __name__ == "__main__":
    master = Tk()
    main(master)
    master.mainloop()