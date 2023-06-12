# pip install ekphrasis==0.5.4

# incorporate social tokenizers, word segmentation, spell correction, and more into a pipeline to process texts.

from ekphrasis.classes.preprocessor import TextPreProcessor
from ekphrasis.classes.tokenizer import SocialTokenizer
from ekphrasis.dicts.emoticons import emoticons

text_processor = TextPreProcessor(
    # terms that will be normalized
    normalize=['url', 'user'],
    # terms that will be annotated
    annotate={"hashtag", "allcaps", "elongated", "repeated",
        'emphasis', 'censored'},
    
    # corpus for word segmentation 
    segmenter="twitter", 
    
    unpack_hashtags=True,  # perform word segmentation on hashtags
    unpack_contractions=True,  # Unpack contractions (can't -> can not)
    spell_correct_elong=False,  # spell correction for elongated words

    tokenizer=SocialTokenizer(lowercase=True).tokenize,
    
    # Replace emojis with words
    dicts=[emoticons]
)

sent = "@coolyazzy94 I'm learning to retweeeet!! Least it sucks LESS than Facebook haha :P #learn-twitter https://t.co/7RdyMCVPKx"

print(" ".join(text_processor.pre_process_doc(sent)))

"""
Reading twitter - 1grams ...
Reading twitter - 2grams ...
Reading english - 1grams ...
<user> i am learning to retweet <elongated> ! <repeated> least it sucks <allcaps> less </allcaps> than facebook haha <tong> <hashtag> learn twitter </hashtag> <url>
"""