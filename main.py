from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import (Color,Rectangle)

Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

class Man1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        self.fl_layout = FloatLayout()
        body = Image(source = "Images_people/Man1.png", pos = (50, -10))
        self.fl_layout.add_widget(body)
        main_layout.add_widget(self.fl_layout)
        
        self.fl_layout2 = None

        btn_biceps = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",
                          size_hint = (None, None), size = (20, 20), pos = (300, 415))
        btn_biceps.bind(on_press = self.on_press_biceps)
        
        self.fl_layout.add_widget(btn_biceps)
        
        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_gender.on_press = self.gender
        layout.add_widget(btn_gender)
        
        btn_layer = Button(text = "Слой", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_biceps(self, instance):
        self.manager.current = 'Print_info'
        
    def gender(self):
        self.manager.current = 'Woman1'

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()
            self.box = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (100, 100), pos = (290, 350))
            self.box.on_press = self.skeleton
            self.fl_layout2.add_widget(self.box)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2=None

    def skeleton(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
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

        btn_rotate = Button( size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75},background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def gender(self):
        self.manager.current = 'Woman2'

    def layer(self):
        self.fl_layout2 = FloatLayout()
        self.box = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                    size_hint = (None, None), size = (100, 100), pos = (290, 350))
        self.box.on_press = self.skeleton
        self.fl_layout2.add_widget(self.box)
        self.add_widget(self.fl_layout2)

    def skeleton(self):
        self.fl_layout2.remove_widget(self.box)
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

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
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

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
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

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75},background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
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

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_layer(self):
        self.manager.current = 'Man2'

    def rotate(self):
        self.manager.current = 'Bone1'

class Print_info(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        flot_layout=FloatLayout()
        
        back_gr=Button(text = "BG",background_color=(0,0,0,1),size_hint=(None,None),size=(600,500),pos=(50,50))
        back_gr.opacity=0.8
        flot_layout.add_widget(back_gr)
        
        btn_close_bg = Button(text = "Нажми, чтобы закрыть", size_hint = (None, None), size = (190, 50), pos=(400,0), background_color = yellow)
        btn_close_bg.bind(on_press=self.close_info)
        
        flot_layout.add_widget(btn_close_bg)


    def close_info(self,instance):
        self.manager.current = "Man1"

class Screen(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Man1(name = 'Man1'))
        sm.add_widget(Man2(name = 'Man2'))
        sm.add_widget(Woman1(name = 'Woman1'))
        sm.add_widget(Woman2(name = 'Woman2'))
        sm.add_widget(Bone1(name='Bone1'))
        sm.add_widget(Bone2(name='Bone2'))
        sm.add_widget(Print_info(name='Print_info'))
        
        return sm

app = Screen()
app.run()
