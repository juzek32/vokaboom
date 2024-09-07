from ui import *


#imports a list of german words and their translations
words_file = open("./../data/words.txt", "r")
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

