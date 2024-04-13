ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_txt):
    cipher_txt = ''
    plain_txt = plain_txt.upper()

    for c in plain_txt:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_txt += ALPHABET[index]
     
    return cipher_txt

def caesar_decrypt(cipher_txt):
    plain_txt = ''
    for c in cipher_txt:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_txt += ALPHABET[index]
    return plain_txt

if __name__ == '__main__':
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    if choice == 'E':
        plaintext = input("Enter the text to encrypt: ")
        encrypted = caesar_encrypt(plaintext)
        print("Encrypted text:", encrypted)
    elif choice == 'D':
        ciphertext = input("Enter the text to decrypt: ")
        decrypted = caesar_decrypt(ciphertext)
        print("Decrypted text:", decrypted)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
