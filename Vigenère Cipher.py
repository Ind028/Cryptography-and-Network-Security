# Caesar cipher function (used as component)
def caesar_encrypt(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            ciphertext += caesar_encrypt(char, shift)
            key_index += 1
        else:
            ciphertext += char

    return ciphertext
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - ord('a')
            plaintext += caesar_encrypt(char, -shift)
            key_index += 1
        else:
            plaintext += char

    return plaintext

text = input("Enter the message: ") 
key = input("Enter the key: ") 
encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)
print("Plaintext :", text)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)