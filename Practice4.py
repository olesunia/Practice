
def encrypt_text(text,key):
    alph_mini = 'abcdefghijklmnopqrstuvwxyz'
    alph_maxi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ciphertext = ''

    for k in range(len(text)):
        key_int = alphabet.index(key[k % len(key)])   #індекс значення ключа в алфавіті
        if text[k] == ' ':                #перевірка на пробіл, проте лише для одного пробіла
            ciphertext += text[k]         #добавляємо пробіл в результат
            text_new = text[k + 1:len(text)]  #створюємо новий текст після пробілу
            for h in range(len(text_new)):
                key_int_new = alphabet.index(key[h % len(key)])
                if text_new[h] == text_new[h].upper():
                    text_int_new = alph_maxi.index(text_new[h])
                    value_new = (text_int_new + key_int_new) % 26
                    ciphertext += alph_maxi[value_new]
                else:
                    text_int_new = alph_mini.index(text_new[h])
                    value_new = (text_int_new + key_int_new) % 26
                    ciphertext += alph_mini[value_new]
            break

        else:
            if text[k] == text[k].upper():              #перевірка на регістр
                text_int = alph_maxi.index(text[k])     #індекс значення літери тексту в алфавіті великих літер
                value = (text_int + key_int) % 26       #зашифровка за Віженером
                ciphertext += alph_maxi[value]
            else:
                text_int = alph_mini.index(text[k])     #індекс значення літери тексту в алфавіті малих літер
                value = (text_int + key_int) % 26
                ciphertext += alph_mini[value]

    print(ciphertext)



def decrypt_text(cipher_text,key):
    alph_mini = 'abcdefghijklmnopqrstuvwxyz'
    alph_maxi = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    real_text = ''

    for k in range(len(cipher_text)):
        key_int = alphabet.index(key[k % len(key)])   #індекс значення ключа в алфавіті
        if cipher_text[k] == ' ':                #перевірка на пробіл, проте лише для одного пробіла
            real_text += cipher_text[k]         #добавляємо пробіл в результат
            text_new = cipher_text[k + 1:len(cipher_text)]  #створюємо новий текст після пробілу
            for h in range(len(text_new)):
                key_int_new = alphabet.index(key[h % len(key)])
                if text_new[h] == text_new[h].upper():
                    text_int_new = alph_maxi.index(text_new[h])
                    value_new = (text_int_new - key_int_new) % 26
                    real_text += alph_maxi[value_new]
                else:
                    text_int_new = alph_mini.index(text_new[h])
                    value_new = (text_int_new - key_int_new) % 26
                    real_text += alph_mini[value_new]
            break

        else:
            if cipher_text[k] == cipher_text[k].upper():              #перевірка на регістр
                text_int = alph_maxi.index(cipher_text[k])     #індекс значення літери тексту в алфавіті великих літер
                value = (text_int - key_int) % 26       #зашифровка за Віженером
                real_text += alph_maxi[value]
            else:
                text_int = alph_mini.index(cipher_text[k])     #індекс значення літери тексту в алфавіті малих літер
                value = (text_int - key_int) % 26
                real_text += alph_mini[value]

    print(real_text)


def main():
    choice = input("Введіть 'Encrypt' для зашифрування тексту або 'Decrypt' для розшифрування: ")
    if choice == 'Encrypt':
        text = input("Ведіть текст: ")
        key = input("Введіть ключ: ")
        print("Вхідний текст: ", text)
        print("Введений ключ: ", key)
        print("Зашифрований текст: ", end = '')
        encrypt_text(text, key)

    elif choice == 'Decrypt':
        cipher_text = input("Введіть зашифрований тескт: ")
        key_1 = input("Введіть ключ: ")
        print("Зашифрований текст: ", cipher_text)
        print("Введений ключ: ", key_1)
        print("Розшифрований текст: ", end = '')
        decrypt_text(cipher_text, key_1)
    else:
        print("Ввід неправильний!")


main()



