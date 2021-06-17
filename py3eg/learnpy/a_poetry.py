import random
import sys
articles = ['the ', 'a ', 'an ', '']
nouns = ['cat ','dog ','pig ','ring ','man ',
         'woman ','mouse ','rain ','train ']
verbs = ['sang ','ran ','jumped ','picked ','beat ','suck ','wrote ']
adverbs = ['loundly ','quietly ','well ','badly ',
           'rightly ','lightly ','brightly ','lonely ']
article = noun = verb = adverb = ''
def poetry(n):
    for i in range(n):
            article = random.choice(articles)
            noun = random.choice(nouns)
            verb = random.choice(verbs)
            adverb = random.choice(adverbs)
            struct = random.randint(0,1)
            if struct == 0:
                print(article+noun+verb+adverb)
            else:
                print(article+noun+verb)
try:
    if len(sys.argv)==1:
        poetry(5)
    elif 1 <= int(sys.argv[1]) <= 10:
        poetry(int(sys.argv[1]))
    else:
        print('please, reenter')
except ValueError as err:
    print(err)
