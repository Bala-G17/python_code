import json
from difflib import get_close_matches

data = json.load(open('data.json'))
def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ans = input("did you mean %s enter y if yes or enter n if no: " % get_close_matches(word,data.keys())[0])
        if ans == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return 'please double check the word'       
    else:
        return "sorry, the word dose not exit."
word =input('enter the word: ')
output = dictionary(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

    









