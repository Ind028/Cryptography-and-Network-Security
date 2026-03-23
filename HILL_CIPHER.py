import numpy as np
def mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    try:
        det_inv = pow(det % modulus, -1, modulus)
    except ValueError:
        return None 
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)
    return (det_inv * adjugate) % modulus
def hill_cipher(text, key_matrix, mode='encrypt'):
    mod = 26
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0: text += 'X'
    key_matrix = np.array(key_matrix, dtype=int)
    if mode == 'decrypt':
        key_matrix = mod_inverse(key_matrix, mod)
        if key_matrix is None:
            return "ERROR: Key matrix is not invertible mod 26"
    res = ""
    for i in range(0, len(text), 2):
        block = np.array([ord(text[i]) - 65, ord(text[i+1]) - 65], dtype=int)
        processed = np.dot(key_matrix, block) % mod
        res += chr(int(processed[0]) + 65) + chr(int(processed[1]) + 65)
    return res
s = input("Enter text: ")
key_input = input("Enter key (e.g., 3 3 2 5): ")
key_list = [int(x) for x in key_input.split()]
key = np.array(key_list).reshape(2, 2)
encrypted = hill_cipher(s, key, 'encrypt')
decrypted = hill_cipher(encrypted, key, 'decrypt')
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

