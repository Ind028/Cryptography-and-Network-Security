# Caesar cipher function (used as component)
def vig_enc(text,key):
    res=""
    key_index=0
    for char in text:
        if char.isalpha():
            shift=ord(key[key_index%len(key)].lower())-97
            if char.isupper():
                res+=chr((ord(char)-65+shift)%26+65)
            else:
                res+=chr((ord(char)-97+shift)%26+97)
            key_index+=1
        else:
            res+=char
    return res
def vig_dec(text,key):
    res2=""
    key_index=0
    for char in text:
        if char.isalpha():
            shift2=ord(key[key_index%len(key)].lower())-97
            if char.isupper():
                res2+=chr((ord(char)-65-shift2)%26+65)
            else:
                res2+=chr((ord(char)-97-shift2)%26+97)
            key_index+=1
        else:
            res2+=char
    return res2
text=input("Enter the text:")
key=input("Enter the key:")
res3=vig_enc(text,key)
print("Encrypted msg:",res3)
print("dEncrypted msg:",vig_dec(res3,key))
  
