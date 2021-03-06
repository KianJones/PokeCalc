# import kivy
# kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Stats_Input(GridLayout):

    def __init__(self, **kwargs):
        super(Stats_Input, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Poke_Name'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='Nature'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='Level'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='HP'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='Atk'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='Def'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='SpAtk'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='SpDef'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        
        self.add_widget(Label(text='Speed'))
        self.poke_name = TextInput(multiline=False)
        self.add_widget(self.poke_name)
        

class Results(GridLayout):
    def __init__(self, **kwargs):
        super(Results, self).__init__(**kwargs)
        
        self.cols = 2
        # self.add_widget(Label())
        # self.add_widget(Label())
        # self.add_widget(Label())
        
        self.add_widget(Label(text='IV'))
        self.HP_IV = TextInput(multiline=False)
        self.add_widget(self.HP_IV)
        self.add_widget(Label(text='IV'))
        self.Atk_IV = TextInput(multiline=False)
        self.add_widget(self.Atk_IV)
        self.add_widget(Label(text='IV'))
        self.Def_IV = TextInput(multiline=False)
        self.add_widget(self.Def_IV)
        self.add_widget(Label(text='IV'))
        self.SpAtk_IV = TextInput(multiline=False)
        self.add_widget(self.SpAtk_IV)
        self.add_widget(Label(text='IV'))
        self.SpDef_IV = TextInput(multiline=False)
        self.add_widget(self.SpDef_IV)
        self.add_widget(Label(text='IV'))
        self.Spe_IV = TextInput(multiline=False)
        self.add_widget(self.Spe_IV)
 

class IVCalc(GridLayout):
    def __init__(self, **kwargs):
        super(IVCalc, self).__init__(**kwargs)
        
        self.cols = 2
        
        si = AnchorLayout(anchor_x='left', anchor_y='top')
        res = AnchorLayout(anchor_x='right', anchor_y='bottom')
        calc_but = AnchorLayout(anchor_x='center', anchor_y='bottom')
        
        si.add_widget(Stats_Input())
        res.add_widget(Results())
        calc_but.add_widget(Button(text='Calculate'))
        
        self.add_widget(si)
        self.add_widget(res)
        self.add_widget(calc_but)
        
        
        
class Calc_with_button(AnchorLayout):
    def __init__(self, **kwargs):
        super(Calc_with_button, self).__init__(**kwargs)
        
        si = AnchorLayout(anchor_x='left', anchor_y='top')
        res = AnchorLayout(anchor_x='right', anchor_y='bottom')
        calc_but = AnchorLayout(anchor_x='center', anchor_y='bottom')
        
        si.add_widget(Stats_Input())
        res.add_widget(Results())
        calc_but.add_widget(Button(text='Calculate'))
        
        self.add_widget(si)
        self.add_widget(res)
        self.add_widget(calc_but)
        
class MyApp(App):
    def build(self):
        return Calc_with_button()
        
if __name__ == '__main__':
    MyApp().run()