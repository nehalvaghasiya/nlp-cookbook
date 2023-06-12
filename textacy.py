# pip install spacy textacy
# python3 -m spacy download en_core_web_sm

# extract a contiguous sequence of words from a text

import spacy
from textacy.extract import ngrams

nlp = spacy.load("en_core_web_sm")

text = nlp("Ice cream is a soft frozen food made with sweetened and flavored milk fat.")

# extract sequences of 3 words
words = [n.text for n in ngrams(text, n=3)]

print(words) # ['soft frozen food', 'sweetened and flavored', 'flavored milk fat']