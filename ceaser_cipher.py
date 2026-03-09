def encrypt(text, s):
    result = ""
    a=1
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((a*(ord(char)) + s - 65) % 26 + 65)
        elif not char.isalpha():
            result += char
        else:
            result += chr((a*(ord(char))indrani
                            + s - 97) % 26 + 97)
    return result

text = input("Enter the message: ") 
s = int(input("Enter shift value: "))
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
#classic Caesar cipher, digits, numbers, spaces, and punctuation were left unencrypted.
#The Affine Cipher formula is:(a*char+b)mod26
#Ceaser Cipher formula:(char+b)mod26
#Special case meaning: a=1 (substisute in affine cipher and you get ceaser cipher)


