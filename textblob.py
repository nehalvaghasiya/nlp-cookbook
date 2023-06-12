# pip install textblob
# python3 -m textblob.download_corpora

from textblob import TextBlob

text = "Today is a beautiful day"
blob = TextBlob(text)

print(blob.words) # Word tokenization - WordList(['Today', 'is', 'a', 'beautiful', 'day'])

print(blob.noun_phrases) # Noun phrase extraction - WordList(['beautiful day'])

print(blob.sentiment) # Sentiment analysis - Sentiment(polarity=0.85, subjectivity=1.0)

print(blob.word_counts) # Word counts - defaultdict(int, {'today': 1, 'is': 1, 'a': 1, 'beautiful': 1, 'day': 1})

# Spelling correction
text = "Today is a beutiful day"
blob = TextBlob(text)
print(blob.correct()) # TextBlob("Today is a beautiful day")