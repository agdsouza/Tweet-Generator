import text_model
import numpy as np

def weighted_values(freq_dict):
	"""
	Helper function: finds probability of each key
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
	Helper function: picks random key based on weights of key
	"""
	dict_word = []
	dict_freq = []
	for word, freq in freq_dict[pair_key].items():
		dict_word.append(word)
		dict_freq.append(freq)
	dict_freq = np.array(dict_freq)
	dict_freq = dict_freq/dict_freq.sum()
	#np.divide(dict_freq, dict_freq.sum(), out=dict_freq)
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


text = "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."
mark_text = MarkovModel(text)
mark_text.create_freq_dict()
freq = mark_text.frequency_dict
prob = mark_text.get_prob_dict()
print(prob)
gen = mark_text.generate_text(1000)
print(gen)