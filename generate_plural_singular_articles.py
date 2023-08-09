# pip install inflect 

import inflect

p = inflect.engine()

print(p.plural_noun('he')) # 'they'

print(p.plural_verb('sees')) # 'see'

p.gender("feminine")
print(p.singular_noun("they")) # 'she'

if p.compare_verbs('sees', 'see'):
    print("same word")  # same word


# Add the correct "a" or "an" for a given word
fruit1 = 'apple'
fruit2 = 'banana'
print(f"I got you {p.a(fruit1)} "
      f"and {p.a(fruit2)}")     # I got you an apple and a banana