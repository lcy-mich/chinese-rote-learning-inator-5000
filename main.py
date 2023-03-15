from tkinter import Tk, Label, Button, TOP, BOTTOM, messagebox
from sys import path

class main:
    def __init__(self, tk):
        width = int(master.winfo_screenwidth() * .3)
        height = int(master.winfo_screenheight() * .3)
        
        
        self.master = tk
        self.master.title("早上好中国我现在有bing chilling")
        self.master.configure(bg="black")
        self.master.iconbitmap('assets/kanna.ico')
        
        Label(self.master, fg="white", bg="black", text="Incomprehensive Compendium for your common sinophile", font=("Comic Sans MS", int(min(width*.1, height*.1)))).pack(side=TOP)
        Button(self.master, fg="white", bg="black", text="go through all words in order like a weakling 😤", font=('Comic Sans MS', int(min(width*.05, height*.05))), command=self.gothroughall).pack(side=BOTTOM)
        Button(self.master, fg="white", bg="black", text="real strong test for strong people 💪🔥🔥",font=('Comic Sans MS', int(min(width*.05, height*.05))), command=self.opentest).pack(side=BOTTOM)
        
    def opentest(self):
        messagebox.showwarning(title="ha! weak! 🤪", message="word of warning:\nbecause of the library used for speech synthesis,\nit will take some time before window opens")
        path.append('test')
        from test import App
        self.master.destroy()
        newapp = Tk()
        App(newapp)
        newapp.mainloop()
        
    def gothroughall(self):
        messagebox.showwarning(title="ha! weak! 🤪", message="word of warning:\nbecause of the library used for speech synthesis,\nit will take some time before window opens")
        path.append('scroller')
        from scroller import App
        self.master.destroy()
        newapp = Tk()
        App(newapp)
        newapp.mainloop()
        
if __name__ == "__main__":
    master = Tk()
    main(master)
    master.mainloop()