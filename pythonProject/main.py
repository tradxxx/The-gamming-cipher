def feedback_cipher(text, a, b, c):
    encrypted_text = ""
    feedback = 0

    for char in text:
        char_code = ord(char)
        encrypted_char = chr(char_code ^ feedback)
        feedback = (a * feedback + char_code + b) % c
        encrypted_text += encrypted_char

    return encrypted_text

def decrypt_feedback_cipher(encrypted_text, a, b, c):
    decrypted_text = ""
    feedback = 0

    for char in encrypted_text:
        char_code = ord(char)
        decrypted_char = chr(char_code ^ feedback)
        decrypted_text += decrypted_char
        feedback = (a * feedback + ord(decrypted_char) + b) % c

    return decrypted_text

# Исходный текст и параметры A, B, C
original_text = input ("Введите текст: ")
A = 7
B = 3
C = 32

# Шифрование текста
encrypted_text = feedback_cipher(original_text, A, B, C)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование текста
decrypted_text = decrypt_feedback_cipher(encrypted_text, A, B, C)
print("Дешифрованный текст:", decrypted_text)