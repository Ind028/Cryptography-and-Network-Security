from collections import Counter

cipher = ''.join(c for c in input("Ciphertext: ").upper() if c.isalpha())

# Estimate key length using repeated patterns
scores = {}
for k in range(1, 11):
    cols = [cipher[i::k] for i in range(k)]
    ic = sum(sum(n*(n-1) for n in Counter(x).values()) /
             (len(x)*(len(x)-1)) for x in cols if len(x) > 1)
    scores[k] = ic / k

keylen = max(scores, key=scores.get)
print("Estimated key length:", keylen)

# Find key using frequency analysis
english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
key = ""

for col in range(keylen):
    s = cipher[col::keylen]
    most = Counter(s).most_common(1)[0][0]
    shift = (ord(most) - ord(english[0])) % 26
    key += chr(65 + shift)
  
print("Estimated key:", key)

# Decrypt
plain = ""
for i, c in enumerate(cipher):
    p = (ord(c) - ord(key[i % keylen])) % 26
    plain += chr(65 + p)

print("Plaintext:", plain)