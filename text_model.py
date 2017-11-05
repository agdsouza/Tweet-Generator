import re

def separate_text(text):
	"""
	Returns all words in a string as a list of words
	input: text, a string
	"""
	tokenized_list = re.findall(r"[\S]+|[;:()]", text)
	return [words for words in tokenized_list if words not in ";:()[]{}"]

def start_marks(text_list):
	"""
	Returns text list, with a "beginning sentence marker" between the start and end
	of a sentence (which will be $ in this case)
	"""
	text = ["$", "$"] + text_list
	mark_text = []
	for i in range(len(text_list)):
		mark_text.append(text[i])
		if i + 1 != len(text_list) and text[i][-1] in ".!?":
			mark_text.append("$")
			mark_text.append("$")

	return mark_text

def make_triple(words):
	""" 
	Returns every word in a list as a triple with the next two words 
	succeeding it
	input: words, a list of strings
	"""
	triple = []
	for i in range(len(words)):
		if len(words[i:]) < 3:
			break
		else:
			triple.append((words[i], words[i+1], words[i+2]))

	return triple

def form_tuple(word_triples):
	"""
	Returns the first two words in a triple as a key, and the last word
	as a value
	input: word_triples, a list of 3 element tuples
	"""
	return [((w1, w2), w3) for (w1, w2, w3) in word_triples]

def get_freq(text):
	"""
	Returns every key value pair with a value of 1 to count one of each
	pair (to prepare for reducing/aggregating)
	input: triples, a list of key-value pairs where the key is a pair of
		   words, and the value is the word that succeeds the pair 
	"""

	cleaned_text = start_marks(separate_text(text))
	triples = form_tuple(make_triple(cleaned_text))
	trip_freq = {} #final list of all the frequencies

	for k, v in triples:
		if k not in trip_freq:
			trip_freq[k] = {v: 1}
		else:
			if v not in trip_freq[k]:
				trip_freq[k][v] = 1
			else:
				trip_freq[k][v] += 1

	return trip_freq