#Name: Nutawut Naprom
#Lang: Python

from difflib import SequenceMatcher

txt1 = input('Enter your fist text: ')
txt2 = input('Enter your second text: ')

match = SequenceMatcher(None, txt1, txt2).find_longest_match(0, len(txt1), 0, len(txt2))

print(txt1[match.a: match.a+match.size])
