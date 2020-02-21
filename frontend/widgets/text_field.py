from kivy.uix.textinput import TextInput


def standardTextField(text):
    t = TextInput()
    t.hint_text = text
    t.font_size = 22
    t.focus = True
    t.size_hint_max_y = 40
    t.multiline = False
    return t
