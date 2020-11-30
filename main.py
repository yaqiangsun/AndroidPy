import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


# kivy.resources.resource_add_path("./font")
# font1=kivy.resources.resource_find("SourceHanSansSC-Light.otf")

from kivy.core.text import LabelBase
LabelBase.register(name='Font_Hanzi',fn_regular='./font/SourceHanSansSC-Light.otf')


class TestApp(App):
    def build(self):
        return Button(text='Hello World!你好',font_name='Font_Hanzi')

TestApp().run()