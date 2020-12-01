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

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from android.runnable import run_on_ui_thread
from jnius import autoclass


Color = autoclass("android.graphics.Color")
WindowManager = autoclass('android.view.WindowManager$LayoutParams')
activity = autoclass('org.kivy.android.PythonActivity').mActivity

Builder.load_string('''
<MainApp>:
    orientation: 'vertical'

    Button:
        text: 'White'
        on_press: root.statusbar("#FFFFFF")

    Button:
        text: 'Red'
        on_press: root.statusbar("#FF0000")

    Button:
        text: 'Green'
        on_press: root.statusbar("#00FF00")

    Button:
        text: 'Blue'
        on_press: root.statusbar("#0000FF")

    Button:
        text: 'Yellow'
        on_press: root.statusbar("#FFFF00")

    Button:
        text: 'Gray'
        on_press: root.statusbar("#808080")

''')



from kivy.core.text import LabelBase
from kivy.resources import resource_add_path,resource_find
resource_add_path('./data/fonts')
from kivy.core.text import LabelBase
LabelBase.register(name='SourceHanSansSC',fn_regular='SourceHanSansSC-Light.otf')





class MainApp(BoxLayout):

    @run_on_ui_thread
    def statusbar(self, color):
        window = activity.getWindow()
        window.clearFlags(WindowManager.FLAG_TRANSLUCENT_STATUS)
        window.addFlags(WindowManager.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS)
        window.setStatusBarColor(Color.parseColor(color))
        window.setNavigationBarColor(Color.parseColor(color))

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
        # return btn
        return MainApp()
        # return Button(text='Hello World!你好')

TestApp().run()