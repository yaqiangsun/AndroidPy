import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle,Color

Window.clearcolor = (1, 1, 1, 1)
# kivy.resources.resource_add_path("./font")
# font1=kivy.resources.resource_find("SourceHanSansSC-Light.otf")

from kivy.core.text import LabelBase
from kivy.resources import resource_add_path,resource_find
resource_add_path('./data/fonts')
from kivy.core.text import LabelBase
LabelBase.register(name='SourceHanSansSC',fn_regular='SourceHanSansSC-Light.otf')





class TestApp(App):
    def build(self):
        btn = Button(text='Hello World!你好',
                   font_size="20sp",
                   color=(0,1,1,1),
                   background_color=(0,0.5,0.5,1),
                   size=(50,50),
                   size_hint=(0.3,0.1),
                   pos=(200,200),
                   font_name='SourceHanSansSC')
        return btn
        # return Button(text='Hello World!你好')

TestApp().run()