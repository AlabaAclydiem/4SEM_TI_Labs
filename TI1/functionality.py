from itertools import cycle

METHOD_USED = ""
KEY_USED = ""
ALPHABET_USED = ""
RU_ALPHABET = sorted("ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ")
RU_ALPHABET.insert(6, 'Ё')
EN_ALPHABET = sorted("QWERTYUIOPLKJHGFDSAZXCVBNM")


class ErrorText(Exception):
    pass


class ErrorKey(Exception):
    pass


def clear(text):
    return "".join([symbol for symbol in text.upper() if symbol in ALPHABET_USED])


def init_encryption(text, key, alphabet, method=""):
    global KEY_USED, ALPHABET_USED, METHOD_USED
    ALPHABET_USED = alphabet
    nkey, ntext = clear(key), clear(text)
    if not ntext:
        raise ErrorText
    if not nkey:
        raise ErrorKey
    KEY_USED = key
    if method:
        METHOD_USED = method
    return ntext, nkey


def load_text(filename):
    with open(filename, 'r') as file:
        result = file.read()
    return result


def export_text(filename, text):
    with open(filename, 'w') as file:
        file.write(text)


def encrypt_s(text, key):
    try:
        text, key = init_encryption(text, key, EN_ALPHABET, "S")
    except ErrorText:
        return "Исходный текст не содержит допустимых символов"
    except ErrorKey:
        return "Ключ не содержит допустимых символов"
    key_indexes = cycle(index for index, _ in sorted(enumerate(key), key=lambda x: x[1]))
    table, text_index = [], 0
    for row_len in key_indexes:
        row = []
        fill_interval = min(len(text) - text_index, row_len + 1)
        if not fill_interval:
            break
        for _ in range(fill_interval):
            row.append(text[text_index])
            text_index += 1
        for _ in range(fill_interval, len(key)):
            row.append('')
        table.append(row)
    key_indexes, result = (index for index, _ in sorted(enumerate(key), key=lambda x: x[1])), ""
    for index in key_indexes:
        for row in table:
            if row[index]:
                result += row[index]
    export_text('res/encrypted.txt', result)
    return result


def encrypt_v(text, key):
    try:
        text, key = init_encryption(text, key, RU_ALPHABET, "V")
    except ErrorText:
        return "Исходный текст не содержит допустимых символов"
    except ErrorKey:
        return "Ключ не содержит допустимых символов"
    key = key + text[:len(text) - len(key)]
    result = "".join(ALPHABET_USED[(ALPHABET_USED.index(index) + ALPHABET_USED.index(shift)) % len(ALPHABET_USED)]
                     for index, shift in zip(text, key))
    export_text('res/encrypted.txt', result)
    return result


def decrypt(text):
    try:
        text, key = init_encryption(text, KEY_USED, ALPHABET_USED)
    except (ErrorText, ErrorKey):
        return "Дешифрование невозможно"
    if METHOD_USED == 'S':
        key_indexes = cycle(index for index, _ in sorted(enumerate(key), key=lambda x: x[1]))
        table, text_index = [], 0
        for row_len in key_indexes:
            row = []
            fill_interval = min(len(text) - text_index, row_len + 1)
            if not fill_interval:
                break
            for _ in range(fill_interval):
                row.append('\0')
                text_index += 1
            for _ in range(fill_interval, len(key)):
                row.append('')
            table.append(row)
        key_indexes, text_index = (index for index, _ in sorted(enumerate(key), key=lambda x: x[1])), 0
        for index in key_indexes:
            for row in table:
                if row[index]:
                    row[index] = text[text_index]
                    text_index += 1
        result = "".join(symbol for row in table for symbol in row)
    elif METHOD_USED == 'V':
        result = ""
        for index, symbol in enumerate(text):
            decrypted_symbol = ALPHABET_USED[(ALPHABET_USED.index(symbol) + len(ALPHABET_USED) -
                                              ALPHABET_USED.index(key[index])) % len(ALPHABET_USED)]
            result += decrypted_symbol
            key += decrypted_symbol
    export_text('res/decrypted.txt', result)
    return result
