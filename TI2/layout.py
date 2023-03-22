import PySimpleGUI as sg

column_one = [
    [sg.Text("Путь к файлу:", font=16)],
    [sg.Input(size=(70, 1), enable_events=True, key="filename", disabled=True, font=16)],
    [sg.Text("Ключ:", font=16)],
    [sg.Input(size=(40, 1), enable_events=True, key="key", font=16, )],
    [
        sg.FileBrowse(button_text="Открыть файл", size=(15, 2), target="filename", font=16),
        sg.Button(button_text="Преобразовать", size=(15, 2), key="process", font=16)
    ],
]

column_two = [
    [sg.Text("Биты исходного текста:", font=16)],
    [sg.Multiline(size=(24, 20), disabled=True, key="bitp", font=16)],
]

column_three = [
    [sg.Text("Биты ключа:", font=16)],
    [sg.Multiline(size=(24, 20), disabled=True, key="bitk", font=16)],
]

column_four = [
    [sg.Text("Биты преобразованного текста:", font=16)],
    [sg.Multiline(size=(24, 20), disabled=True, key="bitc", font=16)],
]

layout = [
    [
        sg.Column(column_one),
        sg.VSeparator(),
        sg.Column(column_two, element_justification='c'),
        sg.VSeparator(),
        sg.Column(column_three, element_justification='c'),
        sg.VSeparator(),
        sg.Column(column_four, element_justification='c'),
    ],

]
