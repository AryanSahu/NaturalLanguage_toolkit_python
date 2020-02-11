import nltk
import matplotlib.pyplot as plt

# nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

text = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text = sent_tokenize(text)
print(tokenized_text)

tokenized_word = word_tokenize(text)
print(tokenized_word)

fdist = nltk.FreqDist(tokenized_word)
print(fdist)

fdist.most_common(2)

# fdist.plot(30, cumulative=False)
# plt.show()


stop_words = set(stopwords.words("english"))
print(stop_words)

ps = PorterStemmer()
stemmed_words=[]



def filtered_sent(w):
    stemmed_words.append(ps.stem(w))


print("Filtered Sentence:",filtered_sent)
print("Stemmed Sentence:",stemmed_words)

