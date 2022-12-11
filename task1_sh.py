import string
import random

# generate alphabet with string module from python
def GenAlpha():
    alpha = list(string.ascii_lowercase)
    alpha.remove('j')
    return alpha

# Shuffle alphabet with random module from python
def ShuffleAlpha(alpha):
    sh_alpha = alpha
    random.shuffle(sh_alpha)
    return sh_alpha

# Encrypt Text
def Encrypt(text, sh_alpha):
    enc_text = ""
    for letter in text:
        letter = letter.lower()
        if letter != " ":
            if letter == "j":
                letter = "i"
            index = sh_alpha.index(letter)
            place = (index + 5) % 25
            enc_text += sh_alpha[place]
        else:
            enc_text += " "
    return enc_text

# Show alphabet in matrix look
def ShowAlphaMatrix(alpha, length):
    for i in range(length):
        print(sh_alpha[i], end=" ")
        if (i + 1) % 5 == 0:
            print()

# Decrypt text
def Decrypt(enc_text, sh_alpha):
    dec_text = ""
    for letter in enc_text:
        if letter != " ":
            index = sh_alpha.index(letter)
            place = (index - 5) % 25
            dec_text += sh_alpha[place]
        else:
            dec_text += " "
    return dec_text

# Main Part
text = input("Input your text: ")

alpha = GenAlpha()
sh_alpha = ShuffleAlpha(alpha)
print("Shuffled alphabet:")
ShowAlphaMatrix(sh_alpha, 25)

print()

print("Text to encrypt: ")
print(text)

print()

enc_text = Encrypt(text, sh_alpha)
print("Encrypted text: ")
print(enc_text)

print()

dec_text = Decrypt(enc_text, sh_alpha)
print("Decrypted text: ")
print(dec_text)






