
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text = 'Ква-квадрат!')

if __name__ == "__main__":
    MyApp().run()

'''
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

KV = """
Label:
    font_size: "25sp"
    text: root.data_label
"""

class MyBL(BoxLayout):
    data_label = StringProperty("Квадрат!")
	
class MyApp(App):
    running = True
	
    def build(self):
        return Builder.load_string(KV)
		
    def on_stop(self):
        self.running = False
		
if __name__ == "__main__":
    MyApp().run()
'''    
    
