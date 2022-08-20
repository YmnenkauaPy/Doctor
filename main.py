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
from Text import Dict_of_muscles
from kivy.clock import Clock

gender_="man"  #Мужчина смотрит лицом в камеру
side_="forward"     #Мужчина смотрит лицом в камеру


key = "Двоголовий м'яз плеча"
Window.clearcolor = (0, .8, .9, 1) #установка цвета нового фона
yellow = (2.2,2.4,0.2,1)

class Man1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})
        
        self.fl_layout = FloatLayout()
        self.body = Image(source = "Images_people/Man1.png", pos = (50, -10))
        self.fl_layout.add_widget(self.body)
        main_layout.add_widget(self.fl_layout)
        
        self.fl_layout2 = None
        #кнопки с мышцами

        self.btn_biceps = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",
                          size_hint = (None, None), size = (20, 20), pos = (300, 415))
        self.btn_biceps.bind(on_press = self.on_press_biceps)
        
        self.tailor_muscle = Button(background_normal = "images/Circle.png", background_down = "images/Circle.png",
                          size_hint = (None, None), size = (20, 20), pos = (260, 265))
        self.tailor_muscle.bind(on_press = self.on_press_tailor)
        
        self.fl_layout.add_widget(self.btn_biceps)
        self.fl_layout.add_widget(self.tailor_muscle)
        
        
        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        btn_gender.on_press = self.gender
        layout.add_widget(btn_gender)
        
        btn_layer = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def on_press_biceps(self, instance):
        global key
        key="Двоголовий м'яз плеча"
        self.manager.current = 'Print_info'
        
    def on_press_tailor(self, instance):
        global key
        key = "Кравецький м'яз"
        self.manager.current = 'Print_info'
        

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()

            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos = (80, 300))
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos = (85, 300))
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos = (210, 300))
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos = (335, 300))
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos = (460, 300))
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos = (585, 300))

            self.bone.on_press = self.skeleton

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def skeleton(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Bone1'
#########################################################################################################################        
    def gender(self):
        global gender_
        global side_
        if gender_=="man" and side_=="forward":
            self.body.source="Images_people/Woman1.png"   #woman1
            self.btn_biceps.pos=(320,428)   #biceps
            self.tailor_muscle.pos=(290,265)  #tailor
            gender_="woman"
            
        elif gender_=="woman" and side_=="forward":
            self.body.source="Images_people/Man1.png"   #man1
            self.btn_biceps.pos=(300,405)   #biceps
            self.tailor_muscle.pos=(260,265)    #tailor
            gender_="man"
            
        elif gender_ =="man" and side_ =="back":
            self.body.source="Images_people/Woman2.png" #woman2
            gender_="woman"
        elif gender_=="woman" and side_ =="back":
            self.body.source="Images_people/Man2.png"   #man2
            gender_="man"
#################################################################################################################################################
    def rotate(self):
        global gender_
        global side_
        if gender_=="man" and side_=="forward":
            self.body.source="Images_people/Man2.png"       #man2
            self.fl_layout.remove_widget(self.btn_biceps)
            self.fl_layout.remove_widget(self.tailor_muscle)
            side_="back"
            print(side_)
        elif gender_=="woman" and side_=="forward":
            self.body.source="Images_people/Woman2.png"     #woman2
            self.fl_layout.remove_widget(self.btn_biceps)
            self.fl_layout.remove_widget(self.tailor_muscle)
            side_="back"
            print(side_)
        elif gender_ =="man" and side_ =="back":
            self.body.source="Images_people/Man1.png"   #man1
            self.fl_layout.add_widget(self.btn_biceps)
            self.fl_layout.add_widget(self.tailor_muscle)
            self.btn_biceps.pos=(300,405)   #biceps
            self.tailor_muscle.pos=(260,265)    #tailor
            side_="forward"
            print(side_)
        elif gender_=="woman" and side_ =="back":
            self.body.source="Images_people/Woman1.png"     #woman1
            self.fl_layout.add_widget(self.btn_biceps)
            self.fl_layout.add_widget(self.tailor_muscle)
            self.btn_biceps.pos=(320,428)   #biceps
            self.tailor_muscle.pos=(290,265)  #tailor
            side_="forward"
            print(side_)
###########################################################################################################################
class Bone1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation = "horizontal")
        layout = BoxLayout(orientation = "vertical", spacing = 5, pos_hint = {"x" : 0.2, "y" : 0.6})

        self.body = Image(source = "Images_people/Bone1.png", pos_hint = {"center_y" : .5, "center_x" : .5, "x" : .9})
        main_layout.add_widget(self.body)

        self.fl_layout2 = None

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        layout.add_widget(btn_gender)
        

        btn_layer = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75},background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()

            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos = (80, 300))
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos = (85, 300))
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos = (210, 300))
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos = (335, 300))
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos = (460, 300))
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos = (585, 300))

            self.muscle.on_press = self.muscle_layer

            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def muscle_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
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

        self.fl_layout2 = None

        btn_gender = Button(text = "Пол", size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_color = yellow)
        layout.add_widget(btn_gender)
        

        btn_layer = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png", size_hint = (None, None), size = (80, 80), pos_hint = {"x" : .75})
        btn_layer.on_press = self.layer
        layout.add_widget(btn_layer)

        btn_rotate = Button(size_hint = (None, None), size = (70, 70), pos_hint = {"x" : .75}, background_normal = "images/Rotate.png", background_down = "images/Rotate.png")
        btn_rotate.on_press = self.rotate
        layout.add_widget(btn_rotate)

        main_layout.add_widget(layout)

        self.add_widget(main_layout)

    def layer(self):
        if not self.fl_layout2:
            self.fl_layout2 = FloatLayout()

            self.frame = Button(background_normal = "images/frame.png", background_down = "images/frame.png",
                        size_hint = (None, None), size = (635, 125), pos = (80, 300))
            self.bone = Button(background_normal = "images/Bone.png", background_down = "images/Bone.png",
                        size_hint = (None, None), size = (125, 125), pos = (85, 300))
            self.muscle = Button(background_normal = "images/muscle.png", background_down = "images/muscle.png",
                        size_hint = (None, None), size = (125, 125), pos = (210, 300))
            self.nerves = Button(background_normal = "images/nerves.png", background_down = "images/nerves.png",
                        size_hint = (None, None), size = (125, 125), pos = (335, 300))
            self.organs = Button(background_normal = "images/organ.png", background_down = "images/organ.png",
                        size_hint = (None, None), size = (125, 125), pos = (460, 300))
            self.skin = Button(background_normal = "images/skin.png", background_down = "images/skin.png",
                        size_hint = (None, None), size = (125, 125), pos = (585, 300))
                        
            self.muscle.on_press = self.muscle_layer
            self.fl_layout2.add_widget(self.frame)
            self.fl_layout2.add_widget(self.bone)
            self.fl_layout2.add_widget(self.muscle)
            self.fl_layout2.add_widget(self.nerves)
            self.fl_layout2.add_widget(self.organs)
            self.fl_layout2.add_widget(self.skin)
            self.add_widget(self.fl_layout2)
        else:
            self.remove_widget(self.fl_layout2)
            self.fl_layout2 = None

    def muscle_layer(self):
        self.remove_widget(self.fl_layout2)
        self.fl_layout2=None
        self.manager.current = 'Man1'

    def rotate(self):
        self.manager.current = 'Bone1'

