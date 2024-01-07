import json
from collections import Counter

data = json.load(open('dictionary_compact.json'))
user = input("Enter the word:")
new = []

for i in data:
    if Counter(user) == Counter(i) and i != user:
        new.append(i)
    else:
        continue
if len(new) >0:
    print(f"Anagram for {user}:{new}")
else:
    print("No anagram found for this word")



