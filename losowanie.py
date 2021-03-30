import kivy
from random import randint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.properties import ObjectProperty
from kivy.config import Config

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

class Losowanie(FloatLayout):
    wynik = ObjectProperty("...")
    def pressed(self):
        self.data_base = ["Bogdan",
                     "Emil",
                     "Jan",
                     "Janusz",
                     "Jarek",
                     "Józef",
                     "Julian",
                     "Krystian",
                     "Marek",
                     "Michał",
                     "Proboszcz",
                     "Wojciech"]

        self.pozycja = randint(0, 11)
        self.wynik = self.data_base[self.pozycja]
        print(self.wynik)


class MainApp(App):
    def build(self):
        return Losowanie()
    

if __name__ == '__main__':
    MainApp().run()