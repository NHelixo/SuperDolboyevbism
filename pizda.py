from kivy.app import App
from kivy.uix.progressbar import ProgressBar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SimpleProgressBarApp(App):
    def build(self):
        self.value1 = 10
        layout = BoxLayout(orientation='vertical')
        self.button = Button(text = "тицьни")
        self.progress_bar = ProgressBar(max=100, value=self.value1)
        layout.add_widget(self.button)
        layout.add_widget(self.progress_bar)

        self.button.on_press = self.huita
        return layout

    def huita(self):
        if self.value1 < 100:
            self.value1 += 10
            self.progress_bar.value = self.value1
        else:
            self.value1 = 0
            self.progress_bar.value = self.value1


if __name__ == '__main__':
    SimpleProgressBarApp().run()
