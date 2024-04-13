ALPHABATE = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_txt):
    cipher_txt = ''
    plain_txt = plain_txt.upper()


    for c in plain_txt:

        index = ALPHABATE.find(c)
        index = (index + KEY) %len(ALPHABATE)

        cipher_txt =cipher_txt+ALPHABATE[index]
     
    return cipher_txt



def caesar_decrypt(cipher_txt):

    plain_txt = ''

    for c in cipher_txt:
        index = ALPHABATE.find(c)
        index = (index - KEY) % len(ALPHABATE)
        plain_txt = plain_txt + ALPHABATE[index]

    return plain_txt

if __name__ == '__main__':
    
    m = 'My name is Sandip Paul'
    encrypted = caesar_encrypt(m)
    print(encrypted)
    print(caesar_decrypt(encrypted))


