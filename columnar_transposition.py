import math

def columnar_encrypt(plaintext, num_cols):
    # Buang spasi untuk transposisi standar
    text = plaintext.replace(" ", "")
    ciphertext = [""] * num_cols
    for col in range(num_cols):
        pointer = col
        while pointer < len(text):
            ciphertext[col] += text[pointer]
            pointer += num_cols
    return "".join(ciphertext)

def columnar_decrypt(ciphertext, num_cols):
    num_rows = math.ceil(len(ciphertext) / num_cols)
    num_shaded_boxes = (num_cols * num_rows) - len(ciphertext)
    plaintext = [''] * num_rows
    
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_rows) or (row == num_rows - 1 and col >= num_cols - num_shaded_boxes):
            row = 0
            col += 1
    return "".join(plaintext)

if __name__ == "__main__":
    print("=== COLUMNAR TRANSPOSITION CIPHER ===")
    text = input("Masukkan Teks : ")
    cols = int(input("Masukkan Jumlah Kolom (Kunci angka): "))
    
    enc = columnar_encrypt(text, cols)
    dec = columnar_decrypt(enc, cols)
    
    print(f"Hasil Enkripsi : {enc}")
    print(f"Hasil Dekripsi : {dec}")