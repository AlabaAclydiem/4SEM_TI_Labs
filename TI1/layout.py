import PySimpleGUI as sg

from widgets_keys import *

layout_plain_column = [
    [sg.Text('Исходный текст')],
    [sg.Multiline(size=(24, 16), key=ML_PLAIN, font=('Times New Roman', 16))],
]

layout_encrypt_column = [
    [sg.Text('Ключ шифрования:'), sg.Input(size=34, key=KEY_INPUT)],
    [sg.Button("Зашифровать текст\n(Столбцовый улучшенный метод, английский текст)", key=BTN_ENCRYPT_S, size=(50, 2))],
    [sg.Button("Зашифровать текст\n(Метод Виженера, самогенерирующийся ключ,\nрусский текст)",
               key=BTN_ENCRYPT_V, size=(50, 3))],
    [sg.Button('Загрузить текст', key=BTN_LOAD, size=(50, 2))]
]

layout_encrypted_column = [
    [sg.Text('Зашифрованный текст')],
    [sg.Multiline(size=(24, 16), disabled=True, key=ML_ENCRYPTED, font=('Times New Roman', 16))],
]

layout_decrypt_column = [
    [sg.Button("Расшифровать текст в\nсоответствии с использованным методом", key=BTN_DECRYPT, size=(50, 2))],
]

layout_decrypted_column = [
    [sg.Text('Расшифрованный текст')],
    [sg.Multiline(size=(24, 16), disabled=True, key=ML_DECRYPTED, font=('Times New Roman', 16))],
]

layout = [
    [
        sg.Column(layout_plain_column),
        sg.VSeparator(),
        sg.Column(layout_encrypt_column),
        sg.VSeparator(),
        sg.Column(layout_encrypted_column),
        sg.VSeparator(),
        sg.Column(layout_decrypt_column),
        sg.VSeparator(),
        sg.Column(layout_decrypted_column),
    ],
]
