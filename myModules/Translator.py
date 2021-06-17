Dict = {"hello":"привет", 'conundrum':'головоломка',
        'rectangle':'прямоугольник', 'suspect':'подозреваемый'}
def translator(word):
	if word in Dict:
		print(Dict.get(word))
	else:
		print('No words found')

def add_file_words(Dict):
        rus_fh = open('data/russian.txt', 'r')
        eng_fh = open('data/english.txt', 'r')
        rus_words = rus_fh.read().split('\n')
        eng_words = eng_fh.read().split('\n')
        for i in range(len(rus_words)):
                Dict[eng_words[i]] = rus_words[i]
        return Dict
                
Dict = add_file_words(Dict)

def add_word(eng_word, rus_word):
        global Dict
        Dict[eng_word] = rus_word