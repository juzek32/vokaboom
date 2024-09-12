import tkinter as tk
from tkinter import *


#imports a list of german words and their translations
words_file = open("./data/words.txt", "r")
words_str = words_file.read()
words = words_str.split("\n")
for i, item in enumerate(words):
    words[i] = item.split(" ")
    words[i][2] = f"{words[i][2]} {words[i][3]}"
    if len(words[i]) < 6:
        words[i][3] = "-"
        words[i] = words[i][:-1]
    else:
        words[i][3] = f"{words[i][4]} {words[i][5]}"
        words[i] = words[i][:-2]
words_file.close()

root = tk.Tk()
root.title("Vokaboom!")
root.geometry("1000x600")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=5)
root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=3)
root.rowconfigure(4, weight=2)

guess = StringVar()

guess_entry = tk.Entry(root, textvariable=guess)
guess_entry.grid(column=1, row=1)

root.mainloop()