# pip install git+https://github.com/ramsrigouthamg/Questgen.ai
# pip install git+https://github.com/boudinfl/pke.git

# python3 -m nltk.downloader universal_tagset
# python3 -m spacy download en 

# wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
# tar -xvf  s2v_reddit_2015_md.tar.gz

from pprint import pprint
import nltk
nltk.download('stopwords')
from Questgen import main

payload = {
    "input_text": """The weather today was nice so I went for a walk. I stopped for a quick chat with my neighbor.
    It turned out that my neighbor just got a dog named Pepper. It is a black Labrador Retriever."""
}

qe = main.BoolQGen()
output = qe.predict_boolq(payload)
pprint(output)
"""
{'Boolean Questions': ['Is there a dog in my neighborhood?',
                       "Is pepper my neighbor's dog?",
                       'Is pepper the same as a labrador?'],
 'Count': 4,
 'Text': 'The weather today was nice so I went for a walk. I stopped for a '
         'quick chat with my neighbor.\n'
         '    It turned out that my neighbor just got a dog named Pepper. It '
         'is a black Labrador Retriever.'}
"""


output = qe.predict_shortq(payload)
pprint(output)
"""
Running model for generation
{'questions': [{'Question': 'What was the purpose of the stop?', 'Answer': 'chat', 'id': 1, 'context': 'I stopped for a quick chat with my neighbor.'}, {'Question': 'Who got a dog named Pepper?', 'Answer': 'neighbor', 'id': 2, 'context': 'It turned out that my neighbor just got a dog named Pepper. I stopped for a quick chat with my neighbor.'}]}
{'questions': [{'Answer': 'chat',
                'Question': 'What was the purpose of the stop?',
                'context': 'I stopped for a quick chat with my neighbor.',
                'id': 1},
               {'Answer': 'neighbor',
                'Question': 'Who got a dog named Pepper?',
                'context': 'It turned out that my neighbor just got a dog '
                           'named Pepper. I stopped for a quick chat with my '
                           'neighbor.',
                'id': 2}],
 'statement': 'The weather today was nice so I went for a walk. I stopped for '
              'a quick chat with my neighbor. It turned out that my neighbor '
              'just got a dog named Pepper. It is a black Labrador Retriever.'}
"""

