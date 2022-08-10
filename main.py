from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window

Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона

yellow = (2.2,2.4,0.2,1)

class Main(App):
    def build(self):
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.1, "y" : 0.49})

        body1 = Image(source = "Body.png", pos_hint = {"center_y" : .5})
        main_layout.add_widget(body1)

        btn_gender = Button(text = "Пол", size_hint = (0, 0), pos_hint = {"x" : .75},background_color=yellow,)
        btn_gender.bind(on_press=self.on_press_gender)
        layout.add_widget(btn_gender)
        

        btn_layer = Button(text = "Слой", size_hint = (0, 0), pos_hint = {"x" : .75},background_color=yellow)
        btn_layer.bind(on_press=self.on_press_layer)
        layout.add_widget(btn_layer)

        btn_rotate = Button(text = "Поворот", size_hint = (0, 0), pos_hint = {"x" : .75},background_color=yellow)
        btn_rotate.bind(on_press=self.on_press_rotate)
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        return main_layout
    def on_press_gender(self,isistance):
        print("гендер сменен")
    def on_press_layer(self,isistance):
        print("Идет выбор слоя...")
    def on_press_rotate(self,isistance):
        print("Поворот!")

Main().run()
