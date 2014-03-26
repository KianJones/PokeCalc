from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class IVCalc(GridLayout):

    def __init__(self, **kwargs):
        super(IVCalc, self).__init__(**kwargs)
        self.cols = 9
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
        
        
class MyApp(App):
    def build(self):
        return LoginScreen()
        
if __name__ is '__main__':
    MyApp().run()