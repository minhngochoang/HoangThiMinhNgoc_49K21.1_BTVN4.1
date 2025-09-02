def caesar_encrypt(text, key, alphabet):
    key = key % 26 
    encrypted = ""

    text = text.upper()

    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)  
            new_idx = (idx + key) % 26 
            encrypted += alphabet[new_idx] 
        else:
            encrypted += char 
    return encrypted

plaintext = "HOANG THI MINH NGOC"
key = 35
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

result = caesar_encrypt(plaintext, key, alphabet)

print("Văn bản gốc  :", plaintext)
print("Mã hóa       :", result) 
