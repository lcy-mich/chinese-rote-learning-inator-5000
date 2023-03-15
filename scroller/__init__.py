from tkinter import Tk, Label, Button, BOTTOM, TOP
from pinyin import get
from zhtts import TTS
from playsound import playsound

from os import path

class App:

    next_word_key = "<space>"
    show_button_key = "s"
    play_button_key = "a"

    def __init__(self, master):
        self.width = int(master.winfo_screenwidth() * .3)
        self.height = int(master.winfo_screenheight() * .3)

        self.master = master
        self.master.bind(self.next_word_key, lambda x: self.next_word())

        with open('assets/words.txt', encoding="utf-8") as file:
            self.txt = file.readlines()        
            
        self.master.title("cowardly revision since the Xi Dynasty 😤")
        self.master.configure(bg="black")
        self.master.iconbitmap('assets/kanna.ico')
        
        self.tts = TTS()

        self.label = Label(self.master, text="scrolling revision 🔥\nstraight up just checks everything", font=("SimSun", int(min(self.width*.2, self.height*.2))), fg="white", bg="black")
        self.label.pack(side=TOP)

        self.next_button = Button(self.master, text=f"next word {self.next_word_key}", font=("Comic Sans MS", int(min(self.width*.1, self.height*.1))), bg="black", fg="white", command=self.next_word)
        
        self.next_button.pack(side=BOTTOM)
        
        self.show_button = Button(self.master, text=f"show word <{self.show_button_key}>", font=("Comic Sans MS", int(min(self.width*.1, self.height*.1))), bg="black", fg="white", command=self.show_word)
        
        self.play_button = Button(self.master, text=f"play sound <{self.play_button_key}>", font=("Comic Sans MS", int(min(self.width*.1, self.height*.1))), bg="black", fg="white", command=self.play_sound)

    def get_id(self, word): #literally a bundle of pain
        return ''.join(map(lambda x : x[2:] ,map(hex,(map(ord, list(word.strip()))))))

    def play_sound(self):
        if not hasattr(self,'current_index'):
            return
        id = self.get_id(self.txt[self.current_index])
        if not path.exists(f'assets/sounds/{id}.wav'):
            self.tts.text2wav(self.txt[self.current_index], f'assets/sounds/{id}.wav')
        playsound(f'assets/sounds/{id}.wav')
    
    def show_word(self):
        self.label.configure(text=f'{get(self.txt[self.current_index])}\n{self.txt[self.current_index]}')
        self.show_button.pack_forget()
    
    def next_word(self):
        self.play_button.pack(side=BOTTOM)
        self.show_button.pack(side=BOTTOM)

        self.master.bind(self.show_button_key, lambda x: self.show_word())
        self.master.bind(self.play_button_key, lambda x: self.play_sound())
        
        if not hasattr(self,'current_index') or self.current_index >= len(self.txt):
            self.current_index = -1
        
        self.current_index +=1
        
        self.label.configure(text=f'{get(self.txt[self.current_index])}',font=("SimSun", int(min(self.width*.4, self.height*.4))))
        self.play_sound()
        
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
