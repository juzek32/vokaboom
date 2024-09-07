from PyMultiDictionary import MultiDictionary
dictionary = MultiDictionary()

#imports a list of 3000 most common english words as a list
words_file = open("./../data/words.txt", "r")
words_str = words_file.read()
words = words_str.split("\n")
words_file.close()