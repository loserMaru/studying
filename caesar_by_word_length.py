sentence = input()
text = list(sentence)
for i in ',."!?':
    sentence = sentence.replace(i, ' ')
text_list = sentence.split()
step = len(text_list[0])
counter = 0

alpha_lower = [chr(i) for i in range(97, 123)]
alpha_upper = [chr(i) for i in range(65, 91)]

for i in text:
    if i.isalpha():
        if i.isupper():
            print(alpha_upper[(alpha_upper.index(i) + step) % len(alpha_upper)], end='')
        if i.islower():
            print(alpha_lower[(alpha_lower.index(i) + step) % len(alpha_lower)], end='')

    else:
        print(i, end='')

    if i == ' ':
        counter += 1
        step = len(text_list[counter])
