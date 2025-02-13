import json
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
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "
                                    % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word dosn't exist. Please double check it."
        else:
            return "I didn't understand the entry!!!"
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")

output = translate(word)

if type(output) == str:
    print(output)
else:
    for item in output:
        print(item)
