# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def enc(text,s):
    res=""
    for i in range (len(text)):
        char=text[i]
        if (char.isupper()):
            res+=chr((ord(char)-65+s)%26+65)
        elif(char.islower()):
            res+=chr((ord(char)-97+s)%26+97)
        else:
            res+=char
    return res
def dec(text,s):
    res2=""
    for i in range (len(text)):
        char=text[i]
        if (char.isupper()):
            res2+=chr((ord(char)-65-s)%26+65)
        elif (char.islower()):
            res2+=chr((ord(char)-97-s)%26+97)
        else:
            res2+=char
    return res2
text=input("Enter the message:")
s=int(input("Enter the value of shift:"))
res3=enc(text,s)
print("Encrypted message:",res3)
print("Dencrypted message:",dec(res3,s))

#classic Caesar cipher, digits, numbers, spaces, and punctuation were left unencrypted.
#The Affine Cipher formula is:(a*char+b)mod26
#Ceaser Cipher formula:(char+b)mod26
#Special case meaning: a=1 (substisute in affine cipher and you get ceaser cipher)


