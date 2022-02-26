# create a dictionary program,to define words

import  json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        reply = input("enter y for yes or n for no")
        if reply == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif reply == "n":
            return("Word not found")
        else:
            return("Invalid input")
    else:
        print("Word does not exists")

word = input("Which word do you want to search?")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
