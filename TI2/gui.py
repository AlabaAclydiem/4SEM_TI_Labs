import PySimpleGUI as sg

from layout import layout
import re
from funcs import enchipher, bitrepr

window = sg.Window("Потоковое шифрование", layout, element_justification='c')
saved_data = dict()

show, p, c, k, i = False, None, None, None, 0

while True:
    event, values = window.read()
    if event == "key":
        res = re.sub(r"[^01]", "", values["key"])[:24]
        if res != values["key"]:
            window["key"].update(res)
    elif event == "filename":
        name = values["filename"].split("/")[-1]
        if name in saved_data.keys():
            window["key"].update(saved_data[name])
    elif not show and event == "process":
        name = values["filename"].split("/")[-1]
        if name in saved_data.keys():
            tail, front, _ = name.split(".")
            targetfile = ".".join(["deciphered", front, tail])
        else:
            front, tail = name.split(".")
            targetfile = ".".join([tail, front, "txt"])
            saved_data[targetfile] = values["key"]
        enchipher(values["filename"], "/".join(values["filename"].split("/")[:-1]) + "/" + targetfile, values["key"])
        show = True
        i = 0
        with open(values["filename"], "rb") as f:
            p = f.read()
        with open("testfiles/key.txt", "rb") as f:
            k = f.read()
        with open("/".join(values["filename"].split("/")[:-1]) + "/" + targetfile, "rb") as f:
            c = f.read()
        window["bitp"].update("")
        window["bitk"].update("")
        window["bitc"].update("")
    elif event == sg.WIN_CLOSED:
        break

    while show:
        window["bitp"].update(bitrepr(p[i]) + "\n", append=True)
        window["bitk"].update(bitrepr(k[i]) + "\n", append=True)
        window["bitc"].update(bitrepr(c[i]) + "\n", append=True)
        window.refresh()
        i += 1
        if len(p) > 2000:
            if i == 1000:
                i = -i + 1
                window["bitp"].update("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", append=True)
                window["bitk"].update("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", append=True)
                window["bitc"].update("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", append=True)
            elif i == 0:
                show = False
        elif i == len(p):
            show = False




window.close()
