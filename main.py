from tkinter import Tk, Label, Button, TOP, BOTTOM
from pinyin import get
from random import choice
from zhtts import TTS
from playsound import playsound

from os import path

class App:
    def __init__(self, master, txt, tts):
        width = int(master.winfo_screenwidth() * .3)
        height = int(master.winfo_screenheight() * .3)

        self.master = master
        self.tts = tts
        
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.title("rote learning chinese since the Xi Dynasty 😻")
        self.master.configure(bg="black")
        self.master.iconbitmap('assets/kanna.ico')
        self.txt = txt
        self.label = Label(self.master, text="rote learning\n-inator 5000", font=("Comic Sans MS", int(min(width*.2, height*.2))), fg="white", bg="black")
        self.label.pack(side=TOP)

        self.next_button = Button(self.master, text="next word", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.next_word)
        self.next_button.pack(side=BOTTOM)
        self.show_button = Button(self.master, text="show word", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.show_word)
        self.play_button = Button(self.master, text="play sound", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.play_sound)

    def get_id(self, word):
        return ''.join(list(map(str,map(ord, list(word)))))

    def play_sound(self):
        if not self.current_word:
            return
        if not path.exists(f'assets/{self.get_id(self.current_word)}.wav'):
            self.tts.text2wav(self.current_word, f'assets/{self.get_id(self.current_word)}.wav')
        playsound(f'assets/{self.get_id(self.current_word)}.wav')
    
    def show_word(self):
        self.label.configure(text=f'      {get(self.current_word)}      \n{self.current_word}')
        self.show_button.pack_forget()
    
    def next_word(self):
        self.play_button.pack(side=BOTTOM)
        self.show_button.pack(side=BOTTOM)
        self.current_word = choice(self.txt).strip()
        self.label.configure(text=f'      {get(self.current_word)}      ')
        self.play_sound()
        
    def on_closing(self):
        root.destroy()

        
if __name__ == "__main__":
    with open('assets/words.txt', encoding="utf-8") as file:
        txt = file.readlines()
    root = Tk()
    app = App(root, txt, TTS())
    root.mainloop()
