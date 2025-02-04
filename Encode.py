def a1z22_encrypt(text):
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    encrypted_text = ''
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char) + 1
            encrypted_text += str(index) + ' '
        else:
            encrypted_text += char
    return encrypted_text.strip()

text = "Привіт, світ!"
encrypted_text = a1z22_encrypt(text)
print(encrypted_text)
