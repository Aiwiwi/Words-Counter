def calcwords(information):
    inf = information.split()
    return f'В тексте {len(inf)} слов'


def calcsym(inf):
    l = 0
    for i in range(len(inf)):
        if inf[i] == ' ' or inf[i] == ',' or inf[i] == ':' or inf[i] == ';' or inf[i] == '"' or inf[i] == "'" or inf[i] == '.':
            continue
        else:
            l += 1
    return str(l)


def wordsbynum(information):
    text = ''
    words = list()

    for _ in range(16):
        words.append(0)

    inf = information.split()

    for i in inf:
        for j in range(0,len(words)):
            if len(i) == j:
                if i[-1] in '.,/|!#%?':
                    words[j-1] += 1
                    continue
                words[j] += 1

    for i in range(len(words)):
        text += f'Слов которые состоят из {i} букв {words[i]}\n'

    return text


def alphabet(information):
    text = ''
    information = information.lower()
    alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    ltrs = list()
    for i in range(33):
        ltrs.append(0)

    for i in range(len(information)):
        for j in range(len(alph)):
            if information[i] == alph[j]:
                ltrs[j] += 1

    for i in range(len(ltrs)):
        text += f'Буква {alph[i]} встречается {ltrs[i]} раз\n'

    return text

