import text_model
import numpy as np

def weighted_values(freq_dict):
	"""
	Finds probability of each key and returns the probability of each word in a dictionary
	"""
	prob_dict = {}
	for d in freq_dict.keys():
		prob_dict[d] = {}
		sum_freq = sum(freq_dict[d].values())
		for k in freq_dict[d].keys():
			prob_dict[d][k] = freq_dict[d][k]/sum_freq
	return prob_dict

def random_key(freq_dict, pair_key):
	"""
	Picks random key based on weights of key and returns that key
	"""
	dict_word = []
	dict_freq = []
	for word, freq in freq_dict[pair_key].items():
		dict_word.append(word)
		dict_freq.append(freq)
	dict_freq = np.array(dict_freq)
	dict_freq = dict_freq/dict_freq.sum()
	return np.random.choice(dict_word, 1, p=dict_freq)[0]

class MarkovModel:
	"""
	Creates instance of a Markov Model object, which contains recorded text of a person 
	and the frequencies of pairs of words
	"""

	text = ""
	frequency_dict = {}

	def __init__(self, text_source):
		self.text = text

	def add_text(self, text):
		"""
		Adds text to model
		text: string containing words of person
		"""
		self.text += text

	def create_freq_dict(self):
		"""
		Returns frequency of word pairs using text from model
		text using function from text_model.py
		"""
		self.frequency_dict = text_model.get_freq(self.text)

	def get_prob_dict(self):
		"""
		Returns a dictionary showing the probablities of each word after
		a word pair
		"""
		return weighted_values(self.frequency_dict)

	def generate_text(self, char_n):
		"""
		Returns Markov chain from frequency dictionary
		"""
		fst = ("$", "$")
		first, second = "$", "$"
		markov = []
		n = 0
		while(n <= char_n):
			# add word to list
			word = random_key(self.frequency_dict, (first, second))
			markov.append(word)
			first, second = second, word
			n += len(word)
		markov = [w for w in markov if w != "$"]
		return ' '.join(markov)
		