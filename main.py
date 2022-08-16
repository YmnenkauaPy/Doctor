from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window


Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

class Man1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        fl_layout=FloatLayout()
        body = Image(source = "Images_people/Man1.png",pos=(50,-10))
        fl_layout.add_widget(body)
        main_layout.add_widget(fl_layout)
        
        btn_biceps=Button(background_normal="An_images/Circle.png",background_down="An_images/Circle.png",
                          size_hint=(None,None),size=(20,20),pos=(300,415))
        btn_biceps.bind(on_press=self.on_press_biceps)
        
        fl_layout.add_widget(btn_biceps)
        
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
    def on_press_biceps(self,instance):
        print("Это бицепс...")

    def on_press_gender(self):
        self.manager.current = 'Woman1'

    def on_press_layer(self):
        self.manager.current = 'Bone1'
    
    def rotate(self):
        self.manager.current = 'Man2'


class Man2(Screen):
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
        self.manager.current = 'Woman2'

    def layer(self):
        self.manager.current = 'Bone2'
    
    def rotate(self):
        self.manager.current = 'Man1'

class Woman1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/woman1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

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
        self.manager.current = 'Man1'

    def on_press_layer(self):
        self.manager.current = 'Bone1'
    
    def rotate(self):
        self.manager.current = 'Woman2'

class Woman2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        body = Image(source = "Images_people/woman2.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

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
        self.manager.current = 'Man2'

    def on_press_layer(self):
        self.manager.current = 'Bone2'

    def rotate(self):
        self.manager.current = 'Woman1'

class Bone1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        self.body = Image(source = "Images_people/Bone1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(self.body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        #btn_gender.on_press = self.on_press_gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.on_press_layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_layer(self):
        self.manager.current = 'Man1'

    def rotate(self):
        self.manager.current = 'Bone2'

class Bone2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        self.body = Image(source = "Images_people/Bone2.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})

        main_layout.add_widget(self.body)

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow,)
        #btn_gender.on_press = self.on_press_gender
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.on_press_layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_layer(self):
        self.manager.current = 'Man2'

    def rotate(self):
        self.manager.current = 'Bone1'

class Screen(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Man1(name = 'Man1'))
        sm.add_widget(Man2(name = 'Man2'))
        sm.add_widget(Woman1(name = 'Woman1'))
        sm.add_widget(Woman2(name = 'Woman2'))
        sm.add_widget(Bone1(name='Bone1'))
        sm.add_widget(Bone2(name='Bone2'))
        
        return sm

app = Screen()
app.run()
