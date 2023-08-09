# pip install num2words

from num2words import num2words

print(num2words(2019)) # 'two thousand and nineteen'

print(num2words(2019, to='ordinal')) # 'two thousand and nineteenth'

print(num2words(2019, to='ordinal_num')) # '2019th'

print(num2words(2019, to='year')) # 'twenty nineteen'

# generate ordinal numbers and support multiple languages

print(num2words(2019, lang='de')) # zweitausendneunzehn