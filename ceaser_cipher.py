def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif not char.isalpha():
            result += char
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

text = input("Enter the message: ") 
s = int(input("Enter shift value: "))
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
#classic Caesar cipher, digits, numbers, spaces, and punctuation were left unencrypted.