from kivy.core.window import Window
Window.size = (1600, 900)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.popup import Popup
from kivy.clock import Clock


from nltk.tokenize import word_tokenize
from nltk.classify import ClassifierI
from statistics import mode

import nltk
from docutils.parsers.rst.directives import encoding
nltk.download('punkt')

import pickle
import os
import Data.kanooncrawler as kw

resultFound = 0
validFile = 0
law_found=' '

class Vote_(ClassifierI):
    def __init__(self, *classifier_):
        self._classifier_ = classifier_

    def classify(self, feature):
        vote = []
        for c in self._classifier_:
            v = c.classify(feature)
            vote.append(v)
        return mode(vote)

    def confidence(self, feature):
        vote = []
        for c in self._classifier:
            v = c.classify(feature)
            vote.append(v)

        choice_vote = vote.count(mode(vote))
        confidence_ = choice_vote / len(vote)
        return confidence_

law_dict =    {
  "law_1": "ATTRIBUTION, ACKNOWLEDGMENT AND DISPATCH OF ELECTRONIC RECORDS",
  "law_2": "DIGITAL SIGNATURE AND ELECTRONIC SIGNATURE",
  "law_3": "DUTIES OF SUBSCRIBERS",
  "law_4": "ELECTRONIC GOVERNANCE",
  "law_5": "ELECTRONIC SIGNATURE CERTIFICATES",
  "law_6": "INTERMEDIARIES NOT TO BE LIABLE IN CERTAIN CASES",
  "law_7": "EXAMINER OF ELECTRONIC EVIDENCE",
  "law_8": "MISCELLANEOUS",
  "law_9": "NETWORK SERVICE PROVIDERS NOT TO BE LIABLE IN CERTAIN CASES",
  "law_10": "section 65 66a information technology act",
  "law_11": "PENALTIES, COMPENSATION AND ADJUDICATION",
  "law_12": "REGULATION OF CERTIFYING AUTHORITIES",
  "law_13": "SECURE ELECTRONIC RECORDS",
  "law_14": "Cyber Appellate Tribunal",
  
}


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<SimplePopup>:
    id:pop
    size_hint: .5,.5
    auto_dismiss: False
    font_size: 20
    title: ''
    BoxLayout:
        orientation: "vertical"
        Label: 
            font_size: 15
            text: "WELCOME TO LAW FINDER"
        Button:
            padding: 20,20
            font_size: 25
            text: 'CHOOSE COMPLAINT LETTER'
            on_press: pop.dismiss()

<FileChooserScreen>:
    id: screen1
    
    filechooser: filechooser
    preview_label: preview_label
    
    BoxLayout:
        orientation: "horizontal"
        padding: 20,20
        BoxLayout:
            orientation: "vertical"
            FileChooserListView:
                id: filechooser
                
                font_size: 20                
                size_hint: None, .5
                width: 700
                
                on_selection: screen1.selected(filechooser.path, filechooser.selection)
            Label:
                font_size: 20
                width: 700
                height: 150
                size_hint: None, None
                text: "*INSTRUCTIONS*"
            Label:
                font_size: 20
                width: 700
                height: 50
                size_hint: None, None
                text: "1. Select complaint letter.txt from above window."
            Label:
                font_size: 20
                width: 700
                height: 50
                size_hint: None, None
                text: "2. Click Find Results to find and read applicable law."
            Label:
                font_size: 20
                width: 700
                height: 50
                size_hint: None, None
                text: "3. Click Show Judgements to find and read previous judgements related to law."
            Label:
                font_size: 20
                width: 700
                height: 200
                size_hint: None, None
                text: ""
        Label:
            id: paddingLabel
            text: " "
            padding: 10,10
            size_hint: None, None
            size: self.texture_size
        BoxLayout:
            size_hint: None, None
            orientation: "vertical"
            width: 200
            Button:
                padding: 10,10
                text: "Find Results"
                font_size: 25        
                size_hint: None, None
                size: self.texture_size 
                on_release: 
                    screen1.findresult(filechooser.path, filechooser.selection)
                    
            Label:
                id: paddingLabel
                text: " "
                padding: 10,10
                size_hint: None, None
                size: self.texture_size
            
            Button:
                padding: 10,10
                text: "Show Judgements"
                font_size: 20        
                size: self.texture_size
                size_hint: None, None
                on_release: 
                    screen1.showjudgement()
            Label:
                id: paddingLabel
                text: " "
                padding: 10,150
                size_hint: None, None
                size: self.texture_size
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
    
    result_label: result_label
    
    BoxLayout:
    	id: blyout
    	padding: 20,20
        ScrollView:
            Label:
                font_size: 20
                text_size: self.width, None
                height: self.texture_size[1]
                padding: 20, 20
                size_hint: 1, None
                size: self.texture_size
                id: result_label
                text: ""
                color: 1,0,0,1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
            
        Label:
            id: paddingLabel
            text: " "
            padding: 10,10
            size_hint: None, None
            size: self.texture_size
        
        Button:
            text: 'Back to filechooser'
            on_press: 
                root.manager.current = 'filechooser'
                root.manager.transition.direction = 'down'