class Print_info(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        global key
        float_layout = FloatLayout()
        
        back_gr=Button(text = "", background_color = (0, 0, 0, 1), size_hint = (None, None), size = (600, 500), pos = (50, 50))
        back_gr.opacity = 0.6
        back_gr_white=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 150), pos = (100, 380))
        back_gr_white.opacity = 0.4
        back_gr_white2=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 105), pos = (100, 278))
        back_gr_white2.opacity = 0.3
        back_gr_white3=Button(text = "", background_color = (1, 1, 1, 1), size_hint = (None, None), size = (520, 200), pos = (100, 80))
        back_gr_white3.opacity = 0.2
        

        self.name_muscle = Label(text = key, pos=(-40,210),font_size='25sp')
        function_text = Label(text = "Функція", pos=(-50,180),font_size='20sp')
        self.function = Label(text = Dict_of_muscles[key]['Функція'], pos=(-40,125),font_size='20sp')
        injury_text = Label(text = "Травми/Хвороби", pos=(-50,60),font_size='20sp')
        self.injury = Label(text = Dict_of_muscles[key]['Травми/Хвороби'], pos=(-50,10),font_size='20sp')
        exercices_text = Label(text = "Корисні вправи", pos=(-50, -50),font_size='20sp')
        self.exercices = Label(text = Dict_of_muscles[key]['Корисні вправи'], pos=(-50, -100),font_size='20sp')

        Clock.schedule_interval(self.Update, 0.1)

        btn_close_bg = Button(text = "Нажми, чтобы закрыть", size_hint = (None, None), size = (190, 50), pos=(400,0), background_color = yellow)
        btn_close_bg.bind(on_press=self.close_info)
        
        float_layout.add_widget(back_gr_white)
        float_layout.add_widget(back_gr_white2)
        float_layout.add_widget(back_gr_white3)
        float_layout.add_widget(back_gr)
        float_layout.add_widget(self.name_muscle)
        float_layout.add_widget(function_text)
        float_layout.add_widget(self.function)
        float_layout.add_widget(injury_text)
        float_layout.add_widget(self.injury)
        float_layout.add_widget(exercices_text)
        float_layout.add_widget(self.exercices)
        float_layout.add_widget(btn_close_bg)
        self.add_widget(float_layout)

    def Update(self, *args):
        global key
        self.name_muscle.text = key
        self.function.text = Dict_of_muscles[key]['Функція']
        self.injury.text = Dict_of_muscles[key]['Травми/Хвороби']

    def close_info(self, instance):
        self.manager.current = "Man1"

class Screen(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(Man1(name = 'Man1'))
        sm.add_widget(Bone1(name='Bone1'))
        sm.add_widget(Bone2(name='Bone2'))
        sm.add_widget(Print_info(name='Print_info'))
        
        return sm

app = Screen()
app.run()
