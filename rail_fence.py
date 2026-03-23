def rail_fence(text, rails, mode='e'):
    idx = list(range(rails)) + list(range(rails-2, 0, -1))
    pattern = [idx[i % len(idx)] for i in range(len(text))]
    if mode == 'e':
        return "".join(text[i] for r in range(rails) for i, row in enumerate(pattern) if row == r)
    else:
        result = [''] * len(text)
        pos = 0
        for r in range(rails):
            for i, row in enumerate(pattern):
                if row == r:
                    result[i] = text[pos]
                    pos += 1
        return "".join(result)
s = input("Enter text: ").replace(" ", "").upper()
n = int(input("Enter number of rails: "))
enc = rail_fence(s, n, 'e')
dec = rail_fence(enc, n, 'd')
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
