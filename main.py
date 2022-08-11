from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window

Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

rotate = False

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global rotate
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Man1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.bind(on_press = self.on_press_gender)
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.bind(on_press = self.on_press_layer)
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_gender(self, isistance):
        print("гендер сменен")

    def on_press_layer(self, isistance):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'rotate1'


class rotate1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Man2.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})
        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.bind(on_press = self.gender)
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.bind(on_press = self.layer)
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def gender(self, isistance):
        print("гендер сменен")

    def layer(self, isistance):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'main'

class Screen(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(main(name = 'main'))
        sm.add_widget(rotate1(name = 'rotate1'))
        return sm

app = Screen()
app.run()
