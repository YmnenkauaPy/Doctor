from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window


Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

class man1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/Man1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.on_press = self.on_press_gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.on_press_layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_gender(self):
        self.manager.current = 'woman1'

    def on_press_layer(self):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'man2'


class man2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/Man2.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})
        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.on_press = self.gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def gender(self):
        self.manager.current = 'woman1'

    def layer(self):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'man1'

class woman1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/Woman1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.on_press = self.on_press_gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.on_press_layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_gender(self):
        self.manager.current = 'man1'

    def on_press_layer(self):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'woman2'

class woman2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/Woman2.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        btn_gender.on_press = self.on_press_gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.on_press_layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_gender(self):
        self.manager.current = 'man1'

    def on_press_layer(self):
        print("Идет выбор слоя...")
    
    def rotate(self):
        self.manager.current = 'woman1'

class Screen(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(man1(name = 'man1'))
        sm.add_widget(man2(name = 'man2'))
        sm.add_widget(woman1(name = 'woman1'))
        sm.add_widget(woman2(name = 'woman2'))
        return sm

app = Screen()
app.run()
