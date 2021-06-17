#program to hold dictionary of words in english

''' I'd like to check the text file and to write a new word there using
this program'''
class engDict(dict):
    def __init__(self, 
try:
    file = open(new_english_words.docx)
    dictionary = set()
    for line in file.read():
        english_word = line.split(':')[1]
        russian_word = line.split(':')[2]
        dictionary.add(english_word)
        
except FileError:

except FileError...
        

