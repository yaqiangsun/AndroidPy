import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


kivy.resources.resource_add_path("./font")
font1=kivy.resources.resource_find("SourceHanSansSC-Light.otf")


class TestApp(App):
    def build(self):
        return Button(text='Hello World!你好',font_name=font1)

TestApp().run()