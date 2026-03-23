def playfair(txt, key, mode=1):
    abc = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    k = "".join(dict.fromkeys(key.upper().replace('J','I') + abc))
    m = [k[i:i+5] for i in range(0, 25, 5)]
    t = txt.upper().replace('J','I').replace(" ","")
    if mode == 1:
        t = "".join(t[i] + (t[i+1] if i+1 < len(t) and t[i] != t[i+1] else 'X') for i in range(0, len(t), 2))
        if len(t) % 2: t += 'X'
    def pos(c): return next((r, row.find(c)) for r, row in enumerate(m) if c in row)
    res = ""
    for i in range(0, len(t), 2):
        r1, c1 = pos(t[i]); r2, c2 = pos(t[i+1])
        if r1 == r2: res += m[r1][(c1+mode)%5] + m[r2][(c2+mode)%5]
        elif c1 == c2: res += m[(r1+mode)%5][c1] + m[(r2+mode)%5][c2]
        else: res += m[r1][c2] + m[r2][c1]
    return res
s, k = input("Enter text: "), input("Enter key: ")
enc = playfair(s, k, 1)
dec = playfair(enc, k, -1)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
