from kivy.uix.label import Label

"""
Creer un titre standard contenant le texte fourni en argument
"""


def standardTitle(text):
    title = Label()
    title.text = text
    title.bold = True
    title.font_size = 26
    return title