""")


class SimplePopup(Popup):
    pass

# Declare both screens
class FileChooserScreen(Screen):
    resultFound = 0
    validFile = 0
    def __init__(self, **kwargs):
        super(FileChooserScreen, self).__init__(**kwargs)
        cwd = os.getcwd()
        cwd = cwd + "/Data/Complaint letters"
        self.filechooser.path = cwd
    
    def findresult(self, path, filename):
        global law_found
        global resultFound
        global validFile
        '''
        Run actual program.
        '''
        if (validFile == 1):
            if (filename[0].endswith(".txt")):
                selectedFile  = open(filename[0],"r").read()
                
                word_feature = open("Data/pickled_algorithms/word_features.pickle", "rb")
                word_features = pickle.load(word_feature)
                word_feature.close()
                
                ### Loading Saved Classifiers
                open_file_LSV = open("Data/pickled_algorithms/LinearSVC_classifier.pickle", "rb")
                LinearSVC = pickle.load(open_file_LSV)
                open_file_LSV.close()
    
                open_file_SGDC = open("Data/pickled_algorithms/SGDC_classifier.pickle", "rb")
                SGDC = pickle.load(open_file_SGDC)
                open_file_SGDC.close()
                
                
                open_file_NB = open("Data/pickled_algorithms/naivebayes.pickle", "rb")
                naive_bayes = pickle.load(open_file_NB)
                open_file_NB.close()
                
                open_file_MNB = open("Data/pickled_algorithms/MNB_classifier.pickle", "rb")
                MNB = pickle.load(open_file_MNB)
                open_file_MNB.close()
                
                open_file_BNB = open("Data/pickled_algorithms/BernoulliNB_classifier.pickle", "rb")
                BernoulliNB= pickle.load(open_file_BNB)
                open_file_BNB.close()
                
                open_file_LR = open("Data/pickled_algorithms/LogisticRegression_classifier.pickle", "rb")
                LogisticRegression = pickle.load(open_file_LR)
                open_file_LR.close()
                
                # Making Instance of the class vote
                Classify = Vote_(LogisticRegression, SGDC,naive_bayes,LinearSVC,MNB,BernoulliNB)
                
                word = word_tokenize(selectedFile)
                feature = {}
                for w in word_features:
                    feature[w] = (w in word)
                
                query = Classify.classify(feature)
                
                law_found = law_dict[query]
                
                #print(law_found)
                
                lawPath = "Data/Laws/" + query + ".txt"
                enc = "iso-8859-15"
                finalResult  = open(lawPath,"r", encoding=enc).read()
                
                finalResult = "MOST APPLICABLE LAW IS: \n------------------------------------------\n\n" + finalResult
                
                self.preview_label.text = finalResult
                
                resultFound = 1
                validFile = 0
                
                #print(finalResult)
                
                '''
                rs = ResultScreen()
                rs.showresult(selectedFile)
                print ("\nshow result on next screen.")
                '''

    def selected(self, path, filename):
        global resultFound
        global validFile
        try:
            with open(os.path.join(path, filename[0])) as f:
                if filename[0].endswith(".txt"):
                    self.preview_label.text = f.read()
                    resultFound = 0
                    validFile = 1
        except:
                self.preview_label.text = ""
                resultFound = 0
                validFile = 0
                
    def showjudgement(self):
        '''
        '''
        if (resultFound == 1):
            #print (law_found)
            self.preview_label.text = kw.crawl(law_found)
        

    def showresult(self):
        '''
        '''

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

    def showresult(self, selectedFile):
        print (selectedFile)
        self.result_label.text = selectedFile

# Create the screen manager
sm = ScreenManager()
sm.add_widget(FileChooserScreen(name='filechooser'))
sm.add_widget(ResultScreen(name='result'))

class ML_ApplicationApp(App):
    
    def show_popup(self, dt):
        SimplePopup().open()

    def build(self):
        Clock.schedule_once(self.show_popup, 1)
        return sm

if __name__ == '__main__':
    #Window.fullscreen = True
    ML_ApplicationApp().run()
