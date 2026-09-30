def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('A')
            ciphertext += chr((ord(char) - start + k) % 26 + start)
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('A')
            plaintext += chr((ord(char) - start - k) % 26 + start)
            key_index += 1
        else:
            plaintext += char
    return plaintext

if __name__ == "__main__":
    print("=== VIGENERE CIPHER (ABJAD MAJEMUK) ===")
    text = input("Masukkan Teks : ")
    key = input("Masukkan Kata Kunci : ")
    
    enc = vigenere_encrypt(text, key)
    dec = vigenere_decrypt(enc, key)
    
    print(f"Hasil Enkripsi : {enc}")
    print(f"Hasil Dekripsi : {dec}")