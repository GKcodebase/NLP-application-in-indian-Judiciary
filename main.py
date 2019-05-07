from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import os

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<FileChooserScreen>:
    id: screen1
    
    filechooser: filechooser
    preview_label: preview_label
    
    BoxLayout:
        padding: 20,20
        FileChooserIconView:
            id: filechooser
            on_selection: screen1.selected(filechooser.path, filechooser.selection)
        Label:
            id: paddingLabel
            text: " "
            padding: 10,10
            size_hint: None, None
            size: self.texture_size
        Button:
            text: "Find results"
            font_size: 20        
            size: self.texture_size
            size_hint: None, None
            on_release: 
                screen1.findresult(filechooser.path, filechooser.selection)
                root.manager.current = 'result'
                root.manager.transition.direction = 'up'
        Label:
            id: paddingLabel
            text: " "
            padding: 10,10
            size_hint: None, None
            size: self.texture_size
        ScrollView:
            Label:
                font_size: 20
                text_size: self.width, None
                height: self.texture_size[1]
                padding: 20, 20
                size_hint: 1, None
                size: self.texture_size
                id: preview_label
                text: ""
                color: 0,0,0,1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size

<ResultScreen>:
    id: screen2
    BoxLayout:
        Button:
            text: 'Results page'
        Button:
            text: 'Back to filechooser'
            on_press: 
                root.manager.current = 'filechooser'
                root.manager.transition.direction = 'down'
""")

# Declare both screens
class FileChooserScreen(Screen):
    def __init__(self, **kwargs):
        super(FileChooserScreen, self).__init__(**kwargs)
        cwd = os.getcwd()
        self.filechooser.path = cwd
        
    
    def findresult(self, path, filename):
        '''
        Run actual program.
        '''

    def selected(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as f:
                if filename[0].endswith(".txt") or filename[0].endswith(".py") :
                    self.preview_label.text = f.read()
        except:
                self.preview_label.text = ""

class ResultScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(FileChooserScreen(name='filechooser'))
sm.add_widget(ResultScreen(name='result'))

class ML_ApplicationApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    ML_ApplicationApp().run()