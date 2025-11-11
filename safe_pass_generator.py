import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'


def requirements():
    chars = ''
    count = int(input('Количество паролей хотите создать: '))
    length = int(input('Какой длины должен быть пароль(-и)?: '))
    digits_in_pass = input('Включать ли цифры 0123456789?: ')
    uppercase_in_pass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?: ')
    lowercase_in_pass = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?: ')
    punc_in_pass = input('Включать ли символы !#$%&*+-=?@^_?: ')
    exclude_in_pass = input('Исключать ли неоднозначные символы il1Lo0O?: ')

    if digits_in_pass.lower() == 'да':
        chars += digits

    if uppercase_in_pass.lower() == 'да':
        chars += uppercase_letters

    if lowercase_in_pass.lower() == 'да':
        chars += lowercase_letters

    if punc_in_pass.lower() == 'да':
        chars += punctuation

    if exclude_in_pass == 'да':
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')

    return count, length, chars

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

count, length, chars = requirements()

for _ in range(count):
    print(generate_password(length, chars))