from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder


Builder.load_file("kitabtap.kv")




class Interface(MDScreen):
    pass


class Kitabtap(MDApp):
    def build(self):
        return Interface()

if __name__ == '__main__':
    Kitabtap().run()
