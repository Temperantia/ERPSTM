from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

#Builder.load_file("test.kv")

def standardTextField(text):
        t = TextInput()
        t.hint_text= text
        t.size_hint=(0.4,1)
        t.font_size = 25
        t.focus = True
        t.size_hint_max_y = 40
        t.multiline=False
        return t

class MyApp(App):
    nom = None
    mdp = None

    def getFields(self):
        nom = self.nom.text
        mdp = self.mdp.text
        print (nom, mdp)
        return (nom, mdp)

    def build(self):
        b = BoxLayout(orientation = 'vertical')
        b.padding= [10,10,10,10]
        b.pos = (0,0)
        b.spacing = 40

        self.nom = standardTextField("Nom")
        self.mdp = standardTextField("Mot de passe")
        self.mdp.password = True
        b.add_widget(self.nom)
        b.add_widget(self.mdp)

        btn = Button(text = "Valider")
        btn.size_hint = (.4,0.1)
        btn.on_press = self.getFields
        l = Label(text = "")
        
        b.add_widget(btn)
        b.add_widget(l)
       
        return b


MyApp().run()
