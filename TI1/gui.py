import PySimpleGUI as sg

from layout import layout
from widgets_keys import *
from functionality import load_text, encrypt_s, encrypt_v, decrypt

window = sg.Window("Шифровальная машина", layout)

while True:
    event, values = window.read()
    if event == BTN_LOAD:
        window[ML_PLAIN].Update(load_text('res/plain.txt'))
        window[ML_ENCRYPTED].Update("")
        window[ML_DECRYPTED].Update("")
    elif event == BTN_ENCRYPT_S:
        window[ML_ENCRYPTED].Update(encrypt_s(values[ML_PLAIN], values[KEY_INPUT]))
        window[ML_DECRYPTED].Update("")
    elif event == BTN_ENCRYPT_V:
        window[ML_ENCRYPTED].Update(encrypt_v(values[ML_PLAIN], values[KEY_INPUT]))
        window[ML_DECRYPTED].Update("")
    elif event == BTN_DECRYPT:
        window[ML_DECRYPTED].Update(decrypt(values[ML_ENCRYPTED]))
    elif event == sg.WIN_CLOSED:
        break

window.close()
