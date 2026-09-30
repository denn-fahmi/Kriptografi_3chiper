def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - start + k) % 26 + start)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, k):
    return caesar_encrypt(ciphertext, -k)

if __name__ == "__main__":
    print("=== CAESAR CIPHER ===")
    text = input("Masukkan Teks : ")
    k = int(input("Masukkan Kunci (pergeseran n): "))
    
    enc = caesar_encrypt(text, k)
    dec = caesar_decrypt(enc, k)
    
    print(f"Hasil Enkripsi : {enc}")
    print(f"Hasil Dekripsi : {dec}")