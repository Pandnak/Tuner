'''
----------------------------------------------------------
Run this line one time before run script:

export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 
----------------------------------------------------------
'''

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


KV = """
BoxLayout:
    orientation: 'vertical'
    Label:
        text: 'Text'
        font_size: '30sp'
        size: self.texture_size
    Button:
        text: 'Start'
        font_size: '30sp'
        bold: True
        background_color: '#00DDC3'
        on_state:
            print("Button_1 current state is {}".format(self.state))
    Button:
        text: 'Stop'
        font_size: '30sp'
        bold: True
        background_color: '#00DDC3'
        on_state:
            print("Button_2 current state is {}".format(self.state))
"""
	
class MyApp(App):
    running = True
	
    def build(self):
        return Builder.load_string(KV)
		
    def on_stop(self):
        self.running = False
		
if __name__ == "__main__":
    MyApp().run() 

