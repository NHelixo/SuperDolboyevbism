from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout


class MyApp1(App):
    def build(self):
        layout = RelativeLayout()

        button = Button(text = "fff", background_normal='pictures/button.png', background_down= 'pictures/button_down.png')

        layout.add_widget(button)

        return layout



if __name__ == '__main__':
    MyApp1().run()