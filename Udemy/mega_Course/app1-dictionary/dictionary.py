import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json",'r'))

search_word = input("Enter the word you want to know the meaning of: ")
search_word = search_word.lower()

def translate(word):
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	else:
		suggest = get_close_matches(word,data.keys(),cutoff=0.8)
		if  len(suggest) > 0:
			for item in suggest:
				choice = input("Did you mean %s. Press Y for YES and N for NO: " %item)
				if choice == 'y' or choice == 'Y':
					return data[item]
			return "Couldn't find any similar words"
		
		else:
			return "The word doesn't exist. Please Enter valid input"
		


print('\n'.join(translate(search_word)))
