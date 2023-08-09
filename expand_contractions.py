# pip install contractions

import contractions

sent = "I'm not sure, but I'd like to do it"

expanded_sent = contractions.fix(sent)

print(expanded_sent) # 'I am not sure, but I would like to do it'