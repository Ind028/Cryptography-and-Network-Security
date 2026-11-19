#Monoalphabetic Cipher Breaking
from collections import Counter 
ci=input("Enter cipher text:").upper()
freq=Counter(c for c in ci if c.isalpha())
english="QWERTYUIOPASDFGHJKLZXCVBNM"
letters=[x[0] for x in freq.most_common()]
mapping=dict(zip(letters,english))
res=""
for c in ci:
  res+=mapping.get(c,c) if c.isalpha() else c
print(ci)
print(res)
