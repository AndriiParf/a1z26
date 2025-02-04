def a1z22_decrypt(text):
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    decrypted_text = ''
    parts = text.split(' ')
    for part in parts:
        if part.isdigit():
            index = int(part) - 1
            if 0 <= index < len(alphabet):
                decrypted_text += alphabet[index]
            else:
                decrypted_text += '?'
        else:
            decrypted_text += part
    return decrypted_text

text = '20 21 11 3 12 23 , 22 3 12 23 !'
decrypted_text = a1z22_decrypt(text)
print(decrypted_text)
