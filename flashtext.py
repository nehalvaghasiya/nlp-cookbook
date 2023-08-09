# pip install flashtext

# extract similar keywords and turn them into one standard keyword
# use FlashText to extract the keywords CEO and Python programming language from a sentence that contains only the keywords ceo and Python

from flashtext import KeywordProcessor

kw_processor = KeywordProcessor()
kw_dict = {
    "CEO": ["Chief Executive Officer", "ceo"], # Similar keywords to CEO
    "Python programming language": ["Python", "Python language"]
}
kw_processor.add_keywords_from_dict(keyword_dict=kw_dict)

sent = "The ceo of this company is fluent in Python."
standard_keyword = kw_processor.extract_keywords(sent)

print(standard_keyword)  # ['CEO', 'Python programming language']