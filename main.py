from tkinter import Tk, Label, Button, TOP, BOTTOM, messagebox
from pinyin import get
from random import choice
from zhtts import TTS
from playsound import playsound
import json

from os import path

class App:

    start_weight = 100

    def __init__(self, master, txt, tts):
        width = int(master.winfo_screenwidth() * .3)
        height = int(master.winfo_screenheight() * .3)

        self.master = master
        self.tts = tts
        
        self.words = dict(zip(map(str,map(self.get_id,txt)), [self.start_weight]*len(txt)))

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.master.title("rote learning chinese since the Xi Dynasty 😻")
        self.master.configure(bg="black")
        self.master.iconbitmap('assets/kanna.ico')
        self.txt = txt

        self.wordscore = Label(self.master, text = 'word score : 0', font=("Comic Sans MS", int(min(width*.05, height*.05))), fg="white", bg="black")

        self.label = Label(self.master, text="rote learning\n-inator 5000", font=("Comic Sans MS", int(min(width*.2, height*.2))), fg="white", bg="black")
        self.label.pack()

        self.next_button = Button(self.master, text="next word", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.next_word)
        self.next_button.pack(side=BOTTOM)
        self.show_button = Button(self.master, text="show word", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.show_word)
        self.play_button = Button(self.master, text="play sound", font=("Comic Sans MS", int(min(width*.1, height*.1))), bg="black", fg="white", command=self.play_sound)

        self.rightbutton = Button(self.master, text="correct", font=("Comic Sans MS", int(min(width*.05, height*.05))), bg='black', fg='green', command=self.right)
        self.wrongbutton = Button(self.master, text="incorrect", font=("Comic Sans MS", int(min(width*.05, height*.05))), bg='black', fg='red', command=self.wrong)

    def get_id(self, word): #literally a bundle of pain
        return ''.join(map(lambda x : x[2:] ,map(hex,(map(ord, list(word.strip()))))))

    def right(self):
        self.words[self.current_word] -= self.start_weight//4
        self.next_word()

    def wrong(self):
        self.words[self.current_word] += self.start_weight//10
        self.next_word()

    def play_sound(self):
        if not hasattr(self,'current_word'):
            return
        id = self.get_id(self.current_word)
        if not path.exists(f'assets/sounds/{id}.wav'):
            self.tts.text2wav(self.current_word, f'assets/sounds/{id}.wav')
        playsound(f'assets/sounds/{id}.wav')
    
    def show_word(self):
        self.label.configure(text=f'      {get(self.current_word)}      \n{self.current_word}')
        self.show_button.pack_forget()
    
    def next_word(self):
        self.wordscore.pack(side=TOP)
        self.rightbutton.pack(side=BOTTOM)
        self.wrongbutton.pack(side=BOTTOM)
        self.play_button.pack(side=BOTTOM)
        self.show_button.pack(side=BOTTOM)
        escapeLoop = False
        while not escapeLoop:
            self.current_word = choice(self.txt).strip()
            if not hasattr(self, 'pastword'):
                escapeLoop = True          
            else:
                if self.pastword != self.current_word:
                    escapeLoop = True
        self.pastword = self.current_word
        
        self.wordscore.configure(text=f'word score : {self.start_weight - self.words[str(self.get_id(self.current_word))]}')
        self.label.configure(text=f'      {get(self.current_word)}      ')
        self.play_sound()
        
    def on_closing(self):
        if messagebox.askokcancel("🤣🤣 clown moment", "Do you want to save before quitting?"):
            with open('assets/saved_scores.txt', encoding='utf-8', mode= 'w') as file:
                file.writelines(json.dumps(self.words))
        root.destroy()

        
if __name__ == "__main__":
    with open('assets/words.txt', encoding="utf-8") as file:
        txt = file.readlines()
    root = Tk()
    app = App(root, txt, TTS())
    root.mainloop()
