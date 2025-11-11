en_alpha_lower = [chr(i) for i in range(97, 123)]
en_alpha_upper = [chr(i) for i in range(65, 91)]

ru_alpha_lower = [chr(i) for i in range(1072, 1104)]
ru_alpha_upper = [chr(i) for i in range(1040, 1072)]


def caesar(text, lang, step):
    if lang == 'en':
        alpha_lower = en_alpha_lower
        alpha_upper = en_alpha_upper

    elif lang == 'ru':
        alpha_lower = ru_alpha_lower
        alpha_upper = ru_alpha_upper

    else:
        print('Такого языка не существует')
        return

    for i in text:
        if i.isalpha():
            if i.isupper():
                print(alpha_upper[(alpha_upper.index(i) + step) % len(alpha_upper)], end='')
            if i.islower():
                print(alpha_lower[(alpha_lower.index(i) + step) % len(alpha_lower)], end='')

        else:
            print(i, end='')


caesar(input('Введите текст: '), input('Введите язык: '),
       int(input('На сколько шагов сдвигать? (Для сдвига в левую сторону введите отрицательное число): ')))
